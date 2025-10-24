"""
Job Processor Service
Handles job queue management, status tracking, and result storage
"""

import json
import shutil
from pathlib import Path
from typing import Optional, Dict, Any
from datetime import datetime

from ..models.job_models import JobResult, TransferReceipt
from ...shared.schemas.job_packet import JobPacket


class JobProcessor:
    """Manages job queue and processing lifecycle"""
    
    def __init__(self, queue_root: str = ".3ox/queue"):
        self.queue_root = Path(queue_root)
        self.new_queue = self.queue_root / "NEW"
        self.claimed_queue = self.queue_root / "CLAIMED"
        self.results_queue = self.queue_root / "RESULTS"
        self.receipts_queue = self.queue_root / "RECEIPTS"
        
        # Ensure queue directories exist
        for queue_dir in [self.new_queue, self.claimed_queue, self.results_queue, self.receipts_queue]:
            queue_dir.mkdir(parents=True, exist_ok=True)
    
    def submit_job(self, job_packet: JobPacket) -> str:
        """Submit job to NEW queue"""
        job_file = self.new_queue / f"{job_packet.id}.job.json"
        
        with open(job_file, 'w') as f:
            json.dump(job_packet.dict(), f, indent=2)
        
        return job_packet.id
    
    def claim_job(self, job_id: str) -> Optional[JobPacket]:
        """Move job from NEW to CLAIMED queue"""
        new_file = self.new_queue / f"{job_id}.job.json"
        claimed_file = self.claimed_queue / f"{job_id}.job.json"
        
        if not new_file.exists():
            return None
        
        # Move file to claimed queue
        shutil.move(str(new_file), str(claimed_file))
        
        # Load and return job packet
        with open(claimed_file, 'r') as f:
            job_data = json.load(f)
        
        return JobPacket(**job_data)
    
    def get_job_result(self, job_id: str) -> Optional[Dict[str, Any]]:
        """Get job result from RESULTS queue"""
        result_file = self.results_queue / f"{job_id}.result.json"
        
        if not result_file.exists():
            return None
        
        with open(result_file, 'r') as f:
            return json.load(f)
    
    def store_job_result(self, job_id: str, result: JobResult):
        """Store job result in RESULTS queue"""
        result_file = self.results_queue / f"{job_id}.result.json"
        
        with open(result_file, 'w') as f:
            json.dump(result.dict(), f, indent=2)
        
        # Create transfer receipt
        self._create_transfer_receipt(job_id, result)
    
    def _create_transfer_receipt(self, job_id: str, result: JobResult):
        """Create immutable transfer receipt"""
        receipt = TransferReceipt(
            job_id=job_id,
            start_time=datetime.now().isoformat(),
            end_time=datetime.now().isoformat(),
            gregorian_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            sirius_time="⧗-25.108",  # Would use proper Sirius time in real implementation
            offline=result.offline,
            connector=result.connector_used,
            cost_estimate=result.cost_estimate,
            files_touched=result.files_touched,
            checksums={},  # Would calculate actual checksums
            ops_required=result.status == "SUCCESS" and len(result.files_touched) > 0
        )
        
        receipt_file = self.receipts_queue / f"{job_id}.receipt.json"
        
        with open(receipt_file, 'w') as f:
            json.dump(receipt.dict(), f, indent=2)
    
    def process_confirmation(self, job_id: str, confirmation: Dict[str, Any]) -> bool:
        """Process job confirmation (OPS token, sensitive data, etc.)"""
        # In a real implementation, this would:
        # 1. Validate OPS token if provided
        # 2. Handle sensitive data confirmation
        # 3. Update job status accordingly
        
        # For now, just return True to allow processing
        return True
    
    def get_job_status(self, job_id: str) -> str:
        """Get current job status"""
        if (self.results_queue / f"{job_id}.result.json").exists():
            return "COMPLETED"
        elif (self.claimed_queue / f"{job_id}.job.json").exists():
            return "PROCESSING"
        elif (self.new_queue / f"{job_id}.job.json").exists():
            return "QUEUED"
        else:
            return "NOT_FOUND"