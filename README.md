# 1n3ox - CORE.3ox Agent Runtime
**Version:** v1.1.0  
**Status:** Production Ready  
**License:** Commercial (see LICENSE)

---

## What is CORE.3ox?

A self-contained, offline AI agent runtime for secure file operations, validation, and automation. Perfect for developers, small businesses, and anyone needing controlled AI without cloud dependencies.

---

## Key Features

✅ **100% Offline** - No data sent to cloud  
✅ **Cryptographic Receipts** - Audit trail for all operations  
✅ **Machine-Bound Licensing** - Anti-piracy protection  
✅ **Fast Batch Operations** - Process multiple files efficiently  
✅ **Surgical Precision** - Minimal data exposure (76.8% less than cloud AI)

---

## Quick Start

### 1. Installation

```bash
git clone https://github.com/YOUR_USERNAME/1n3ox.git
cd 1n3ox/CORE.3ox
```

### 2. Requirements

- Python 3.8+ ([Download](https://www.python.org/downloads/))
- Dependencies: `pip install xxhash toml pyyaml tiktoken`

### 3. Run Operations

**Single operation:**
```bash
python CORE.3ox/run.py knowledge_update
```

**Batch operations:**
```bash
python CORE.3ox/run.py critical_error deploy_ready sync_request
```

**Note:** This is the Python version - ideal for testing and development. For production/commercial use with licensing, see **RAW.3ox** (Ruby version).

---

## What's Included

```
CORE.3ox/               - Python version (testing/dev)
├── run.py             - Main runtime (Python)
├── brain.rs           - Agent configuration
├── tools.yml          - Tool registry
├── routes.json        - Routing configuration
└── limits.toml        - Resource constraints

RAW.3ox/                - Ruby version (commercial/OG)
├── run.rb             - Main runtime (Ruby)
├── brain.rs           - Agent configuration (Rust)
├── brain.exe          - Compiled brain binary
├── tools.yml          - Tool registry
├── routes.json        - Routing configuration
├── limits.json        - Resource constraints
└── generate_key.rb    - License key generator
```

---

## Key Differentiators

**vs Cloud AI (ChatGPT, Claude):**
- ✅ No subscription fees
- ✅ No data leakage
- ✅ Works offline/air-gapped
- ✅ HIPAA/GDPR compliant by design

**vs Traditional Software:**
- ✅ AI-powered intelligence
- ✅ Self-contained (no dependencies)
- ✅ Cryptographic audit trail
- ✅ Machine-bound security

---

## Use Cases

**Developers:**
- File validation pipelines
- Automated testing
- CI/CD integration

**Small Business:**
- Document processing
- Data validation
- Compliance reporting

**Enterprise:**
- Regulated industry operations
- On-premise AI requirements
- Air-gapped environments

---

## Licensing

**CORE.3ox is commercial software.**

- Single machine: $299 one-time
- Multi-machine: Custom pricing
- Generated keys are machine-bound and non-transferable

**For commercial licensing:** contact@3ox.ai

**Free for evaluation:** 7-day trial keys available

---

## Documentation

- [README.md](CORE.3ox/README.md) - Full product documentation
- [LEXICON.md](CORE.3ox/LEXICON.md) - Terminology and concepts
- [EXAMPLES.md](CORE.3ox/EXAMPLES.md) - Practical usage examples
- [COMPLIANCE.md](CORE.3ox/COMPLIANCE.md) - Privacy and compliance

---

## Security & Privacy

**Machine Binding:** Each key is cryptographically bound to specific hardware  
**No Telemetry:** Zero network calls, zero data collection  
**Audit Trail:** SHA256/xxHash64 receipts for all operations  
**Offline Capable:** Works without internet connection

**Tested:** 100% offline verified, 0 external connections detected

---

## Support

- **Documentation:** [Full docs in CORE.3ox/](CORE.3ox/)
- **Issues:** Use GitHub Issues for bug reports
- **Email:** support@3ox.ai
- **Commercial:** sales@3ox.ai

---

## Project Structure

This repository contains the CORE.3ox base product. Other industry-specific variants:

- **LEGAL.3ox** ($999) - Law firms, contract editing
- **MEDICAL.3ox** ($1,499) - HIPAA-compliant healthcare
- **FINANCE.3ox** ($1,299) - SEC-compliant financial services
- **HR.3ox** ($599) - GDPR-compliant HR operations

**Website:** [3ox.store](https://3ox.store) (coming soon)

---

## Technical Details

**Main Runtime:** Python 3.8+ (testing/development)  
**Commercial Runtime:** Ruby 3.2+ (production/licensed)  
**Brain:** Rust (compiled to binary in RAW.3ox)  
**Hashing:** xxHash64 for speed  
**Performance:** 
- Python: ~2.6 seconds for 10 operations
- Ruby (RAW.3ox): ~2.2 seconds for 10 operations (faster!)

**Architecture:**
- Sentinel brain (Guardian-Synchronizer)
- Atomic operations with validation
- Automatic backup creation
- Cryptographic verification

---

## Version History

**v1.1.0** (2025-10-18)
- Initial public release
- Production-ready runtime
- Machine-bound licensing
- Batch operation support

---

## License

Copyright © 2025 3OX.AI  
Commercial software - see LICENSE file

**For evaluation/trial:** Generate 7-day key with `generate_key.rb --trial`

---

**Built with:** ⧗ 3OX.AI Framework  
**Status:** ✅ Production Ready  
**Build:** v1.1.0 | ⧗-25.291

:: ∎

