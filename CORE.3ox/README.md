# CORE.3ox - Python Runtime (Testing & Development)
**Version:** v1.1.0  
**Runtime:** Python 3.8+  
**Purpose:** Development, testing, and user-friendly operations

---

## What is CORE.3ox?

The **Python implementation** of the .3ox agent runtime. Perfect for:
- ✅ **Testing and development** - Fast iteration, easy debugging
- ✅ **Learning the system** - Readable code, clear structure
- ✅ **Cross-platform** - Works everywhere Python works
- ✅ **No compilation** - Just run it

**For production/commercial use with licensing:** See `RAW.3ox` (Ruby version)

---

## Installation

### 1. Install Python
Download from [python.org](https://www.python.org/downloads/) (3.8 or higher)

### 2. Install Dependencies
```bash
pip install xxhash toml pyyaml tiktoken
```

### 3. Run It
```bash
python run.py knowledge_update
```

---

## Features

✅ **File Operations**
- Validate file integrity with xxHash64
- Generate cryptographic receipts
- Audit trail for all operations

✅ **Routing System**
- Auto-route files to destinations
- Custom routing rules via `routes.json`

✅ **Resource Management**
- File size limits enforcement (`limits.toml`)
- Token/cost tracking with `tiktoken`

✅ **Security**
- 100% offline operation
- No data sent to cloud
- Cryptographic audit trail

---

## Files Included

```
CORE.3ox/
├── run.py           ← Main runtime (Python)
├── brain.rs         ← Agent configuration
├── tools.yml        ← Tool registry
├── routes.json      ← Routing configuration
├── limits.toml      ← Resource constraints
├── 3ox.log          ← Operation logs
└── !KEY             ← Agent identity
```

---

## Usage Examples

**Single operation:**
```bash
python run.py knowledge_update
```

**Batch operations:**
```bash
python run.py critical_error deploy_ready sync_request
```

**With custom file:**
```bash
python run.py validate_files --file=myfile.txt
```

---

## Configuration

### routes.json
Define where outputs go:
```json
{
  "routes": {
    "knowledge_update": "OBSIDIAN.BASE",
    "critical_error": "CMD.BRIDGE",
    "deploy_ready": "SYNTH.BASE"
  }
}
```

### limits.toml
Set resource constraints:
```toml
[files]
max_size = 10485760  # 10MB

[tokens.models.claude_sonnet_4]
context = 200000
cost_per_million = 3.00
```

### tools.yml
Available operations:
```yaml
tools:
  - name: file_validation
    description: Validate file integrity
    enabled: true
```

---

## Differences from RAW.3ox (Ruby)

| Feature | CORE.3ox (Python) | RAW.3ox (Ruby) |
|---------|------------------|----------------|
| **Speed** | ~2.6s for 10 ops | ~2.2s for 10 ops ⚡ |
| **Licensing** | None (open) | Machine-bound 🔒 |
| **Compilation** | No | Yes (Rust brain) |
| **Best for** | Testing, dev | Production, commercial |
| **Dependencies** | pip install | gem install |
| **Config format** | TOML, YML | JSON, YML |

---

## When to Use This Version

**Use CORE.3ox (Python) if:**
- 🧪 Testing and development
- 📚 Learning the .3ox system
- 🔧 Rapid prototyping
- 🐍 Python-first environment
- 🆓 No licensing needed

**Use RAW.3ox (Ruby) if:**
- 🏭 Production deployment
- 💼 Commercial application
- 🔒 Need machine-bound licensing
- ⚡ Need maximum speed
- 🛡️ Regulatory compliance (HIPAA/GDPR)

---

## Support

- **Issues:** Use GitHub Issues
- **Docs:** See main README.md
- **Commercial:** For RAW.3ox, contact sales@3ox.ai

---

**Version:** v1.1.0 | Python Runtime  
**Build:** ⧗-25.291

:: ∎

