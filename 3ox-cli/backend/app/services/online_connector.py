"""
Online Connector Service
Handles external API calls and online resource access
Based on chatlog specifications for online/offline routing
"""

import httpx
import json
from typing import Dict, Any, Optional
from datetime import datetime

from ..models.job_models import JobResult
from ...shared.schemas.job_packet import JobPacket


class OnlineConnector:
    """Manages online API calls and external resource access"""
    
    def __init__(self):
        self.connectors = {
            'openai': self._call_openai,
            'anthropic': self._call_anthropic,
            'web_search': self._call_web_search,
            'email': self._call_email,
            'slack': self._call_slack
        }
        
        self.cost_limits = {
            'daily': 2.0,  # $2 per day default
            'per_job': 0.50  # $0.50 per job default
        }
        
        self.model_whitelist = [
            'gpt-3.5-turbo',
            'gpt-4',
            'claude-3-haiku',
            'claude-3-sonnet'
        ]
    
    async def execute_job(self, job_packet: JobPacket) -> JobResult:
        """Execute job using online connectors"""
        start_time = datetime.now()
        
        try:
            # Determine which connector to use
            connector = self._select_connector(job_packet)
            
            if not connector:
                return JobResult(
                    job_id=job_packet.id,
                    status="FAILED",
                    error_message="No suitable online connector available",
                    offline=False
                )
            
            # Check cost limits
            if not self._check_cost_limits(job_packet):
                return JobResult(
                    job_id=job_packet.id,
                    status="FAILED",
                    error_message="Cost limit exceeded",
                    offline=False
                )
            
            # Execute with selected connector
            result_data = await self.connectors[connector](job_packet)
            
            execution_time = (datetime.now() - start_time).total_seconds()
            
            return JobResult(
                job_id=job_packet.id,
                status="SUCCESS",
                result_data=result_data,
                execution_time=execution_time,
                offline=False,
                connector_used=connector,
                cost_estimate=self._estimate_cost(job_packet, connector)
            )
            
        except Exception as e:
            execution_time = (datetime.now() - start_time).total_seconds()
            
            return JobResult(
                job_id=job_packet.id,
                status="FAILED",
                error_message=str(e),
                execution_time=execution_time,
                offline=False
            )
    
    def _select_connector(self, job_packet: JobPacket) -> Optional[str]:
        """Select appropriate connector based on job requirements"""
        prompt_lower = job_packet.prompt.lower()
        
        # Check for specific connector requirements
        if any(keyword in prompt_lower for keyword in ['search', 'web', 'google']):
            return 'web_search'
        elif any(keyword in prompt_lower for keyword in ['email', 'send mail']):
            return 'email'
        elif any(keyword in prompt_lower for keyword in ['slack', 'message', 'notify']):
            return 'slack'
        elif any(keyword in prompt_lower for keyword in ['analyze', 'summarize', 'explain']):
            return 'openai'  # Default to OpenAI for analysis
        else:
            return 'openai'  # Default fallback
    
    def _check_cost_limits(self, job_packet: JobPacket) -> bool:
        """Check if job is within cost limits"""
        # In a real implementation, this would check:
        # 1. Daily spending against cost_limits['daily']
        # 2. Per-job cost against cost_limits['per_job']
        # 3. User's remaining budget
        
        # For now, always allow (placeholder)
        return True
    
    def _estimate_cost(self, job_packet: JobPacket, connector: str) -> float:
        """Estimate cost for job execution"""
        # Rough cost estimation based on prompt length and connector
        base_cost = 0.01  # $0.01 base cost
        
        # Add cost based on prompt length (rough token estimation)
        prompt_tokens = len(job_packet.prompt.split()) * 1.3  # Rough token count
        token_cost = prompt_tokens * 0.0001  # $0.0001 per token
        
        # Connector-specific multipliers
        multipliers = {
            'openai': 1.0,
            'anthropic': 1.2,
            'web_search': 0.5,
            'email': 0.1,
            'slack': 0.1
        }
        
        multiplier = multipliers.get(connector, 1.0)
        
        return (base_cost + token_cost) * multiplier
    
    async def _call_openai(self, job_packet: JobPacket) -> Dict[str, Any]:
        """Call OpenAI API (placeholder implementation)"""
        # In a real implementation, this would:
        # 1. Set up OpenAI client with API key
        # 2. Format prompt according to job requirements
        # 3. Make API call with appropriate model
        # 4. Process and return response
        
        return {
            "connector": "openai",
            "model": "gpt-3.5-turbo",
            "response": f"OpenAI analysis of: {job_packet.prompt}",
            "tokens_used": len(job_packet.prompt.split()) * 1.3,
            "cost": 0.05
        }
    
    async def _call_anthropic(self, job_packet: JobPacket) -> Dict[str, Any]:
        """Call Anthropic API (placeholder implementation)"""
        return {
            "connector": "anthropic",
            "model": "claude-3-haiku",
            "response": f"Anthropic analysis of: {job_packet.prompt}",
            "tokens_used": len(job_packet.prompt.split()) * 1.3,
            "cost": 0.06
        }
    
    async def _call_web_search(self, job_packet: JobPacket) -> Dict[str, Any]:
        """Call web search API (placeholder implementation)"""
        return {
            "connector": "web_search",
            "query": job_packet.prompt,
            "results": [
                {
                    "title": "Sample Search Result",
                    "url": "https://example.com",
                    "snippet": "This is a sample search result..."
                }
            ],
            "cost": 0.01
        }
    
    async def _call_email(self, job_packet: JobPacket) -> Dict[str, Any]:
        """Send email (placeholder implementation)"""
        return {
            "connector": "email",
            "action": "sent",
            "recipient": "extracted_from_prompt",
            "subject": "3OX Command Result",
            "cost": 0.001
        }
    
    async def _call_slack(self, job_packet: JobPacket) -> Dict[str, Any]:
        """Send Slack message (placeholder implementation)"""
        return {
            "connector": "slack",
            "action": "sent",
            "channel": "extracted_from_prompt",
            "message": f"3OX Command: {job_packet.prompt}",
            "cost": 0.001
        }
    
    def get_connector_status(self) -> Dict[str, Any]:
        """Get status of all connectors"""
        return {
            "connectors": list(self.connectors.keys()),
            "cost_limits": self.cost_limits,
            "model_whitelist": self.model_whitelist,
            "daily_spent": 0.0,  # Would track actual spending
            "remaining_budget": self.cost_limits['daily']
        }