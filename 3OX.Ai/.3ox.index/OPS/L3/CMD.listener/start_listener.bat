@echo off
echo Starting CMD.BRIDGE 0ut.3ox/1n.3ox Listener...
cd /d "%~dp0"
pip install -r requirements.txt
python listener.py
pause
