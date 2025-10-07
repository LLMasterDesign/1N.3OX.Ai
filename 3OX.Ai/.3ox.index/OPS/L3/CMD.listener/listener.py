#!/usr/bin/env python3
"""
CMD.BRIDGE Background Listener
Listens for 0ut.3ox and 1n.3ox transactions and logs them
"""

import os
import time
import yaml
import json
from datetime import datetime
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ThreeOxHandler(FileSystemEventHandler):
    def __init__(self):
        self.tx_log = Path("tx.log")
        self.rx_log = Path("rx.log")
        self.sirius_start = datetime(2025, 8, 8)
    
    def get_sirius_time(self):
        """Calculate current Sirius time"""
        now = datetime.now()
        days = (now - self.sirius_start).days
        year = now.year % 100
        return f"⧗-{year}.{days}"
    
    def log_transaction(self, event_type, file_path, data=None):
        """Log transaction to appropriate log file"""
        sirius_time = self.get_sirius_time()
        timestamp = datetime.now().isoformat()
        
        log_entry = {
            "sirius_time": sirius_time,
            "timestamp": timestamp,
            "event_type": event_type,
            "file_path": str(file_path),
            "data": data
        }
        
        if "0ut" in str(file_path):
            log_file = self.tx_log
            direction = "TX"
        else:
            log_file = self.rx_log
            direction = "RX"
        
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"[{direction}] {sirius_time} - {event_type}: {file_path}\n")
            if data:
                f.write(f"  Data: {json.dumps(data, indent=2)}\n")
            f.write("\n")
    
    def on_created(self, event):
        if not event.is_directory:
            file_path = Path(event.src_path)
            if file_path.suffix in ['.yaml', '.yml', '.json']:
                if "0ut.3ox" in str(file_path) or "1n.3ox" in str(file_path):
                    # Try to read and parse the file
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            if file_path.suffix in ['.yaml', '.yml']:
                                data = yaml.safe_load(f)
                            else:
                                data = json.load(f)
                    except Exception as e:
                        data = {"error": str(e)}
                    
                    self.log_transaction("CREATED", file_path, data)
    
    def on_modified(self, event):
        if not event.is_directory:
            file_path = Path(event.src_path)
            if "0ut.3ox" in str(file_path) or "1n.3ox" in str(file_path):
                self.log_transaction("MODIFIED", file_path)

def main():
    """Start the background listener"""
    event_handler = ThreeOxHandler()
    observer = Observer()
    
    # Watch the L3 directory for changes
    watch_path = Path(__file__).parent.parent
    observer.schedule(event_handler, str(watch_path), recursive=True)
    
    print(f"🔍 CMD.BRIDGE Listener started - watching {watch_path}")
    print("📡 Monitoring 0ut.3ox and 1n.3ox transactions...")
    print("📝 Logging to tx.log and rx.log")
    print("Press Ctrl+C to stop")
    
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n🛑 Listener stopped")
    
    observer.join()

if __name__ == "__main__":
    main()
