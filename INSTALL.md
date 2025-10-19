# CAT.3OX Installation Guide

**Version:** 1.0  
**Time to install:** 2 minutes

---

## Quick Start

### Step 1: Download
Download `CAT.3OX` folder (this entire folder)

### Step 2: Run Setup
```bash
cd CAT.3OX
python setup.py
```

**This creates:**
- 5 Life Domain categories (CAT.1-5)
- 1 Master Orchestrator (CAT.0 ADMIN) 🎭

---

## What You Get

### The 5 Life Domains
```
(CAT.1) Self/          - Personal development, health
├── 1N.3OX/            - Drop files here
└── .3ox/              - Runtime processes them
    └── 0UT.3OX/       - Receipts & logs

(CAT.2) Education/     - Learning, courses
(CAT.3) Business/      - Work, projects  
(CAT.4) Family/        - Photos, events
(CAT.5) Social/        - Resumes, social
```

### The Grand Finale: CAT.0 ADMIN
```
(CAT.0) ADMIN/
├── (NO 1N.3OX - nothing enters from outside)
└── .3ox/              - Master orchestration
    └── 0UT.3OX/       - All receipts collect here
```

**ADMIN conducts the symphony of all other categories.**

---

## Step 3: Choose Your Runtime

### Option A: CORE (Python - Free)
**For testing and personal use**

```bash
# Copy CORE runtime to each category
cd CAT.3OX
cp -r CORE/* "(CAT.1) Self/.3ox/"
cp -r CORE/* "(CAT.2) Education/.3ox/"
cp -r CORE/* "(CAT.3) Business/.3ox/"
cp -r CORE/* "(CAT.4) Family/.3ox/"
cp -r CORE/* "(CAT.5) Social/.3ox/"
cp -r CORE/* "(CAT.0) ADMIN/.3ox/"

# Install Python dependencies
pip install xxhash toml pyyaml tiktoken
```

### Option B: RAW (Ruby - Commercial)
**For production and compliance**

```bash
# Copy RAW runtime to each category
cd CAT.3OX
cp -r RAW/* "(CAT.1) Self/.3ox/"
cp -r RAW/* "(CAT.2) Education/.3ox/"
cp -r RAW/* "(CAT.3) Business/.3ox/"
cp -r RAW/* "(CAT.4) Family/.3ox/"
cp -r RAW/* "(CAT.5) Social/.3ox/"
cp -r RAW/* "(CAT.0) ADMIN/.3ox/"

# Install Ruby dependencies
gem install xxhash tiktoken_ruby
```

**Note:** RAW version requires a license key in each `.3ox/` folder

---

## Step 4: Use ADMIN Tools

**View dashboard:**
```bash
python ADMIN/cat-router.py dashboard
# or
ruby ADMIN/cat-router.rb dashboard
```

**Track activity:**
```bash
python ADMIN/cat-trace.py report
# or
ruby ADMIN/cat-trace.rb report
```

---

## That's It!

**Drop files in 1N.3OX/ folders → CAT.0 ADMIN orchestrates everything**

---

## Want More Categories?

After initial setup, create custom categories:

**Coming soon:** 3oxmaker script to create perfectly formatted categories

**Manual creation:**
```bash
mkdir "(CAT.6) YourCategory"
mkdir "(CAT.6) YourCategory/.3ox"
mkdir "(CAT.6) YourCategory/.3ox/0UT.3OX"
mkdir "(CAT.6) YourCategory/1N.3OX"
```

Then copy CORE or RAW runtime into `.3ox/`

---

## Support

Email: support@3ox.store  
Docs: 3ox.store/docs/cat3ox

---

**Build:** ⧗-25.291

:: ∎
