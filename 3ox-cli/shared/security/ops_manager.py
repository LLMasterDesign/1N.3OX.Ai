"""
OPS (Operational Authority) Security Manager
Handles OPS tokens, 2FA gating, and protected operations
Based on chatlog security specifications
"""

import os
import json
import hashlib
import secrets
from pathlib import Path
from typing import Optional, Dict, Any, Tuple
from datetime import datetime, timedelta


class OPSToken:
    """OPS token structure"""
    def __init__(self, token_id: str, created_at: str, expires_at: str, 
                 permissions: list, signature: str):
        self.token_id = token_id
        self.created_at = created_at
        self.expires_at = expires_at
        self.permissions = permissions
        self.signature = signature
    
    def is_valid(self) -> bool:
        """Check if token is still valid"""
        now = datetime.now()
        expires = datetime.fromisoformat(self.expires_at)
        return now < expires
    
    def has_permission(self, permission: str) -> bool:
        """Check if token has specific permission"""
        return permission in self.permissions or "ALL" in self.permissions


class OPSManager:
    """Manages OPS security and 2FA gating"""
    
    def __init__(self, ops_path: str = ".3ox/ops"):
        self.ops_path = Path(ops_path)
        self.tokens_file = self.ops_path / "tokens.json"
        self.policy_file = self.ops_path / "policy.json"
        self._ensure_ops_directory()
    
    def _ensure_ops_directory(self):
        """Create OPS directory structure if it doesn't exist"""
        self.ops_path.mkdir(parents=True, exist_ok=True)
        
        # Initialize tokens file if it doesn't exist
        if not self.tokens_file.exists():
            self._initialize_tokens()
        
        # Initialize policy file if it doesn't exist
        if not self.policy_file.exists():
            self._initialize_policy()
    
    def _initialize_tokens(self):
        """Initialize empty tokens file"""
        with open(self.tokens_file, 'w') as f:
            json.dump({"tokens": {}}, f, indent=2)
    
    def _initialize_policy(self):
        """Initialize default OPS policy"""
        policy = {
            "ops_required_actions": [
                "modify .3ox files",
                "deploy to R:/3OX.Ai", 
                "change POLICY/*",
                "modify OPS tokens",
                "change security settings"
            ],
            "sensitive_paths": [
                "~/Private",
                "~/Vault", 
                "~/Downloads/Encrypted",
                "~/.3ox/secure_uploads"
            ],
            "2fa_required": True,
            "token_expiry_hours": 24,
            "max_retry_attempts": 3
        }
        
        with open(self.policy_file, 'w') as f:
            json.dump(policy, f, indent=2)
    
    def generate_ops_token(self, permissions: list, expiry_hours: int = 24) -> str:
        """Generate new OPS token"""
        token_id = secrets.token_urlsafe(32)
        created_at = datetime.now().isoformat()
        expires_at = (datetime.now() + timedelta(hours=expiry_hours)).isoformat()
        
        # Create signature
        signature_data = f"{token_id}:{created_at}:{expires_at}:{':'.join(permissions)}"
        signature = hashlib.sha256(signature_data.encode()).hexdigest()
        
        token = OPSToken(token_id, created_at, expires_at, permissions, signature)
        
        # Store token
        self._store_token(token)
        
        return token_id
    
    def _store_token(self, token: OPSToken):
        """Store OPS token in tokens file"""
        tokens_data = self._load_tokens()
        tokens_data["tokens"][token.token_id] = {
            "created_at": token.created_at,
            "expires_at": token.expires_at,
            "permissions": token.permissions,
            "signature": token.signature
        }
        
        with open(self.tokens_file, 'w') as f:
            json.dump(tokens_data, f, indent=2)
    
    def _load_tokens(self) -> Dict[str, Any]:
        """Load tokens from file"""
        try:
            with open(self.tokens_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"tokens": {}}
    
    def validate_ops_token(self, token_id: str) -> Tuple[bool, Optional[OPSToken]]:
        """Validate OPS token and return token object if valid"""
        tokens_data = self._load_tokens()
        
        if token_id not in tokens_data["tokens"]:
            return False, None
        
        token_data = tokens_data["tokens"][token_id]
        token = OPSToken(
            token_id,
            token_data["created_at"],
            token_data["expires_at"],
            token_data["permissions"],
            token_data["signature"]
        )
        
        if not token.is_valid():
            return False, None
        
        return True, token
    
    def check_ops_required(self, action: str, targets: list) -> bool:
        """Check if action requires OPS authorization"""
        policy = self._load_policy()
        ops_required_actions = policy.get("ops_required_actions", [])
        
        # Check if action matches any OPS-required patterns
        for required_action in ops_required_actions:
            if required_action.lower() in action.lower():
                return True
        
        # Check if targets contain protected paths
        sensitive_paths = policy.get("sensitive_paths", [])
        for target in targets:
            for sensitive_path in sensitive_paths:
                if sensitive_path in target:
                    return True
        
        return False
    
    def _load_policy(self) -> Dict[str, Any]:
        """Load OPS policy from file"""
        try:
            with open(self.policy_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def require_2fa_confirmation(self, action: str, targets: list) -> bool:
        """Check if action requires 2FA confirmation"""
        policy = self._load_policy()
        
        if not policy.get("2fa_required", True):
            return False
        
        return self.check_ops_required(action, targets)
    
    def is_sensitive_path(self, path: str) -> bool:
        """Check if path is marked as sensitive"""
        policy = self._load_policy()
        sensitive_paths = policy.get("sensitive_paths", [])
        
        for sensitive_path in sensitive_paths:
            if sensitive_path in path:
                return True
        
        return False
    
    def redact_sensitive_data(self, data: str) -> Tuple[str, Dict[str, Any]]:
        """Redact sensitive data and return redacted content + log"""
        redaction_log = {
            "redacted_patterns": [],
            "line_numbers": [],
            "timestamp": datetime.now().isoformat()
        }
        
        # Common PII patterns
        patterns = {
            "email": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            "ssn": r'\b\d{3}-\d{2}-\d{4}\b',
            "credit_card": r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b',
            "phone": r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
        }
        
        redacted_data = data
        
        for pattern_name, pattern in patterns.items():
            matches = re.finditer(pattern, data, re.IGNORECASE)
            for match in matches:
                redacted_data = redacted_data.replace(match.group(), "[REDACTED]")
                redaction_log["redacted_patterns"].append({
                    "pattern": pattern_name,
                    "original": match.group(),
                    "position": match.span()
                })
        
        return redacted_data, redaction_log