#!/bin/bash
# Setup script for Website Monitoring Agent

set -e

echo "▛▞ Website Monitoring Agent Setup"
echo "=================================="
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | grep -oP '\d+\.\d+')
required_version="3.8"

if (( $(echo "$python_version >= $required_version" | bc -l) )); then
    echo "✓ Python $python_version detected"
else
    echo "✗ Python $required_version or higher required"
    exit 1
fi

# Create virtual environment
echo ""
echo "Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt
echo "✓ Dependencies installed"

# Create config from template if not exists
echo ""
echo "Setting up configuration..."
if [ ! -f "src/config.yaml" ]; then
    echo "✓ Config file already exists at src/config.yaml"
    echo "⚠ Remember to update Telegram credentials!"
else
    echo "✓ Using existing config.yaml"
fi

# Run tests
echo ""
echo "Running tests..."
pytest tests/ -v --tb=short
echo "✓ Tests passed"

echo ""
echo "=================================="
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit src/config.yaml with your settings"
echo "2. Add your Telegram bot token and chat ID"
echo "3. Run: python src/main.py"
echo ""
echo "For Telegram bot setup:"
echo "- Message @BotFather to create a bot"
echo "- Message @userinfobot to get your chat ID"
echo ""
echo ":: ∎"
