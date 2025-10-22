#!/bin/bash
# Run script for Website Monitoring Agent

set -e

echo "▛▞ Starting Website Monitoring Agent..."

# Activate virtual environment if exists
if [ -d "venv" ]; then
    source venv/bin/activate
    echo "✓ Virtual environment activated"
fi

# Run the monitoring agent
cd /workspace
python src/main.py

echo ":: ∎"
