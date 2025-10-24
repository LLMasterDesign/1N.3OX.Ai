"""
3OX Job Packet Schema
Based on the chatlog specifications for job queue system
"""

from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
import uuid


class JobMetadata(BaseModel):
    """Job metadata container"""
    workspace: Optional[str] = None
    app: str = "3oxbar"
    estimated_tokens: Optional[int] = None
    complexity_score: Optional[float] = None


class JobPacket(BaseModel):
    """Main job packet structure for 3OX queue system"""
    id: str = Field(default_factory=lambda: f"3ox-{datetime.now().strftime('%Y%m%d-%H%M%S')}-{str(uuid.uuid4())[:8]}")
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat() + "Z")
    sirius_time: Optional[str] = None  # Will be injected by LLMD validator
    user: str = "rvnx/lucius"  # Default user
    role: str = "@MASTER"  # Default role
    mode: str = "!ANALYTICAL"  # Default mode
    prompt: str
    targets: List[str] = Field(default_factory=list)
    sensitive: bool = False
    allow_online: bool = False
    ops_action: bool = False
    metadata: JobMetadata = Field(default_factory=JobMetadata)
    
    # Additional fields for processing
    status: str = "NEW"  # NEW, CLAIMED, PROCESSING, COMPLETED, FAILED
    priority: int = 1  # 1-5 priority scale
    retry_count: int = 0
    max_retries: int = 3


class JobResult(BaseModel):
    """Job result structure"""
    job_id: str
    status: str  # SUCCESS, FAILED, PARTIAL
    result_data: Dict[str, Any] = Field(default_factory=dict)
    error_message: Optional[str] = None
    files_touched: List[str] = Field(default_factory=list)
    execution_time: float = 0.0
    offline: bool = True
    connector_used: Optional[str] = None
    cost_estimate: Optional[float] = None


class TransferReceipt(BaseModel):
    """Immutable job receipt for audit trail"""
    job_id: str
    start_time: str
    end_time: str
    gregorian_time: str
    sirius_time: str
    offline: bool
    connector: Optional[str] = None
    cost_estimate: Optional[float] = None
    files_touched: List[str] = Field(default_factory=list)
    checksums: Dict[str, str] = Field(default_factory=dict)
    redaction_log: Optional[Dict[str, Any]] = None
    ops_required: bool = False
    human_confirmed: bool = False


class OutReport(BaseModel):
    """0UT.3OX report for station reporting"""
    header: Dict[str, str] = Field(default_factory=lambda: {
        "stratos": "STRATOS-1",
        "station": "RVNx.BASE",
        "timestamp": "",
        "type": "status"
    })
    payload: Dict[str, Any] = Field(default_factory=dict)
    routing: Dict[str, str] = Field(default_factory=lambda: {
        "priority": "normal",
        "destination": "CMD.BRIDGE"
    })