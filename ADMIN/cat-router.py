#!/usr/bin/env python3
"""
CAT-ROUTER - Category Management (Python)
Version: 1.0
"""

import os
import sys
from pathlib import Path
from datetime import datetime
import shutil

CAT_FOLDERS = [
    "(CAT.1) Self",
    "(CAT.2) Education",
    "(CAT.3) Business",
    "(CAT.4) Family",
    "(CAT.5) Social"
]

def show_dashboard():
    """View all category status"""
    print("\n  CAT ROUTER DASHBOARD")
    print("  ====================")
    print()
    
    for cat in CAT_FOLDERS:
        if Path(cat).exists():
            inbox_path = Path(cat) / "1N.3OX"
            if inbox_path.exists():
                item_count = len(list(inbox_path.glob("*")))
                if item_count > 0:
                    print(f"  {cat} - {item_count} items")
                else:
                    print(f"  {cat} - Empty")
    
    print()
    print("  Commands: python cat-router.py [dashboard|showall|route|transfer]")
    print()

def show_all():
    """List all items in all categories"""
    print("\n  ALL ITEMS")
    print("  =========")
    print()
    
    total_items = 0
    
    for cat in CAT_FOLDERS:
        if Path(cat).exists():
            inbox_path = Path(cat) / "1N.3OX"
            if inbox_path.exists():
                items = list(inbox_path.glob("*"))
                if items:
                    print(f"  {cat} - {len(items)} items")
                    for item in items:
                        print(f"    - {item.name}")
                    print()
                    total_items += len(items)
    
    print(f"  Total: {total_items} items")
    print()

def route_item(item_path, target_category):
    """Route item to specific category"""
    source = Path(item_path)
    if not source.exists():
        print(f"  ERROR: Item not found: {item_path}")
        return
    
    target_inbox = Path(target_category) / "1N.3OX"
    if not target_inbox.exists():
        print(f"  ERROR: Category not found: {target_category}")
        return
    
    destination = target_inbox / source.name
    shutil.move(str(source), str(destination))
    
    # Log to category
    log_path = Path(target_category) / ".3ox" / "3ox.log"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"\n[{timestamp}] ROUTED: {source.name}"
    
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(log_entry)
    
    print(f"  SUCCESS: {source.name} -> {target_category}")

def show_help():
    print("""
  CAT-ROUTER Commands:
  ====================
  
  python cat-router.py dashboard
    View status of all categories
  
  python cat-router.py showall
    List all items in all categories
  
  python cat-router.py route <file> <category>
    Route item to specific category
    
  Example:
    python cat-router.py route invoice.pdf "(CAT.3) Business"
""")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
    elif sys.argv[1] == "dashboard":
        show_dashboard()
    elif sys.argv[1] == "showall":
        show_all()
    elif sys.argv[1] == "route" and len(sys.argv) >= 4:
        route_item(sys.argv[2], sys.argv[3])
    else:
        show_help()

