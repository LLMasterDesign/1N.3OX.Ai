"""
LLMD (Lucius Language Markup Data) Validator and v8sl Header Injection
Based on the chatlog specifications for 3OX formatting standards
"""

import re
from datetime import datetime
from typing import Dict, Any, Optional


class SiriusTime:
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


class LLMDValidator:
    """Validates and injects LLMD/v8sl headers into job packets"""
    
    @staticmethod
    def inject_v8sl_header(job_data: Dict[str, Any]) -> str:
        """Inject v8sl header into job packet"""
        sirius_time = SiriusTime.get_sirius_time()
        job_id = job_data.get('id', 'unknown')
        role = job_data.get('role', '@MASTER')
        mode = job_data.get('mode', '!ANALYTICAL')
        
        # Extract action from prompt (simplified)
        prompt = job_data.get('prompt', '')
        action = LLMDValidator._extract_action(prompt)
        
        header = f"""▛//▞▞ ⟦⎊⟧ :: {sirius_time} // JOB.{action.upper()} ▞▞
▞//▞ ρ{{{role}}}.φ{{LOCAL}}.τ{{{job_id}}}.λ{{oneoff}} ⫸
▙⌱[📁] ≔ [⊢{{input}}⇨{{route}}⟿{{execute}}▷{{receipt}}]
:: ∎"""
        
        return header
    
    @staticmethod
    def _extract_action(prompt: str) -> str:
        """Extract action verb from prompt"""
        action_verbs = [
            'organize', 'summarize', 'extract', 'secure-delete', 
            'backup', 'audit', 'heal-sync', 'actuate', 'clean',
            'analyze', 'process', 'transform', 'sync'
        ]
        
        prompt_lower = prompt.lower()
        for verb in action_verbs:
            if verb in prompt_lower:
                return verb.replace('-', '_')
        
        return 'PROCESS'
    
    @staticmethod
    def validate_llmd_format(content: str) -> bool:
        """Validate LLMD format compliance"""
        # Check for required LLMD markers
        required_markers = ['▛//▞▞', '⟦⎊⟧', '::', '▞▞', ':: ∎']
        
        for marker in required_markers:
            if marker not in content:
                return False
        
        return True
    
    @staticmethod
    def format_job_with_llmd(job_data: Dict[str, Any]) -> str:
        """Format job packet with LLMD headers"""
        header = LLMDValidator.inject_v8sl_header(job_data)
        
        # Create formatted job content
        formatted_job = f"""{header}

JOB_PACKET:
{{
  "id": "{job_data.get('id', '')}",
  "created_at": "{job_data.get('created_at', '')}",
  "sirius_time": "{SiriusTime.get_sirius_time()}",
  "user": "{job_data.get('user', '')}",
  "role": "{job_data.get('role', '')}",
  "mode": "{job_data.get('mode', '')}",
  "prompt": "{job_data.get('prompt', '')}",
  "targets": {job_data.get('targets', [])},
  "sensitive": {str(job_data.get('sensitive', False)).lower()},
  "allow_online": {str(job_data.get('allow_online', False)).lower()},
  "ops_action": {str(job_data.get('ops_action', False)).lower()}
}}

:: ∎"""
        
        return formatted_job