"""
3OX FastAPI Backend
Main application entry point for job processing engine
"""

import os
import asyncio
import json
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .services.job_processor import JobProcessor
from .services.routing_brain import RoutingBrain
from .services.offline_executor import OfflineExecutor
from .services.online_connector import OnlineConnector
from .models.job_models import JobRequest, JobResponse, JobStatus
from ..shared.schemas.job_packet import JobPacket, JobResult, TransferReceipt
from ..shared.llmd.validator import LLMDValidator
from ..shared.security.ops_manager import OPSManager


# Initialize FastAPI app
app = FastAPI(
    title="3OX CLI Backend",
    description="Offline-first command bridge with Tauri frontend",
    version="1.0.0"
)

# CORS middleware for Tauri frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify Tauri app origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global services
job_processor = JobProcessor()
routing_brain = RoutingBrain()
offline_executor = OfflineExecutor()
online_connector = OnlineConnector()
ops_manager = OPSManager()


class JobRequest(BaseModel):
    """Request model for job submission"""
    role: str = "@MASTER"
    prompt: str
    targets: list = []
    sensitive: bool = False
    allow_online: bool = False
    force_online: bool = False


class JobResponse(BaseModel):
    """Response model for job status"""
    job_id: str
    status: str
    message: str
    result_data: Optional[Dict[str, Any]] = None
    requires_confirmation: bool = False
    confirmation_message: Optional[str] = None


@app.get("/")
async def root():
    """Health check endpoint"""
    return {"status": "3OX CLI Backend Running", "timestamp": datetime.now().isoformat()}


@app.post("/api/3oxjob", response_model=JobResponse)
async def submit_job(request: JobRequest, background_tasks: BackgroundTasks):
    """Submit a new job to the 3OX processing queue"""
    try:
        # Create job packet
        job_packet = JobPacket(
            prompt=request.prompt,
            role=request.role,
            targets=request.targets,
            sensitive=request.sensitive,
            allow_online=request.allow_online or request.force_online,
            ops_action=ops_manager.check_ops_required(request.prompt, request.targets)
        )
        
        # Check for OPS requirements
        if job_packet.ops_action:
            if not request.force_online:  # This would be a token in real implementation
                return JobResponse(
                    job_id=job_packet.id,
                    status="requires_ops_confirmation",
                    message="This action requires OPS authorization",
                    requires_confirmation=True,
                    confirmation_message="This action modifies protected resources. Please confirm with OPS token."
                )
        
        # Check for sensitive data handling
        if job_packet.sensitive and job_packet.allow_online:
            return JobResponse(
                job_id=job_packet.id,
                status="requires_sensitive_confirmation",
                message="Sensitive data detected",
                requires_confirmation=True,
                confirmation_message="This action involves sensitive data. Confirm to proceed with redaction."
            )
        
        # Submit job for processing
        background_tasks.add_task(process_job_async, job_packet)
        
        return JobResponse(
            job_id=job_packet.id,
            status="queued",
            message="Job submitted successfully"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Job submission failed: {str(e)}")


@app.get("/api/job/{job_id}")
async def get_job_status(job_id: str):
    """Get job status and results"""
    try:
        result = job_processor.get_job_result(job_id)
        if result:
            return result
        else:
            raise HTTPException(status_code=404, detail="Job not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get job status: {str(e)}")


@app.post("/api/confirm/{job_id}")
async def confirm_job(job_id: str, confirmation: Dict[str, Any]):
    """Confirm a job that requires user confirmation"""
    try:
        # Process confirmation (OPS token, sensitive data, etc.)
        success = job_processor.process_confirmation(job_id, confirmation)
        
        if success:
            return {"status": "confirmed", "message": "Job confirmed and processing"}
        else:
            raise HTTPException(status_code=400, detail="Invalid confirmation")
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Confirmation failed: {str(e)}")


async def process_job_async(job_packet: JobPacket):
    """Background task to process job"""
    try:
        # Move job to CLAIMED status
        job_processor.claim_job(job_packet.id)
        
        # Determine execution path
        if should_use_offline_execution(job_packet):
            result = await offline_executor.execute_job(job_packet)
        else:
            result = await online_connector.execute_job(job_packet)
        
        # Store result
        job_processor.store_job_result(job_packet.id, result)
        
    except Exception as e:
        # Store error result
        error_result = JobResult(
            job_id=job_packet.id,
            status="FAILED",
            error_message=str(e)
        )
        job_processor.store_job_result(job_packet.id, error_result)


def should_use_offline_execution(job_packet: JobPacket) -> bool:
    """Determine if job should be executed offline"""
    # Default to offline unless explicitly requiring online
    if not job_packet.allow_online:
        return True
    
    # Check if job requires online resources
    online_required_keywords = [
        "search", "web", "api", "download", "upload", "email", "slack"
    ]
    
    prompt_lower = job_packet.prompt.lower()
    for keyword in online_required_keywords:
        if keyword in prompt_lower:
            return False
    
    return True


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)