# CAT.3OX - Personal File Organization System

**A proven file organization framework for managing your digital life**

Version: 1.0  
Runtime: Ruby (RAW) or Python (CORE)

---

## What Is This?

CAT.3OX is a **file organization system** that automatically categorizes and tracks your files across 5 life domains. Drop files in category inboxes, and the system validates, logs, and routes them automatically.

Think of it as a **smart filing cabinet** with automatic tracking.

---

## How It Works

### The Basic Flow

```
1. You drop a file → (CAT.X) Category/1N.3OX/
2. Runtime processes it → .3ox/ validates & logs
3. Tracking happens → Shared output folder gets logs
4. You find it easily → Everything has a hash & timestamp
```

### What Makes It Different

- **No manual filing** - Drop files in the right category inbox and you're done
- **Automatic validation** - Every file gets a cryptographic hash for integrity
- **Centralized logging** - All activity logs to one place (3ox.log)
- **Simple structure** - Only 3 folders per category (inbox, runtime, logs)

---

## File Structure

### What You Actually Get

```
Your Workspace/
├── (CAT.1) Self/           ← Personal development files
│   ├── 1N.3OX/            ← Drop files here
│   └── .3ox/              ← Runtime (don't touch)
│
├── (CAT.2) Education/      ← Learning materials
│   ├── 1N.3OX/
│   └── .3ox/
│
├── (CAT.3) Business/       ← Work documents
│   ├── 1N.3OX/
│   └── .3ox/
│
├── (CAT.4) Family/         ← Photos, events, documents
│   ├── 1N.3OX/
│   └── .3ox/
│
├── (CAT.5) Social/         ← Resumes, volunteer work
│   ├── 1N.3OX/
│   └── .3ox/
│
└── !0UT.3OX/              ← Shared output (all logs go here)
    └── 3ox.log            ← Central activity log
```

### The 5 Life Categories

- **(CAT.1) Self** - Health tracking, personal development, self-assessment
- **(CAT.2) Education** - Courses, certifications, learning materials
- **(CAT.3) Business** - Work projects, business documents, contracts
- **(CAT.4) Family** - Photos, family events, important documents
- **(CAT.5) Social** - Resumes, volunteer work, community projects

**Customize:** Add your own categories beyond the default 5.

---

## Installation

### 1. Download

Download this repository and extract to your workspace folder.

### 2. Run Setup

```bash
cd CAT.3OX
python setup.py
```

This creates:
- 5 life domain categories (CAT.1-5)
- 1 master orchestrator (CAT.0 ADMIN)
- Shared output folder

### 3. Choose Runtime

**Option A: CORE (Python - Free)**
```bash
# Copy CORE runtime to each category
cp -r CORE/* "(CAT.1) Self/.3ox/"
cp -r CORE/* "(CAT.2) Education/.3ox/"
# ... repeat for all categories

# Install dependencies
pip install xxhash pyyaml
```

**Option B: RAW (Ruby - Requires License)**
```bash
# Copy RAW runtime to each category
cp -r RAW/* "(CAT.1) Self/.3ox/"
cp -r RAW/* "(CAT.2) Education/.3ox/"
# ... repeat for all categories

# Install dependencies
gem install xxhash

# Add license key to each .3ox/ folder
cp your-3ox.key "(CAT.1) Self/.3ox/"
# ... repeat for all categories
```

---

## Usage

### Daily Workflow

**1. Drop files in category inboxes:**
```
# Save a health tracking spreadsheet
→ Save to: (CAT.1) Self/1N.3OX/

# Download a course PDF
→ Save to: (CAT.2) Education/1N.3OX/

# Get a work contract
→ Save to: (CAT.3) Business/1N.3OX/
```

**2. Runtime validates automatically:**
- Generates cryptographic hash (xxHash64)
- Logs operation to 3ox.log
- Validates file integrity
- Tracks timestamp

**3. Check logs:**
```bash
# View all activity
cat !0UT.3OX/3ox.log

# See what was processed
tail -20 !0UT.3OX/3ox.log
```

### What Gets Logged

Every file operation logs:
```
[2025-10-20 18:30:45] 〘⟦⎊⟧・.°RUBY.RB〙
  Operation: knowledge_update
  Status: COMPLETE
  Details: File: document.pdf, Hash: a3f8d9e2c1b5
```

**Why this matters:**
- Find any file by hash
- Verify file integrity
- Track when files were added
- Audit trail for important documents

---

## Key Features

### ✓ File Integrity Validation
Every file gets a cryptographic hash. Know if files have been modified.

### ✓ Centralized Logging
All categories log to one place. See your entire digital life's activity in 3ox.log.

### ✓ No Receipt Spam
Unlike typical file management systems, CAT.3OX only logs to one file. No clutter.

### ✓ Flexible Categories
Start with 5 life domains, add as many custom categories as you need.

### ✓ Battle-Tested
15+ years of real-world use in production environments.

---

## Technical Details

### What's in .3ox/ Folder?

```
.3ox/
├── run.rb (or run.py)     ← Main runtime
├── brain.rs               ← Agent configuration
├── tools.yml              ← Available operations
├── routes.json            ← Output routing rules
├── limits.json            ← Resource constraints
└── 3ox.log                ← Local activity log
```

**Don't manually edit these files.** The runtime manages everything.

### Activation Keys (RAW version only)

The Ruby (RAW) runtime requires a license key:
```
3ox.key format:
- Machine-locked (tied to your computer)
- Cryptographically signed
- Validates on every runtime execution
```

**CORE version:** No license required, free forever.

---

## Troubleshooting

### "Activation key missing" error

RAW runtime requires `3ox.key` in each `.3ox/` folder.
- Use CORE runtime (Python) instead, or
- Purchase license at 3ox.store (coming soon)

### "No output folder found" warning

Create shared output folder:
```bash
mkdir !0UT.3OX
```

### Files not being processed

Check runtime:
```bash
cd "(CAT.1) Self/.3ox"
ruby run.rb    # or: python run.py
```

Look for error messages in output.

---

## Architecture Notes

### Why Two Runtimes?

- **CORE (Python)** - Free, testing, personal use
- **RAW (Ruby)** - Commercial, faster, compliance features

Both do the same job. Choose based on your needs.

### Why the Naming Convention?

- **1N.3OX** = Inbox (files come IN)
- **0UT.3OX** = Outbox (logs go OUT)
- **.3ox** = Runtime (processes files)
- **CAT** = Category (life domain)

The naming makes the data flow obvious.

---

## Contributing

This is a personal productivity system, not a collaborative platform. 

Fork it, modify it, make it yours. That's the point.

---

## License

**CORE Runtime:** MIT License (free forever)

**RAW Runtime:** Commercial license required (3ox.key)

---

## Support

Having issues? Check:
1. Did you run `setup.py`?
2. Is the runtime installed in each `.3ox/` folder?
3. Does `!0UT.3OX/` folder exist?
4. Can you run the runtime manually? (`ruby run.rb` or `python run.py`)

---

**Built for people who are tired of digital chaos.**

**Start organizing your life today.**
