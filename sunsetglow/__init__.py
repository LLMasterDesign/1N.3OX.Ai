"""
Sunsetglow - Street Banner Research & Design Agent

A comprehensive multi-stage AI agent system for street banner market research
and conceptual design generation.

Modules:
    - banner_cost_research: Vendor pricing research and analysis
    - banner_design: Print-ready banner design generation
    - banner_preview: Mockup visualization and export
    - agent: Main orchestrator for complete workflow
"""

__version__ = "1.0.0"
__author__ = "Cursor AI Agent"
__description__ = "Street Banner Research & Design Agent"

from .banner_cost_research import BannerCostResearch
from .banner_design import SunsetGlowDesigner
from .banner_preview import BannerPreview
from .agent import BannerAgent

__all__ = [
    'BannerCostResearch',
    'SunsetGlowDesigner',
    'BannerPreview',
    'BannerAgent',
]
