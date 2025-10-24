"""
Job Models for 3OX Backend
Data models for job processing and management
"""

from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class JobRequest(BaseModel):
    """Request model for job submission"""
    role: str = "@MASTER"
    prompt: str
    targets: List[str] = []
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


class JobStatus(BaseModel):
    """Job status enumeration"""
    QUEUED = "QUEUED"
    CLAIMED = "CLAIMED"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    REQUIRES_CONFIRMATION = "REQUIRES_CONFIRMATION"


class ConfirmationRequest(BaseModel):
    """Request model for job confirmation"""
    confirmed: bool
    ops_token: Optional[str] = None
    sensitive_confirmed: bool = False
    additional_data: Optional[Dict[str, Any]] = None