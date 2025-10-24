"""
Routing Brain Service
Implements Master Routing Brain logic for agent selection
Based on chatlog specifications
"""

import os
from pathlib import Path
from typing import Optional, Dict, Any


class RoutingBrain:
    """Master Routing Brain for agent selection and context detection"""
    
    def __init__(self):
        self.role_mappings = {
            '@SENTINEL': 'security_monitoring',
            '@LIGHTHOUSE': 'guidance_navigation', 
            '@ALCHEMIST': 'data_transformation',
            '@BRIDGE': 'communication_coordination',
            '@MASTER': 'general_purpose'
        }
        
        self.project_indicators = [
            'PROJECT.BRAIN.md',
            '.3ox',
            'brain.rs',
            'agent_config.json'
        ]
        
        self.station_roots = [
            'RVNx.BASE',
            'SYNTH.BASE', 
            'OBSIDIAN.BASE'
        ]
    
    def detect_context(self, workspace: str, targets: list = None) -> Dict[str, Any]:
        """Detect workspace context and determine appropriate agent"""
        workspace_path = Path(workspace).expanduser().resolve()
        
        context = {
            'workspace': str(workspace_path),
            'agent_role': '@MASTER',  # Default fallback
            'context_type': 'general',
            'confidence': 0.0,
            'indicators': []
        }
        
        # Check for project brain files
        project_brain = self._find_project_brain(workspace_path)
        if project_brain:
            context['agent_role'] = self._extract_role_from_brain(project_brain)
            context['context_type'] = 'project'
            context['confidence'] = 0.9
            context['indicators'].append('project_brain')
            return context
        
        # Check for station roots
        station_context = self._detect_station_context(workspace_path)
        if station_context:
            context.update(station_context)
            return context
        
        # Check for .3ox files
        threeox_files = list(workspace_path.rglob('.3ox'))
        if threeox_files:
            context['agent_role'] = '@LIGHTHOUSE'
            context['context_type'] = 'threeox_project'
            context['confidence'] = 0.7
            context['indicators'].append('threeox_files')
            return context
        
        # Check for specific file patterns
        file_patterns = self._detect_file_patterns(workspace_path)
        if file_patterns:
            context['agent_role'] = self._map_patterns_to_role(file_patterns)
            context['context_type'] = 'pattern_based'
            context['confidence'] = 0.5
            context['indicators'].extend(file_patterns)
        
        return context
    
    def _find_project_brain(self, workspace_path: Path) -> Optional[Path]:
        """Find PROJECT.BRAIN.md file in workspace"""
        for indicator in self.project_indicators:
            brain_file = workspace_path / indicator
            if brain_file.exists():
                return brain_file
        
        # Check parent directories
        current = workspace_path.parent
        while current != current.parent:  # Not at root
            for indicator in self.project_indicators:
                brain_file = current / indicator
                if brain_file.exists():
                    return brain_file
            current = current.parent
        
        return None
    
    def _extract_role_from_brain(self, brain_file: Path) -> str:
        """Extract agent role from PROJECT.BRAIN.md"""
        try:
            with open(brain_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Look for role patterns
            for role in self.role_mappings.keys():
                if role in content:
                    return role
            
            # Look for role: pattern
            lines = content.split('\n')
            for line in lines:
                if 'role:' in line.lower():
                    role_part = line.split(':')[1].strip()
                    if role_part.startswith('@'):
                        return role_part
            
        except Exception:
            pass
        
        return '@MASTER'
    
    def _detect_station_context(self, workspace_path: Path) -> Optional[Dict[str, Any]]:
        """Detect if workspace is a station root"""
        workspace_name = workspace_path.name
        
        for station in self.station_roots:
            if station in workspace_name:
                return {
                    'agent_role': '@LIGHTHOUSE',
                    'context_type': 'station',
                    'confidence': 0.8,
                    'indicators': ['station_root'],
                    'station': station
                }
        
        return None
    
    def _detect_file_patterns(self, workspace_path: Path) -> list:
        """Detect file patterns that suggest specific agent roles"""
        patterns = []
        
        # Check for security-related files
        security_files = list(workspace_path.rglob('*security*')) + \
                        list(workspace_path.rglob('*auth*')) + \
                        list(workspace_path.rglob('*key*'))
        if security_files:
            patterns.append('security_files')
        
        # Check for data/analysis files
        data_files = list(workspace_path.rglob('*.csv')) + \
                    list(workspace_path.rglob('*.json')) + \
                    list(workspace_path.rglob('*.xlsx'))
        if data_files:
            patterns.append('data_files')
        
        # Check for documentation
        doc_files = list(workspace_path.rglob('*.md')) + \
                   list(workspace_path.rglob('*.rst')) + \
                   list(workspace_path.rglob('*.txt'))
        if doc_files:
            patterns.append('documentation')
        
        return patterns
    
    def _map_patterns_to_role(self, patterns: list) -> str:
        """Map detected patterns to appropriate agent role"""
        if 'security_files' in patterns:
            return '@SENTINEL'
        elif 'data_files' in patterns:
            return '@ALCHEMIST'
        elif 'documentation' in patterns:
            return '@LIGHTHOUSE'
        else:
            return '@MASTER'
    
    def get_agent_capabilities(self, role: str) -> Dict[str, Any]:
        """Get capabilities for specific agent role"""
        capabilities = {
            '@SENTINEL': {
                'description': 'Security monitoring and protection',
                'capabilities': ['security_audit', 'threat_detection', 'access_control'],
                'preferred_actions': ['audit', 'secure-delete', 'monitor']
            },
            '@LIGHTHOUSE': {
                'description': 'Guidance and navigation',
                'capabilities': ['summarization', 'organization', 'guidance'],
                'preferred_actions': ['summarize', 'organize', 'guide']
            },
            '@ALCHEMIST': {
                'description': 'Data transformation and analysis',
                'capabilities': ['data_processing', 'transformation', 'analysis'],
                'preferred_actions': ['extract', 'transform', 'analyze']
            },
            '@BRIDGE': {
                'description': 'Communication and coordination',
                'capabilities': ['communication', 'coordination', 'integration'],
                'preferred_actions': ['sync', 'coordinate', 'communicate']
            },
            '@MASTER': {
                'description': 'General purpose operations',
                'capabilities': ['general_ops', 'coordination', 'fallback'],
                'preferred_actions': ['organize', 'process', 'manage']
            }
        }
        
        return capabilities.get(role, capabilities['@MASTER'])