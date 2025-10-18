# CORE.3ox Setup Guide
**Python Runtime** - Free Testing & Development Version

---

## Quick Start (2 minutes)

### Step 1: Install Python
**Need Python 3.8 or higher**

**Windows:**
```bash
winget install Python.Python.3.11
# or download from https://www.python.org/downloads/
```

**Mac:**
```bash
brew install python@3.11
```

**Linux:**
```bash
sudo apt install python3 python3-pip
```

**Verify:**
```bash
python --version
# Should show: Python 3.8+ 
```

---

### Step 2: Install Dependencies
```bash
pip install xxhash toml pyyaml tiktoken
```

**Expected output:**
```
Successfully installed xxhash-3.x.x toml-0.x.x PyYAML-6.x tiktoken-0.x.x
```

---

### Step 3: Test It!
```bash
# Navigate to CORE.3ox folder
cd CORE.3ox

# Run a test operation
python run.py knowledge_update
```

**Expected output:**
```
============================================================
3OX TESTRUN :: Python Runtime
============================================================

✓ Brain: VALIDATOR (Sentinel)
✓ Tools loaded: 4 available
✓ File validated
✓ Receipt generated
✓ Routed to: OBSIDIAN.BASE

TEST COMPLETE
```

---

## That's It!

**No license keys, no compilation, no hassle.**

---

## Usage Examples

### Single Operation
```bash
python run.py knowledge_update
```

### Batch Operations (Multiple at Once)
```bash
python run.py critical_error deploy_ready sync_request
```

### Available Operations
- `knowledge_update` - Routes to OBSIDIAN.BASE
- `critical_error` - Routes to CMD.BRIDGE  
- `deploy_ready` - Routes to SYNTH.BASE
- `sync_request` - Routes to SYNTH.BASE
- `emergency` - Routes to CMD.BRIDGE/EMERGENCY

---

## Configuration Files

### routes.json
Define where operations route to:
```json
{
  "routes": {
    "knowledge_update": "OBSIDIAN.BASE",
    "critical_error": "CMD.BRIDGE"
  }
}
```

### limits.toml
Set resource constraints:
```toml
[files]
max_size = 104857600  # 100MB

[tokens.models.claude_sonnet_4]
context = 200000
cost_per_million = 3.00
```

### tools.yml
Available tools/operations:
```yaml
tools:
  - name: file_validation
    enabled: true
```

---

## Outputs

**Logs:**
- `3ox.log` - All operations logged here

**Receipts:**
- `0ut.3ox/receipts.log` - Cryptographic receipts

**Routed Files:**
- `CMD.BRIDGE/` - Critical/emergency operations
- `OBSIDIAN.BASE/` - Knowledge/documentation  
- `SYNTH.BASE/` - Synthesis/deployment

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'xxhash'"
**Fix:** Run `pip install xxhash toml pyyaml tiktoken`

### "python: command not found"
**Fix:** Install Python 3.8+ (see Step 1)

### "UnicodeEncodeError" on Windows
**Fix:** Already handled in run.py! If you still see this, update the file.

### Operations run but no output files
**Fix:** Check permissions on current directory

---

## Differences from RAW.3ox (Commercial Version)

| Feature | CORE.3ox (This) | RAW.3ox (Commercial) |
|---------|-----------------|---------------------|
| **Cost** | Free | $299-$1,499 |
| **Speed** | ~2.6s (10 ops) | ~2.2s (15% faster) |
| **Licensing** | None | Machine-bound 🔒 |
| **Setup** | 2 minutes | 5 minutes + key |
| **Best for** | Testing, dev | Production |

---

## Need Production/Commercial Version?

**RAW.3ox offers:**
- ⚡ 15% faster performance
- 🔒 Machine-bound licensing (anti-piracy)
- 🛡️ HIPAA/GDPR compliance features
- 💼 Commercial support
- 🔪 Surgical editing tools
- 📋 Compliance documentation

**Contact:** sales@3ox.ai  
**Pricing:** $299-$1,499 (one-time, no subscription)

---

**Ready to build!** 🚀

:: ∎

