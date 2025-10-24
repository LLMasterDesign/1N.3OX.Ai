# 3OX CLI Project Structure

## Root Directory Layout
```
3ox-cli/
├── frontend/                 # Tauri application
│   ├── src/
│   │   ├── main.js          # Floating bar UI
│   │   └── components/      # UI components
│   ├── src-tauri/
│   │   ├── src/main.rs      # Tauri configuration
│   │   └── Cargo.toml
│   └── tauri.conf.json
├── backend/                  # FastAPI service
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py          # FastAPI app
│   │   ├── models/          # Data models
│   │   ├── services/        # Business logic
│   │   └── utils/           # Utilities
│   ├── requirements.txt
│   └── Dockerfile
├── shared/                   # Shared components
│   ├── schemas/             # Job packet schemas
│   ├── llmd/                # LLMD validation
│   └── security/            # OPS security
├── docker-compose.yml
├── .3ox/                    # Runtime directory
│   ├── queue/
│   │   ├── NEW/            # New jobs
│   │   ├── CLAIMED/        # Processing jobs
│   │   ├── RESULTS/        # Completed jobs
│   │   └── RECEIPTS/       # Job receipts
│   ├── receipts/           # Immutable audit logs
│   ├── secure_uploads/     # Encrypted sensitive data
│   └── config/             # Configuration files
└── README.md
```

## Key Components

### 1. Job Queue System
- File-based queue for reliability
- JSON job packets with LLMD headers
- Immutable receipts with Sirius timestamps

### 2. Security Architecture
- OPS token validation
- Sensitive file detection and redaction
- 2FA gating for protected operations

### 3. Offline/Online Routing
- Local model capacity limits
- Connector priority system
- Cost caps and whitelist enforcement

### 4. Command Bridge Interface
- Deterministic verb parsing
- Role-based execution (@SENTINEL, @LIGHTHOUSE, etc.)
- Single-shot requests with clear status