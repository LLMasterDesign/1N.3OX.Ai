# 3OX CLI - Offline-First Command Bridge

A sophisticated command bridge system built with Tauri frontend and FastAPI backend, designed for offline-first operations with optional online capabilities.

## 🎯 Overview

3OX CLI is a floating command bar (like Spotlight) that provides:
- **Offline-first architecture** - Works without internet by default
- **Command bridge interface** - Deterministic verbs, not chat
- **Role-based execution** - @SENTINEL, @LIGHTHOUSE, @ALCHEMIST, etc.
- **Security layer** - OPS tokens, sensitive file handling, 2FA gating
- **Job queue system** - Reliable file-based queue with receipts
- **Docker support** - Containerized deployment

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Tauri UI      │    │   FastAPI       │    │   Job Queue     │
│   (Floating Bar)│◄──►│   Backend       │◄──►│   (.3ox/queue)  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Command       │    │   Offline/      │    │   Receipts &    │
│   Parsing       │    │   Online        │    │   Audit Logs    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Rust toolchain
- Node.js (≥18)
- Python 3.11+
- Docker (optional)

### Installation

1. **Clone and setup:**
```bash
git clone <repository>
cd 3ox-cli
./setup.sh
```

2. **Start development:**
```bash
# Option 1: Docker (recommended)
docker-compose up

# Option 2: Manual
# Terminal 1 - Backend
cd backend
source venv/bin/activate
python -m uvicorn app.main:app --reload

# Terminal 2 - Frontend  
cd frontend
pnpm tauri dev
```

3. **Use the CLI:**
- Press `Ctrl+Space` to open the 3OX Bar
- Type commands like: `organize ~/Pictures` or `summarize ~/Documents`
- Select roles: @SENTINEL, @LIGHTHOUSE, @ALCHEMIST, @BRIDGE, @MASTER

## 📋 Command Examples

### File Organization
```bash
@LIGHTHOUSE organize ~/Pictures --by-year
@SENTINEL audit ~/Downloads --find-duplicates
@ALCHEMIST extract ~/Documents --metadata
```

### Data Processing
```bash
@ALCHEMIST summarize ~/Vault/Notes --allow-online
@BRIDGE sync ~/Projects --backup
@MASTER clean ~/tmp --remove-old
```

### Security Operations
```bash
@SENTINEL secure-delete ~/Private --confirm
@LIGHTHOUSE audit ~/.ssh --check-permissions
```

## ⚙️ Configuration

### Local Policy (`.3ox/config/local_policy.json`)
```json
{
  "allow_online": false,
  "sensitive_paths": ["~/Private", "~/Vault"],
  "local_model_capacity_tokens": 2048,
  "cost_cap_daily": 2.0,
  "model_whitelist": ["gpt-3.5-turbo", "claude-3-haiku"]
}
```

### OPS Security (`.3ox/ops/policy.json`)
```json
{
  "ops_required_actions": [
    "modify .3ox files",
    "deploy to R:/3OX.Ai",
    "change POLICY/*"
  ],
  "2fa_required": true,
  "token_expiry_hours": 24
}
```

## 🔒 Security Features

### Offline-First Design
- All operations default to offline execution
- Local model capacity limits (2048 tokens default)
- Sensitive file detection and redaction
- No external calls without explicit permission

### OPS Security Layer
- Operational authority tokens for protected actions
- 2FA gating for sensitive operations
- Immutable audit receipts
- Cost caps and whitelist enforcement

### Sensitive Data Handling
- Automatic PII redaction before online calls
- Encrypted local storage of sensitive uploads
- Auditable redaction logs
- Explicit user confirmation for sensitive operations

## 🏛️ Job Queue System

### Queue Structure
```
.3ox/queue/
├── NEW/           # New jobs waiting for processing
├── CLAIMED/       # Jobs currently being processed
├── RESULTS/       # Completed job results
└── RECEIPTS/      # Immutable audit receipts
```

### Job Packet Format
```json
{
  "id": "3ox-20250123-abc123",
  "created_at": "2025-01-23T18:00:00Z",
  "sirius_time": "⧗-25.108",
  "user": "rvnx/lucius",
  "role": "@LIGHTHOUSE",
  "mode": "!ANALYTICAL",
  "prompt": "organize ~/Pictures by year",
  "targets": ["~/Pictures"],
  "sensitive": false,
  "allow_online": false,
  "ops_action": false
}
```

## 🧠 Agent Roles

| Role | Purpose | Capabilities |
|------|---------|--------------|
| @SENTINEL | Security monitoring | Audit, secure-delete, monitor |
| @LIGHTHOUSE | Guidance & navigation | Summarize, organize, guide |
| @ALCHEMIST | Data transformation | Extract, transform, analyze |
| @BRIDGE | Communication | Sync, coordinate, communicate |
| @MASTER | General purpose | Organize, process, manage |

## 🔧 Development

### Project Structure
```
3ox-cli/
├── frontend/          # Tauri application
│   ├── src/          # UI components
│   └── src-tauri/    # Rust configuration
├── backend/           # FastAPI service
│   ├── app/          # Application code
│   └── requirements.txt
├── shared/            # Shared components
│   ├── schemas/      # Data models
│   ├── llmd/         # LLMD validation
│   └── security/     # OPS security
├── .3ox/             # Runtime directory
└── docker-compose.yml
```

### Adding New Commands
1. Add action to `OfflineExecutor.supported_actions`
2. Implement action method
3. Update command parsing in frontend
4. Add tests

### Adding New Connectors
1. Add connector to `OnlineConnector.connectors`
2. Implement connector method
3. Update connector selection logic
4. Add cost estimation

## 🐳 Docker Deployment

```bash
# Build and run
docker-compose up --build

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

## 📊 Monitoring

### Job Status
- Check `.3ox/queue/RESULTS/` for completed jobs
- View `.3ox/receipts/` for audit trail
- Monitor logs for errors and performance

### Health Checks
- Backend: `http://localhost:8000/`
- Frontend: Check Tauri window responsiveness
- Queue: Monitor queue directory sizes

## 🧪 Testing

```bash
# Test offline execution
curl -X POST http://localhost:8000/api/3oxjob \
  -H "Content-Type: application/json" \
  -d '{"role": "@SENTINEL", "prompt": "clean tmp", "allow_online": false}'

# Test sensitive data handling
curl -X POST http://localhost:8000/api/3oxjob \
  -H "Content-Type: application/json" \
  -d '{"role": "@LIGHTHOUSE", "prompt": "summarize ~/Vault", "sensitive": true}'
```

## 📚 API Reference

### Endpoints
- `POST /api/3oxjob` - Submit new job
- `GET /api/job/{job_id}` - Get job status
- `POST /api/confirm/{job_id}` - Confirm job requiring approval

### Response Format
```json
{
  "job_id": "3ox-20250123-abc123",
  "status": "SUCCESS",
  "message": "Job completed successfully",
  "result_data": { ... },
  "requires_confirmation": false
}
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Implement changes with tests
4. Submit pull request

## 📄 License

MIT License - see LICENSE file for details

## 🆘 Support

- Issues: GitHub Issues
- Documentation: `/docs` directory
- Community: Discord/Matrix (TBD)

---

**3OX CLI** - Command Bridge for the Digital Age

*"From keystroke to action, offline to online, command to completion."*

:: ∎