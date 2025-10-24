"""
Offline Executor Service
Handles local execution of jobs without external API calls
"""

import os
import subprocess
import shutil
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime

from ..models.job_models import JobResult
from ...shared.schemas.job_packet import JobPacket


class OfflineExecutor:
    """Executes jobs using local tools and models"""
    
    def __init__(self):
        self.local_model_capacity = 2048  # tokens
        self.supported_actions = {
            'organize': self._organize_files,
            'summarize': self._summarize_text,
            'extract': self._extract_data,
            'clean': self._clean_files,
            'backup': self._backup_files,
            'audit': self._audit_files,
            'duplicate': self._find_duplicates
        }
    
    async def execute_job(self, job_packet: JobPacket) -> JobResult:
        """Execute job using offline methods"""
        start_time = datetime.now()
        
        try:
            # Determine action from prompt
            action = self._extract_action(job_packet.prompt)
            
            if action not in self.supported_actions:
                return JobResult(
                    job_id=job_packet.id,
                    status="FAILED",
                    error_message=f"Unsupported action: {action}",
                    offline=True
                )
            
            # Execute action
            result_data = await self.supported_actions[action](job_packet)
            
            execution_time = (datetime.now() - start_time).total_seconds()
            
            return JobResult(
                job_id=job_packet.id,
                status="SUCCESS",
                result_data=result_data,
                execution_time=execution_time,
                offline=True
            )
            
        except Exception as e:
            execution_time = (datetime.now() - start_time).total_seconds()
            
            return JobResult(
                job_id=job_packet.id,
                status="FAILED",
                error_message=str(e),
                execution_time=execution_time,
                offline=True
            )
    
    def _extract_action(self, prompt: str) -> str:
        """Extract action verb from prompt"""
        prompt_lower = prompt.lower()
        
        for action in self.supported_actions.keys():
            if action in prompt_lower:
                return action
        
        return 'organize'  # default action
    
    async def _organize_files(self, job_packet: JobPacket) -> Dict[str, Any]:
        """Organize files by date, type, or other criteria"""
        targets = job_packet.targets or [str(Path.home())]
        results = []
        
        for target_path in targets:
            target = Path(target_path).expanduser()
            
            if not target.exists():
                continue
            
            if target.is_file():
                # Organize single file
                organized = self._organize_single_file(target)
                results.append(organized)
            else:
                # Organize directory
                organized = await self._organize_directory(target)
                results.append(organized)
        
        return {
            "action": "organize",
            "results": results,
            "files_processed": sum(len(r.get("files", [])) for r in results)
        }
    
    def _organize_single_file(self, file_path: Path) -> Dict[str, Any]:
        """Organize a single file"""
        # Simple organization by extension
        extension = file_path.suffix.lower()
        category = self._get_file_category(extension)
        
        return {
            "file": str(file_path),
            "category": category,
            "extension": extension,
            "size": file_path.stat().st_size
        }
    
    async def _organize_directory(self, dir_path: Path) -> Dict[str, Any]:
        """Organize files in a directory"""
        files_by_category = {}
        total_files = 0
        
        for file_path in dir_path.rglob('*'):
            if file_path.is_file():
                total_files += 1
                extension = file_path.suffix.lower()
                category = self._get_file_category(extension)
                
                if category not in files_by_category:
                    files_by_category[category] = []
                
                files_by_category[category].append({
                    "path": str(file_path),
                    "size": file_path.stat().st_size,
                    "modified": datetime.fromtimestamp(file_path.stat().st_mtime).isoformat()
                })
        
        return {
            "directory": str(dir_path),
            "total_files": total_files,
            "categories": files_by_category
        }
    
    def _get_file_category(self, extension: str) -> str:
        """Categorize file by extension"""
        categories = {
            '.jpg': 'images', '.jpeg': 'images', '.png': 'images', '.gif': 'images',
            '.mp4': 'videos', '.avi': 'videos', '.mov': 'videos',
            '.mp3': 'audio', '.wav': 'audio', '.flac': 'audio',
            '.pdf': 'documents', '.doc': 'documents', '.docx': 'documents',
            '.txt': 'text', '.md': 'text',
            '.zip': 'archives', '.rar': 'archives', '.7z': 'archives'
        }
        
        return categories.get(extension, 'other')
    
    async def _summarize_text(self, job_packet: JobPacket) -> Dict[str, Any]:
        """Summarize text files or content"""
        targets = job_packet.targets or []
        summaries = []
        
        for target_path in targets:
            target = Path(target_path).expanduser()
            
            if target.is_file() and target.suffix.lower() in ['.txt', '.md', '.py', '.js']:
                try:
                    with open(target, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Simple summarization (first 3 lines + word count)
                    lines = content.split('\n')
                    summary = {
                        "file": str(target),
                        "word_count": len(content.split()),
                        "line_count": len(lines),
                        "preview": lines[:3],
                        "size": target.stat().st_size
                    }
                    summaries.append(summary)
                    
                except Exception as e:
                    summaries.append({
                        "file": str(target),
                        "error": str(e)
                    })
        
        return {
            "action": "summarize",
            "summaries": summaries
        }
    
    async def _extract_data(self, job_packet: JobPacket) -> Dict[str, Any]:
        """Extract data from files"""
        # Placeholder for data extraction
        return {
            "action": "extract",
            "message": "Data extraction not yet implemented",
            "targets": job_packet.targets
        }
    
    async def _clean_files(self, job_packet: JobPacket) -> Dict[str, Any]:
        """Clean temporary files and organize"""
        targets = job_packet.targets or [str(Path.home() / "Downloads")]
        cleaned_files = []
        
        for target_path in targets:
            target = Path(target_path).expanduser()
            
            if target.is_dir():
                # Clean common temp files
                temp_patterns = ['*.tmp', '*.temp', '~*', '*.log']
                
                for pattern in temp_patterns:
                    for temp_file in target.rglob(pattern):
                        try:
                            temp_file.unlink()
                            cleaned_files.append(str(temp_file))
                        except Exception:
                            pass
        
        return {
            "action": "clean",
            "cleaned_files": cleaned_files,
            "count": len(cleaned_files)
        }
    
    async def _backup_files(self, job_packet: JobPacket) -> Dict[str, Any]:
        """Create backup of files"""
        # Placeholder for backup functionality
        return {
            "action": "backup",
            "message": "Backup functionality not yet implemented",
            "targets": job_packet.targets
        }
    
    async def _audit_files(self, job_packet: JobPacket) -> Dict[str, Any]:
        """Audit files for issues"""
        targets = job_packet.targets or []
        audit_results = []
        
        for target_path in targets:
            target = Path(target_path).expanduser()
            
            if target.exists():
                audit_result = {
                    "path": str(target),
                    "exists": True,
                    "size": target.stat().st_size if target.is_file() else None,
                    "permissions": oct(target.stat().st_mode)[-3:],
                    "modified": datetime.fromtimestamp(target.stat().st_mtime).isoformat()
                }
                audit_results.append(audit_result)
            else:
                audit_results.append({
                    "path": str(target),
                    "exists": False
                })
        
        return {
            "action": "audit",
            "results": audit_results
        }
    
    async def _find_duplicates(self, job_packet: JobPacket) -> Dict[str, Any]:
        """Find duplicate files"""
        targets = job_packet.targets or []
        duplicates = []
        
        for target_path in targets:
            target = Path(target_path).expanduser()
            
            if target.is_dir():
                # Simple duplicate detection by size and name
                file_sizes = {}
                
                for file_path in target.rglob('*'):
                    if file_path.is_file():
                        size = file_path.stat().st_size
                        name = file_path.name
                        key = f"{size}_{name}"
                        
                        if key in file_sizes:
                            duplicates.append({
                                "file1": str(file_sizes[key]),
                                "file2": str(file_path),
                                "size": size
                            })
                        else:
                            file_sizes[key] = file_path
        
        return {
            "action": "duplicate",
            "duplicates": duplicates,
            "count": len(duplicates)
        }