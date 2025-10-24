#!/bin/bash

# 3OX CLI Development Setup Script
# Sets up the complete development environment

set -e

echo "🚀 Setting up 3OX CLI Development Environment"
echo "=============================================="

# Check if we're in the right directory
if [ ! -f "docker-compose.yml" ]; then
    echo "❌ Please run this script from the 3ox-cli root directory"
    exit 1
fi

# Create .3ox directory structure
echo "📁 Creating .3ox directory structure..."
mkdir -p .3ox/{queue/{NEW,CLAIMED,RESULTS,RECEIPTS},receipts,secure_uploads,config,ops}

# Set up Python virtual environment for backend
echo "🐍 Setting up Python backend..."
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd ..

# Install Node.js dependencies for frontend
echo "📦 Installing frontend dependencies..."
cd frontend
pnpm install
cd ..

# Create initial configuration files
echo "⚙️ Creating configuration files..."

# Create .3ox/config/local_policy.json
cat > .3ox/config/local_policy.json << EOF
{
  "allow_online": false,
  "sensitive_paths": [
    "~/Private",
    "~/Vault",
    "~/Downloads/Encrypted"
  ],
  "local_model_capacity_tokens": 2048,
  "cost_cap_daily": 2.0,
  "model_whitelist": [
    "gpt-3.5-turbo",
    "gpt-4",
    "claude-3-haiku"
  ],
  "redaction_policy": {
    "auto_redact": true,
    "patterns": ["email", "ssn", "credit_card", "phone"]
  }
}
EOF

# Create .3ox/ops/policy.json
cat > .3ox/ops/policy.json << EOF
{
  "ops_required_actions": [
    "modify .3ox files",
    "deploy to R:/3OX.Ai",
    "change POLICY/*",
    "modify OPS tokens"
  ],
  "sensitive_paths": [
    "~/Private",
    "~/Vault",
    "~/Downloads/Encrypted"
  ],
  "2fa_required": true,
  "token_expiry_hours": 24
}
EOF

# Create .3ox/ops/tokens.json
cat > .3ox/ops/tokens.json << EOF
{
  "tokens": {}
}
EOF

# Create environment file
cat > .env << EOF
# 3OX CLI Environment Configuration
THREEOX_ROOT=.3ox
API_URL=http://localhost:8000
FRONTEND_URL=http://localhost:3000

# Optional: API Keys (uncomment and add your keys)
# OPENAI_API_KEY=your_openai_key_here
# ANTHROPIC_API_KEY=your_anthropic_key_here
# WEB_SEARCH_API_KEY=your_search_key_here
EOF

echo "✅ Setup complete!"
echo ""
echo "🎯 Next steps:"
echo "1. Start the backend: cd backend && source venv/bin/activate && python -m uvicorn app.main:app --reload"
echo "2. Start the frontend: cd frontend && pnpm tauri dev"
echo "3. Or use Docker: docker-compose up"
echo ""
echo "📖 Usage:"
echo "- Press Ctrl+Space to open the 3OX Bar"
echo "- Type commands like: 'organize ~/Pictures' or 'summarize ~/Documents'"
echo "- Use role selectors: @SENTINEL, @LIGHTHOUSE, @ALCHEMIST, etc."
echo ""
echo "🔧 Configuration:"
echo "- Edit .3ox/config/local_policy.json for offline/online settings"
echo "- Edit .3ox/ops/policy.json for security settings"
echo "- Add API keys to .env file for online features"
echo ""
echo ":: ∎"