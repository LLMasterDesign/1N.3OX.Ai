#!/usr/bin/env python3
"""
Validation script to check if all components can be imported
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

def validate_imports():
    """Validate that all modules can be imported"""
    print("▛▞ Validating Website Monitoring Agent Installation")
    print("="*60)
    
    errors = []
    
    # Test core modules
    tests = [
        ("WebsiteMonitor", "from monitors.website_monitor import WebsiteMonitor"),
        ("PerformanceTracker", "from monitors.performance_tracker import PerformanceTracker"),
        ("TelegramWebhook", "from integrations.telegram_webhook import TelegramWebhook"),
        ("AlertSystem", "from integrations.alert_system import AlertSystem"),
        ("Logging Utils", "from utils.logging import setup_logging, get_logger"),
        ("Error Handler", "from utils.error_handler import ErrorHandler, async_error_handler"),
    ]
    
    for name, import_statement in tests:
        try:
            exec(import_statement)
            print(f"✓ {name:.<50} OK")
        except Exception as e:
            print(f"✗ {name:.<50} FAILED")
            errors.append((name, str(e)))
    
    # Test dependencies
    print("\n" + "="*60)
    print("Checking dependencies...")
    print("="*60)
    
    deps = [
        ("aiohttp", "import aiohttp"),
        ("yaml", "import yaml"),
        ("telegram", "from telegram import Bot"),
        ("prometheus_client", "from prometheus_client import Gauge"),
        ("pytest", "import pytest"),
    ]
    
    for name, import_statement in deps:
        try:
            exec(import_statement)
            print(f"✓ {name:.<50} OK")
        except Exception as e:
            print(f"✗ {name:.<50} FAILED")
            errors.append((name, str(e)))
    
    # Results
    print("\n" + "="*60)
    if errors:
        print("❌ Validation FAILED")
        print("="*60)
        print("\nErrors found:")
        for name, error in errors:
            print(f"\n{name}:")
            print(f"  {error}")
        print("\nPlease run: pip install -r requirements.txt")
        return False
    else:
        print("✅ All validations PASSED")
        print("="*60)
        print("\nSystem is ready to run!")
        print("Next steps:")
        print("1. Configure src/config.yaml")
        print("2. Run examples: python example_usage.py")
        print("3. Start monitoring: python src/main.py")
        print("\n:: ∎")
        return True


if __name__ == "__main__":
    success = validate_imports()
    sys.exit(0 if success else 1)
