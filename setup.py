#!/usr/bin/env python3
"""
CAT.3OX SETUP - Create Your 6 Category System
Version: 1.0
"""

import os
from pathlib import Path
from datetime import datetime

# 5 Life domains + ADMIN
CATEGORIES = [
    {"num": "1", "name": "Self", "domain": "Personal development and health"},
    {"num": "2", "name": "Education", "domain": "Learning and knowledge"},
    {"num": "3", "name": "Business", "domain": "Work and professional"},
    {"num": "4", "name": "Family", "domain": "Family matters"},
    {"num": "5", "name": "Social", "domain": "Friends and community"},
    {"num": "0", "name": "ADMIN", "domain": "Master orchestration", "special": True}
]

def create_category(cat, install_path="."):
    folder_name = f"(CAT.{cat['num']}) {cat['name']}"
    full_path = Path(install_path) / folder_name
    
    print(f"\n  Creating: {folder_name}")
    
    # Create main folder
    full_path.mkdir(exist_ok=True)
    
    # Create .3ox folder
    dot_path = full_path / ".3ox"
    dot_path.mkdir(exist_ok=True)
    
    # Create 1N.3OX (inbox) - UNLESS it's ADMIN
    if not cat.get("special"):
        in_path = full_path / "1N.3OX"
        in_path.mkdir(exist_ok=True)
        
        # Create inbox README
        readme_content = f"""# (CAT.{cat['num']}) {cat['name']} - Inbox

**Domain:** {cat['domain']}

Drop files here → CAT.0 ADMIN orchestrates routing

Established: ⧗-25.291
"""
        (in_path / "README.md").write_text(readme_content, encoding='utf-8')
        print(f"    ✓ 1N.3OX/ (inbox)")
    else:
        print(f"    ✓ NO 1N.3OX (ADMIN has no external input)")
    
    # Create 0UT.3OX (inside .3ox)
    out_path = dot_path / "0UT.3OX"
    out_path.mkdir(exist_ok=True)
    print(f"    ✓ .3ox/0UT.3OX/ (receipts)")
    
    # Create category info
    brain_content = f"""# (CAT.{cat['num']}) {cat['name']} - Category Info

**Domain:** {cat['domain']}
**Status:** Active
**Created:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Purpose

This category organizes: {cat['domain']}

## Routing

{"Items arrive in: 1N.3OX/" if not cat.get("special") else "No external input (ADMIN only)"}
Processed by: .3ox/ runtime
Receipts sent to: 0UT.3OX/

## Master Connection

{"Orchestrated by: (CAT.0) ADMIN" if not cat.get("special") else "THIS IS THE MASTER - orchestrates all other categories"}

Established: ⧗-25.291
"""
    (dot_path / "cat.info").write_text(brain_content, encoding='utf-8')
    print(f"    ✓ cat.info")
    
    # Create 3ox.log
    log_content = f"""# (CAT.{cat['num']}) {cat['name']} - Activity Log
# Domain: {cat['domain']}
# Established: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Category created and ready for use.
"""
    (dot_path / "3ox.log").write_text(log_content, encoding='utf-8')
    print(f"    ✓ 3ox.log")

def install_runtime(cat_path, runtime_type):
    """Install CORE or RAW runtime into category"""
    import shutil
    
    runtime_source = Path(runtime_type.upper())
    if not runtime_source.exists():
        print(f"    ERROR: {runtime_type.upper()}/ runtime not found")
        return False
    
    dot_path = cat_path / ".3ox"
    
    # Copy all runtime files
    for item in runtime_source.glob("*"):
        dest = dot_path / item.name
        if item.is_file():
            shutil.copy2(item, dest)
    
    print(f"    ✓ {runtime_type.upper()} runtime installed")
    return True

def main():
    print("\n  CAT.3OX SETUP")
    print("  ================================")
    print()
    
    # Ask user which runtime
    print("  Choose runtime:")
    print("    [1] CORE (Python - free, testing)")
    print("    [2] RAW (Ruby - commercial, faster)")
    print()
    
    choice = input("  Enter choice [1/2]: ").strip()
    runtime = "CORE" if choice == "1" else "RAW" if choice == "2" else None
    
    if not runtime:
        print("\n  ERROR: Invalid choice. Run again and select 1 or 2.")
        return
    
    print(f"\n  Selected: {runtime} runtime")
    print()
    
    # Create first 5 categories
    print("  Creating 5 Life Domain Categories...")
    for cat in CATEGORIES[:5]:
        create_category(cat)
        install_runtime(Path(f"(CAT.{cat['num']}) {cat['name']}"), runtime)
    
    # Create ADMIN last (grand finale!)
    print("\n  ════════════════════════════════")
    print("  Creating Grand Finale: CAT.0 ADMIN")
    print("  ════════════════════════════════")
    create_category(CATEGORIES[5])
    install_runtime(Path("(CAT.0) ADMIN"), runtime)
    
    # Copy ADMIN tools into CAT.0 ADMIN
    import shutil
    admin_dest = Path("(CAT.0) ADMIN") / ".3ox"
    for tool in Path("ADMIN").glob("*"):
        shutil.copy2(tool, admin_dest)
    print(f"    ✓ Admin tools installed")
    
    print("\n  ================================")
    print("  SETUP COMPLETE!")
    print("  ================================")
    print()
    print("  Created: 5 life domain categories (CAT.1-5)")
    print("  Created: CAT.0 ADMIN (master orchestrator) 🎭")
    print(f"  Runtime: {runtime} installed in all categories")
    print()
    print("  Use ADMIN tools:")
    if runtime == "CORE":
        print("    cd '(CAT.0) ADMIN/.3ox'")
        print("    python cat-router.py dashboard")
        print("    python cat-trace.py report")
    else:
        print("    cd '(CAT.0) ADMIN/.3ox'")
        print("    ruby cat-router.rb dashboard")
        print("    ruby cat-trace.rb report")
    print()
    print("  Start using:")
    print("    Drop files in any category's 1N.3OX/ folder")
    print("    CAT.0 ADMIN orchestrates everything")
    print()

if __name__ == "__main__":
    main()

