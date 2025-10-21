<!-- Hello World -->
# 1N.3OX.Ai - 3OX Architecture
**Modular AI Agent System with Event-Driven Routing**

---

## What is 3OX Architecture?

A **layered, event-driven AI agent system** with clear separation of concerns:

```
┌─────────────────────────────────────────────┐
│             1n3ox (Input)                   │
│  Piezoelectric monitoring & routing         │
│  - ONE per ops/base                         │
│  - Monitors incoming files                  │
│  - Ticket-based routing                     │
│  - Files move only when complete/error      │
│  └── 0ut3ox nested (receipts/logs/requests)│
└──────────────────┬──────────────────────────┘
                   │
                   ↓
┌─────────────────────────────────────────────┐
│            cat.3ox (Middleware)             │
│  Category orchestration                     │
│  - 5-8 category folders                     │
│  - Half .3ox persona, half 1n3ox routing    │
│  - Has own 1n3ox, NO 0ut3ox                 │
└──────────────────┬──────────────────────────┘
                   │
                   ↓
┌─────────────────────────────────────────────┐
│              .3ox (Runtime)                 │
│  Core agent execution                       │
│  - CORE.3ox (Python - free)                 │
│  - RAW.3ox (Ruby - commercial)              │
│  - Brain + Spine + Legs                     │
└─────────────────────────────────────────────┘
```

**Key Principle:** Each layer is separate - no mixing, no confusion.

---

## Repository Structure

### Branch: `1n3ox`
**Input Layer + Output**
- Piezoelectric file monitoring
- Ticket routing system
- Station availability tracking
- Nested: 0ut3ox (receipts, logs, requests)

**Usage:** ONE per ops/base (singleton pattern)  
**Status:** Ready for implementation

### Branch: `cat3ox`
**Category Middleware**
- 5-8 category folders
- Smart routing logic
- Half persona, half routing
- Has own 1n3ox (no 0ut3ox)

**Usage:** Orchestrates between input and runtime  
**Status:** Ready for implementation

### Branch: `core-runtime`
**.3ox Agent Runtime**
- CORE.3ox (Python) - Free for testing
- RAW.3ox (Ruby) - Commercial with licensing
- Pre-flight checks, validation, compliance

**Usage:** The actual agent execution layer  
**Status:** ✅ Production ready

### Branch: `3ox-sets`
**SaaS Platform**
- Next.js web application
- Landing page, pricing, features
- User authentication
- Business/monetization strategy

**Usage:** Web interface for 3OX products  
**Status:** ✅ Platform ready

### Branch: `experiments`
**Testing & Experiments**
- Proof of concepts
- Performance testing
- Feature experiments
- Not production code

**Usage:** R&D and validation  
**Status:** Open for experiments

---

## Quick Start

### Get the Full System
```bash
# Clone everything
git clone https://github.com/LLMasterDesign/1N.3OX.Ai.git
cd 1N.3OX.Ai

# Setup each layer
git checkout 1n3ox         # Input/output layer
git checkout cat3ox        # Middleware  
git checkout core-runtime  # Agent runtime
git checkout 3ox-sets      # SaaS platform
```

### Get Just What You Need
```bash
# Just the runtime (most common)
git clone -b core-runtime https://github.com/LLMasterDesign/1N.3OX.Ai.git

# Just the SaaS platform
git clone -b 3ox-sets https://github.com/LLMasterDesign/1N.3OX.Ai.git

# Just input layer
git clone -b 1n3ox https://github.com/LLMasterDesign/1N.3OX.Ai.git
```

---

## Architecture Principles

1. **Separation of Layers**
   - Each layer has clear boundaries
   - No cross-contamination
   - Modular replacement

2. **Singleton Pattern (1n3ox)**
   - ONE input monitor per ops/base
   - Prevents routing conflicts
   - Central ticket system

3. **Scalable Output (0ut3ox)**
   - MANY output collectors
   - All connected to 1n3ox
   - Receipts, logs, requests separate

4. **Smart Middleware (cat.3ox)**
   - Knows what belongs where
   - Orchestrates routing
   - Half persona (smart), half router (efficient)

5. **Runtime Independence (.3ox)**
   - Executes without knowing about layers above
   - Portable, testable
   - Free (Python) and Commercial (Ruby) versions

---

## Use Cases

### Law Firm
```
1n3ox → monitors: incoming contracts
cat.3ox → routes to: LEGAL category
.3ox → executes: surgical contract editing
0ut3ox → logs: compliance receipts
```

### Healthcare
```
1n3ox → monitors: patient records
cat.3ox → routes to: MEDICAL category
.3ox → executes: HIPAA-compliant ops
0ut3ox → logs: PHI access audit trail
```

### Development
```
1n3ox → monitors: code changes
cat.3ox → routes to: appropriate base
.3ox → executes: validation
0ut3ox → logs: test results
```

---

## Documentation

- **ARCHITECTURE.md** - Deep dive into design
- **SETUP.md** - Installation guide
- **COMPARISON.md** - vs traditional approaches
- **FAQ.md** - Common questions

**Per-Branch Docs:**
- `1n3ox/README.md` - Input layer specifics
- `cat3ox/README.md` - Middleware specifics  
- `core-runtime/README.md` - Runtime specifics

---

## Why This Architecture?

**Problem:** AI agents are chaotic
- Files processed randomly
- No tracking
- No validation
- No compliance

**Solution:** Structured flow
- ✅ Everything monitored (1n3ox)
- ✅ Everything categorized (cat.3ox)
- ✅ Everything validated (.3ox)
- ✅ Everything logged (0ut3ox)

**Result:** Predictable, auditable, compliant AI operations

---

## Contributing

See `experiments` branch for:
- Testing new features
- Performance benchmarks
- Proof of concepts

**Branch Protection:**
- `main` - Docs only, protected
- `1n3ox`, `cat3ox`, `core-runtime` - Production code, PR required

---

## License

- CORE.3ox (Python) - Free/Open for testing
- RAW.3ox (Ruby) - Commercial license required
- Architecture - Open documentation

See individual branches for specific licensing.

---

## Status

**Production Ready:**
- ✅ core-runtime (.3ox agent runtime)

**In Development:**
- 🚧 1n3ox (input/output layer)
- 🚧 cat.3ox (category middleware)

**Experimental:**
- 🧪 experiments (testing branch)

---

**Built for:** Developers who need structured AI operations  
**Perfect for:** Regulated industries, compliance-heavy environments  
**Works with:** Any AI agent (Cursor, Claude, ChatGPT, custom)

**Version:** v1.1.0  
**Build:** ⧗-25.291

:: ∎
