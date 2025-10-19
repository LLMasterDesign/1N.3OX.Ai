#!/usr/bin/env python3
"""
CAT-TRACE - Category Trace System
Version: 1.0

Installs .3ox RAW files into each category and provides trace functions
"""

import os
import shutil
import sys
from pathlib import Path
from datetime import datetime

# Template files to install
TEMPLATE_FILES = {
    '!ATTN': '.3ox.TEMPLATE/!ATTN',
    '.3ox/brain.rs': '.3ox.TEMPLATE/.3ox/brain.rs',
    '.3ox/tools.rs': '.3ox.TEMPLATE/.3ox/tools.rs',
    '.3ox/run.rb': '.3ox.TEMPLATE/.3ox/run.rb',
    '.3ox/3ox.log': '.3ox.TEMPLATE/.3ox/3ox.log',
}

def get_categories():
    """Find all CAT folders"""
    categories = []
    for item in Path('.').iterdir():
        if item.is_dir() and item.name.startswith('(CAT.'):
            categories.append(item)
    return sorted(categories)

def install_templates(category_path):
    """Install .3ox template files into a category"""
    print(f"\n  Installing templates into: {category_path.name}")
    
    dotpath = category_path / '.3ox'
    if not dotpath.exists():
        print(f"    ERROR: {category_path.name}/.3ox/ not found")
        return False
    
    installed = 0
    for dest_rel, src_rel in TEMPLATE_FILES.items():
        src = Path(src_rel)
        if not src.exists():
            print(f"    WARNING: Template not found: {src}")
            continue
        
        # Determine destination
        if dest_rel.startswith('.3ox/'):
            # Goes inside .3ox folder
            dest = dotpath / dest_rel.replace('.3ox/', '')
        else:
            # Goes at category root
            dest = category_path / dest_rel
        
        try:
            # Create parent directory if needed
            dest.parent.mkdir(parents=True, exist_ok=True)
            
            # Copy file
            shutil.copy2(src, dest)
            print(f"    ✓ Installed: {dest_rel}")
            installed += 1
        except Exception as e:
            print(f"    ERROR installing {dest_rel}: {e}")
    
    return installed > 0

def scrape_logs(category_path):
    """Scrape .3ox.log for receipts"""
    logfile = category_path / '.3ox' / '.3ox.log'
    if not logfile.exists():
        return []
    
    receipts = []
    try:
        with open(logfile, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if 'ROUTED:' in line or 'COMPLETE' in line or 'SUCCESS' in line:
                    receipts.append(line.strip())
    except Exception as e:
        print(f"    ERROR reading log: {e}")
    
    return receipts

def generate_report():
    """Generate trace report for all categories"""
    categories = get_categories()
    
    print("\n  CAT-TRACE REPORT")
    print("  ================")
    print(f"\n  Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Categories: {len(categories)}")
    print()
    
    total_receipts = 0
    for cat in categories:
        receipts = scrape_logs(cat)
        total_receipts += len(receipts)
        
        if receipts:
            print(f"  {cat.name} - {len(receipts)} receipts")
            for receipt in receipts[:3]:  # Show first 3
                print(f"    • {receipt[:60]}...")
            if len(receipts) > 3:
                print(f"    ... and {len(receipts) - 3} more")
        else:
            print(f"  {cat.name} - No activity")
    
    print(f"\n  Total receipts: {total_receipts}")
    print()

def batch_receipts():
    """Batch all receipts into a single file"""
    categories = get_categories()
    
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    batch_file = f"receipts-batch-{timestamp}.yaml"
    
    print(f"\n  Batching receipts to: {batch_file}")
    
    with open(batch_file, 'w', encoding='utf-8') as out:
        out.write(f"# Receipt Batch - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        out.write(f"# Categories: {len(categories)}\n\n")
        
        for cat in categories:
            receipts = scrape_logs(cat)
            if receipts:
                out.write(f"## {cat.name}\n")
                out.write(f"receipts: {len(receipts)}\n")
                for receipt in receipts:
                    out.write(f"  - {receipt}\n")
                out.write("\n")
    
    print(f"  ✓ Batched {sum(len(scrape_logs(c)) for c in categories)} receipts")
    print()

def show_help():
    """Show command help"""
    print("""
  CAT-TRACE Commands:
  ===================
  
  python cat-trace.py install
    Install .3ox template files into all categories
  
  python cat-trace.py report
    Generate trace report from all .3ox.log files
  
  python cat-trace.py batch
    Batch all receipts into single file
  
  python cat-trace.py help
    Show this help
""")

def main():
    if len(sys.argv) < 2:
        show_help()
        return
    
    action = sys.argv[1].lower()
    
    if action == 'install':
        categories = get_categories()
        print(f"\n  Installing .3ox templates into {len(categories)} categories...")
        
        success = 0
        for cat in categories:
            if install_templates(cat):
                success += 1
        
        print(f"\n  ✓ Installed templates in {success}/{len(categories)} categories")
        print()
    
    elif action == 'report':
        generate_report()
    
    elif action == 'batch':
        batch_receipts()
    
    elif action == 'help':
        show_help()
    
    else:
        print(f"\n  ERROR: Unknown action '{action}'")
        show_help()

if __name__ == '__main__':
    main()

