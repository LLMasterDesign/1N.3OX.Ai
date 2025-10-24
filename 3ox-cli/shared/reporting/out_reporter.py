"""
0UT.3OX Reporting System
Generates station reports for CMD.listener integration
Based on chatlog specifications
"""

import yaml
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional, List

from ..schemas.job_packet import OutReport


class SiriusCalendar:
    """Sirius calendar time converter"""
    
    @staticmethod
    def get_sirius_time() -> str:
        """Generate Sirius time format: ⧗-25.108"""
        now = datetime.now()
        # Simplified Sirius time calculation
        # In real implementation, this would use proper Sirius calendar
        year = now.year - 2000
        day_of_year = now.timetuple().tm_yday
        return f"⧗-{year}.{day_of_year:03d}"
    
    @staticmethod
    def get_gregorian_time() -> str:
        """Get Gregorian timestamp"""
        return datetime.now().isoformat() + "Z"


class OutReporter:
    """Generates 0UT.3OX reports for station integration"""
    
    def __init__(self, station_root: str = ".3ox"):
        self.station_root = Path(station_root)
        self.out_directory = self.station_root / "OPS" / "0UT.3OX"
        self._ensure_out_directory()
    
    def _ensure_out_directory(self):
        """Create 0UT.3OX directory if it doesn't exist"""
        self.out_directory.mkdir(parents=True, exist_ok=True)
    
    def generate_job_report(self, job_id: str, result_data: Dict[str, Any], 
                          files_touched: List[str] = None) -> str:
        """Generate 0UT.3OX report for completed job"""
        
        report = OutReport(
            header={
                "stratos": "STRATOS-1",
                "station": "RVNx.BASE",
                "timestamp": SiriusCalendar.get_sirius_time(),
                "type": "status"
            },
            payload={
                "job_id": job_id,
                "result": "completed",
                "files_touched": files_touched or [],
                "summary": self._generate_summary(result_data),
                "execution_time": result_data.get("execution_time", 0),
                "offline": result_data.get("offline", True),
                "connector_used": result_data.get("connector_used"),
                "cost_estimate": result_data.get("cost_estimate")
            },
            routing={
                "priority": self._determine_priority(result_data),
                "destination": "CMD.BRIDGE"
            }
        )
        
        # Write report to file
        report_file = self.out_directory / f"{job_id}.out.3ox"
        with open(report_file, 'w') as f:
            yaml.dump(report.dict(), f, default_flow_style=False, sort_keys=False)
        
        return str(report_file)
    
    def generate_incident_report(self, job_id: str, error_message: str, 
                               severity: str = "medium") -> str:
        """Generate incident report for failed job"""
        
        report = OutReport(
            header={
                "stratos": "STRATOS-1",
                "station": "RVNx.BASE",
                "timestamp": SiriusCalendar.get_sirius_time(),
                "type": "incident"
            },
            payload={
                "job_id": job_id,
                "result": "failed",
                "error_message": error_message,
                "severity": severity,
                "summary": f"Job {job_id} failed: {error_message}"
            },
            routing={
                "priority": "high" if severity == "critical" else "normal",
                "destination": "CMD.BRIDGE"
            }
        )
        
        # Write report to file
        report_file = self.out_directory / f"{job_id}.incident.out.3ox"
        with open(report_file, 'w') as f:
            yaml.dump(report.dict(), f, default_flow_style=False, sort_keys=False)
        
        return str(report_file)
    
    def generate_change_report(self, job_id: str, changes: Dict[str, Any]) -> str:
        """Generate change report for operational modifications"""
        
        report = OutReport(
            header={
                "stratos": "STRATOS-1",
                "station": "RVNx.BASE",
                "timestamp": SiriusCalendar.get_sirius_time(),
                "type": "change"
            },
            payload={
                "job_id": job_id,
                "result": "change_detected",
                "changes": changes,
                "summary": f"Operational changes detected in job {job_id}",
                "files_modified": changes.get("files_modified", []),
                "config_changes": changes.get("config_changes", [])
            },
            routing={
                "priority": "high",
                "destination": "CMD.BRIDGE"
            }
        )
        
        # Write report to file
        report_file = self.out_directory / f"{job_id}.change.out.3ox"
        with open(report_file, 'w') as f:
            yaml.dump(report.dict(), f, default_flow_style=False, sort_keys=False)
        
        return str(report_file)
    
    def _generate_summary(self, result_data: Dict[str, Any]) -> str:
        """Generate human-readable summary from result data"""
        action = result_data.get("action", "process")
        files_processed = result_data.get("files_processed", 0)
        
        if action == "organize":
            categories = result_data.get("categories", {})
            total_files = sum(len(files) for files in categories.values())
            return f"Organized {total_files} files into {len(categories)} categories"
        
        elif action == "summarize":
            summaries = result_data.get("summaries", [])
            return f"Summarized {len(summaries)} documents"
        
        elif action == "clean":
            cleaned_files = result_data.get("cleaned_files", [])
            return f"Cleaned {len(cleaned_files)} temporary files"
        
        elif action == "duplicate":
            duplicates = result_data.get("duplicates", [])
            return f"Found {len(duplicates)} duplicate files"
        
        else:
            return f"Processed {files_processed} items using {action}"
    
    def _determine_priority(self, result_data: Dict[str, Any]) -> str:
        """Determine report priority based on result data"""
        files_touched = len(result_data.get("files_touched", []))
        cost_estimate = result_data.get("cost_estimate", 0)
        
        if files_touched > 100 or cost_estimate > 0.50:
            return "high"
        elif files_touched > 10 or cost_estimate > 0.10:
            return "medium"
        else:
            return "normal"
    
    def list_reports(self) -> List[Dict[str, Any]]:
        """List all 0UT.3OX reports"""
        reports = []
        
        for report_file in self.out_directory.glob("*.out.3ox"):
            try:
                with open(report_file, 'r') as f:
                    report_data = yaml.safe_load(f)
                
                reports.append({
                    "file": report_file.name,
                    "job_id": report_data.get("payload", {}).get("job_id"),
                    "type": report_data.get("header", {}).get("type"),
                    "timestamp": report_data.get("header", {}).get("timestamp"),
                    "priority": report_data.get("routing", {}).get("priority")
                })
            except Exception as e:
                print(f"Error reading report {report_file}: {e}")
        
        return sorted(reports, key=lambda x: x["timestamp"], reverse=True)
    
    def cleanup_old_reports(self, days: int = 30):
        """Clean up reports older than specified days"""
        cutoff_date = datetime.now().timestamp() - (days * 24 * 60 * 60)
        
        for report_file in self.out_directory.glob("*.out.3ox"):
            if report_file.stat().st_mtime < cutoff_date:
                report_file.unlink()
                print(f"Cleaned up old report: {report_file.name}")