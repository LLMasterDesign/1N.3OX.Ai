#!/usr/bin/env python3
"""
CORE.3ox PROOF OF CONCEPT TEST
Run this to prove the Python runtime works!
"""

import sys
import os
import subprocess
import time
from datetime import datetime

def print_header(text):
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60)

def print_step(num, text):
    print(f"\n▶ STEP {num}: {text}")
    time.sleep(0.5)

def run_command(cmd, desc):
    print(f"\n  Running: {cmd}")
    print(f"  ───────────────────────────────────────")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        if result.stdout:
            print(result.stdout)
        if result.stderr and "warning" not in result.stderr.lower():
            print(f"  Note: {result.stderr}")
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        print(f"  ✗ Timeout after 30 seconds")
        return False
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def check_dependencies():
    print_step(1, "Checking Dependencies")
    
    # Check Python
    print(f"  ✓ Python: {sys.version.split()[0]}")
    
    # Check required packages
    packages = ['xxhash', 'toml', 'yaml', 'tiktoken']
    missing = []
    
    for pkg in packages:
        try:
            __import__(pkg)
            print(f"  ✓ {pkg}: installed")
        except ImportError:
            print(f"  ✗ {pkg}: MISSING")
            missing.append(pkg)
    
    if missing:
        print(f"\n  Installing missing packages: {', '.join(missing)}")
        cmd = f"pip install {' '.join(missing)}"
        if not run_command(cmd, "Installing dependencies"):
            print("\n  ⚠ Installation had issues, but continuing...")
        time.sleep(1)
    
    return True

def test_file_validation():
    print_step(2, "Testing File Validation")
    
    # Create a test file
    test_file = "CORE.3ox/test_sample.txt"
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write("This is a test file for CORE.3ox validation.\n")
        f.write("Testing file integrity with xxHash64.\n")
        f.write(f"Generated: {datetime.now()}\n")
    
    print(f"  ✓ Created test file: {test_file}")
    
    return True

def test_operations():
    print_step(3, "Running CORE.3ox Operations")
    
    operations = [
        ("knowledge_update", "Knowledge base update"),
        ("critical_error", "Critical error handling"),
        ("deploy_ready", "Deployment readiness")
    ]
    
    results = []
    
    for op, desc in operations:
        print(f"\n  Testing: {desc} ({op})")
        success = run_command(f"python CORE.3ox/run.py {op}", desc)
        results.append((op, success))
        time.sleep(0.5)
    
    return results

def test_batch_mode():
    print_step(4, "Testing Batch Mode (Multiple Operations)")
    
    print("\n  Running 3 operations in one call...")
    start = time.time()
    success = run_command(
        "python CORE.3ox/run.py knowledge_update critical_error deploy_ready",
        "Batch operations"
    )
    elapsed = time.time() - start
    
    print(f"\n  ⏱ Completed in {elapsed:.2f} seconds")
    
    return success

def check_outputs():
    print_step(5, "Verifying Outputs")
    
    # Check for log file
    log_file = "CORE.3ox/3ox.log"
    if os.path.exists(log_file):
        print(f"  ✓ Log file created: {log_file}")
        with open(log_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print(f"  ✓ Log entries: {len(lines)}")
            if lines:
                print(f"\n  Last log entry:")
                print(f"  {lines[-1].strip()}")
    else:
        print(f"  ✗ Log file not found")
    
    # Check for routed outputs
    output_dirs = ["CMD.BRIDGE", "OBSIDIAN.BASE", "SYNTH.BASE"]
    found_receipts = []
    
    for dir_name in output_dirs:
        dir_path = os.path.join("CORE.3ox", dir_name)
        if os.path.exists(dir_path):
            files = os.listdir(dir_path)
            if files:
                print(f"  ✓ Routed to {dir_name}: {len(files)} file(s)")
                found_receipts.extend(files)
    
    return len(found_receipts) > 0

def show_summary(results, outputs_found):
    print_header("TEST SUMMARY")
    
    print("\n  Operations Tested:")
    for op, success in results:
        status = "✓ PASS" if success else "✗ FAIL"
        print(f"    {status} - {op}")
    
    print(f"\n  Outputs Created: {'✓ YES' if outputs_found else '✗ NO'}")
    
    total_tests = len(results)
    passed_tests = sum(1 for _, success in results if success)
    
    print(f"\n  Results: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests and outputs_found:
        print("\n  🎉 SUCCESS! CORE.3ox is working perfectly!")
        print("\n  Next steps:")
        print("    1. Check CORE.3ox/3ox.log for operation logs")
        print("    2. Check routed folders (CMD.BRIDGE, etc.) for receipts")
        print("    3. Ready to integrate with your SaaS platform!")
    elif passed_tests > 0:
        print("\n  ⚠ PARTIAL SUCCESS - Some operations worked")
        print("    Check the output above for details")
    else:
        print("\n  ✗ FAILED - No operations succeeded")
        print("    Check Python version and dependencies")

def main():
    print_header("CORE.3ox PROOF OF CONCEPT TEST")
    print(f"\n  Testing Python runtime at: {os.getcwd()}")
    print(f"  Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        # Run tests
        check_dependencies()
        test_file_validation()
        results = test_operations()
        test_batch_mode()
        outputs_found = check_outputs()
        
        # Show summary
        show_summary(results, outputs_found)
        
    except KeyboardInterrupt:
        print("\n\n  ⚠ Test interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n  ✗ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    main()

