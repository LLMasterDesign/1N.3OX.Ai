# RAW.3ox Setup Guide
**Ruby Runtime** - Commercial/Production Version  
**License Required** 🔒

---

## Prerequisites

**You should have received:**
1. ✅ RAW.3ox folder (all files)
2. ✅ License key file (`3ox.key`) **← MUST BE PROVIDED BY VENDOR**
3. ✅ Invoice/receipt confirming purchase

**⚠️ IMPORTANT:** License keys CANNOT be generated locally. They are cryptographically signed by the vendor and machine-bound for security. If you downloaded this from GitHub without purchasing, you MUST contact sales@3ox.ai to obtain a valid license key.

**If you're missing any of these, contact:** license@3ox.ai

---

## Installation (5 minutes)

### Step 1: Install Ruby

**Windows:**
```bash
winget install RubyInstallerTeam.RubyWithDevKit.3.2
```

**Mac:**
```bash
brew install ruby
```

**Linux:**
```bash
sudo apt install ruby-full
```

**Verify:**
```bash
ruby --version
# Should show: ruby 3.2.0 or higher
```

---

### Step 2: Install Dependencies
```bash
gem install xxhash
```

**Expected output:**
```
Successfully installed xxhash-0.x.x
1 gem installed
```

---

### Step 3: Place Your License Key

**IMPORTANT:** You should have received a `3ox.key` file from us.

**Place it in the RAW.3ox folder:**
```
RAW.3ox/
├── run.rb
├── brain.exe
├── 3ox.key  ← PUT YOUR KEY HERE
└── ... other files
```

**Example key file structure:**
```
STATUS: ACTIVATED
EXPIRES: 2026-12-31
MACHINE_ID: 23ad0ab7565592cb
LICENSED_TO: Your Company Name

=== SECURITY ===
SIGNATURE: a1b2c3d4e5f6...
```

---

### Step 4: Test Your Installation
```bash
ruby run.rb knowledge_update
```

**Expected output:**
```
🔓 ACTIVATION KEY VERIFIED
━━━━━━━━━━━━━━━━━━━━━━
Agent: GUARDIAN
Runtime: ruby
Status: UNLOCKED
━━━━━━━━━━━━━━━━━━━━━━

✓ Brain: GUARDIAN (Sentinel)
✓ Tools loaded: 4 available
✓ File validated
✓ Receipt generated
✓ Routed to: OBSIDIAN.BASE
```

---

## License Key Issues?

### "ACTIVATION KEY MISSING"
**Problem:** No `3ox.key` file found  
**Solution:** 
1. Check you placed the key in RAW.3ox/ folder
2. File must be named exactly: `3ox.key`
3. Contact license@3ox.ai if you didn't receive a key

### "MACHINE ID MISMATCH"
**Problem:** Key was generated for a different computer  
**Solution:**
1. Get your current machine ID: `ruby run.rb --machine-id`
2. Email us: license@3ox.ai with:
   - Your invoice number
   - Old machine ID (if known)
   - New machine ID
3. We'll generate a new key (1 business day)

**License Transfer Policy:** 1 free transfer per year

### "LICENSE EXPIRED"
**Problem:** Key expiration date has passed  
**Solution:**
- Contact sales@3ox.ai to renew
- Or purchase new license

### "KEY SIGNATURE INVALID"
**Problem:** Key file has been modified or corrupted  
**Solution:**
- Request fresh key: license@3ox.ai
- Do NOT edit the key file manually

---

## Usage

### Single Operation
```bash
ruby run.rb knowledge_update
```

### Batch Operations (FAST! ⚡)
```bash
ruby run.rb critical_error deploy_ready sync_request
# 3 operations in ~2.2 seconds!
```

### Check Machine ID
```bash
ruby run.rb --machine-id
# Shows: Current Machine ID: 23ad0ab7565592cb
```

---

## Configuration Files

**Same as CORE.3ox, but optimized:**

### routes.json
```json
{
  "routes": {
    "knowledge_update": "OBSIDIAN.BASE",
    "critical_error": "CMD.BRIDGE"
  }
}
```

### limits.json (faster than TOML!)
```json
{
  "files": {
    "max_size": 104857600
  }
}
```

### tools.yml
```yaml
tools:
  - name: file_validation
    enabled: true
```

---

## Advanced Features

### Surgical Editing (Included)
Edit specific line ranges without exposing full file:
```bash
ruby surgical_edit.rb demo contract.txt
# Edits only lines 30-45
# Rest of file never exposed
```

### Compliance Testing (Included)
Verify offline operation and HIPAA/GDPR compliance:
```bash
ruby compliance_test.rb
# Checks: 0 network calls
# Result: 100% offline verified
```

---

## Performance

**Batch mode is your friend:**

```bash
# SLOW (13 seconds)
ruby run.rb op1
ruby run.rb op2  
ruby run.rb op3

# FAST (2.2 seconds) ⚡
ruby run.rb op1 op2 op3
```

**Why?** Single process startup vs 3 separate ones.

---

## Support

**Technical Issues:**  
📧 support@3ox.ai  
⏱ Response time: 24 hours

**License Issues:**  
📧 license@3ox.ai  
⏱ Response time: 1 business day

**Sales/Upgrades:**  
📧 sales@3ox.ai

**Emergency Support:**  
📧 emergency@3ox.ai (Enterprise customers only)

---

## Compliance Documentation

**Included in your package:**
- HIPAA compliance statement
- GDPR compliance statement  
- SOC 2 audit evidence
- Cryptographic receipt format
- Data minimization white paper

**Location:** `docs/` folder (if included) or contact support@3ox.ai

---

## License Terms

**Your license includes:**
- ✅ Use on ONE machine (specified in key)
- ✅ Lifetime updates (for your license version)
- ✅ Technical support (email)
- ✅ 1 free machine transfer per year

**Prohibited:**
- ❌ Sharing license keys
- ❌ Multi-machine use (without multi-license)
- ❌ Editing/tampering with key file
- ❌ Reverse engineering
- ❌ Redistribution

**Violations result in:**
- License revocation (no refund)
- Legal action if commercial damage

---

## Upgrading

**From CORE.3ox (Python)?**

Good news! Config files are compatible:
1. Copy your `routes.json`, `tools.yml` from CORE.3ox
2. Convert `limits.toml` → `limits.json` (if needed)
3. Place your `3ox.key`
4. Run!

**To Enterprise License?**

Contact sales@3ox.ai for:
- Unlimited machine deployment
- Priority support
- Custom integrations
- Volume discounts

---

## Version Info

**Current Version:** v1.1.0  
**Build:** ⧗-25.291  
**Runtime:** Ruby 3.2+  
**Brain:** Compiled Rust binary (included)

---

**Thank you for your purchase!** 💎

Questions? → support@3ox.ai

:: ∎

