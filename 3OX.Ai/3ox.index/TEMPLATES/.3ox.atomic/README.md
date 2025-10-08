# 🧬 Atomic `.3ox` Structure

**Version:** v1.0.0  
**Sirius Time:** ⧗-25.61  
**Purpose:** Minimal, modular backend for AI agent operation

---

## 📁 **Structure**

```
.3ox/
├── brain.rs          # Agent identity + rules (< 150 lines, Rust)
├── tools.rs          # Runtime toolset (< 200 lines, Rust)
├── runtime.rb        # Orchestration (< 250 lines, Ruby)
├── trace.log         # Event log (append-only, plain text)
└── README.md         # This file (human docs)
```

**Total:** ~600 lines of config, highly modular

---

## 🦀 **brain.rs** - Agent Identity

**Purpose:** Defines WHO the agent is and WHAT rules it follows

**Contains:**
- Agent configuration (name, brain type, model)
- Instructions (core directives)
- Rules (constraints & behaviors)
- Brain types: SENTINEL, ALCHEMIST, LIGHTHOUSE

**Language:** Rust (compiled, fast, type-safe)

**Example:**
```rust
pub const RVNX_BRAIN: AgentConfig = AgentConfig {
    name: "SENTINEL",
    brain: BrainType::Sentinel,
    model: "claude-sonnet-4",
    instructions: "Protect sync safety. Atomic ops only.",
    max_turns: 10,
};
```

---

## 🔧 **tools.rs** - Runtime Toolset

**Purpose:** Defines WHAT the agent can do

**Contains:**
- Tool registry (subset of global toolset)
- Tool implementations (actual execution code)
- Workspace-specific toolsets
- Version tracking

**Language:** Rust (runtime execution, type-safe)

**Example:**
```rust
pub enum Tool {
    FileValidator,
    ConflictResolver,
    GitPusher,
    ReceiptGenerator,
}

impl Tool {
    pub fn execute(&self, input: &str) -> Result<String> {
        match self {
            Tool::FileValidator => validate_file(input),
            // ...
        }
    }
}
```

**Changes Often:** Add new tools as capabilities expand

---

## 💎 **runtime.rb** - Orchestration

**Purpose:** Defines HOW the agent operates

**Contains:**
- Session management (context memory)
- Receipt system (SHA256 tracking)
- Router (handoff logic)
- Trace logger (event tracking)

**Language:** Ruby (dynamic, elegant orchestration)

**Modules:**
- `Session` - Conversation context
- `Receipt` - Cryptographic receipts
- `Router` - Handoff destinations
- `Trace` - Event logging

**Example:**
```ruby
# Session management
Session.init('workspace_001')
Session.add(:user, 'Sync this file')
Session.add(:agent, 'Validating...')

# Receipt generation
receipt = Receipt.generate(file, :intake)

# Routing
Router.handoff(:critical_error, { reason: 'Validation failed' })
```

---

## 📝 **trace.log** - Event Stream

**Purpose:** Records WHAT the agent did

**Format:**
```
[⧗-25.61.12:30] AGENT_START | SENTINEL | session_001
[⧗-25.61.12:30] TOOL_CALL | FileValidator | test.md | OK
[⧗-25.61.12:31] HANDOFF | CMD.BRIDGE | critical_error
[⧗-25.61.12:31] AGENT_END | success | duration=1.2s
```

**Append-only, never delete**

---

## 🔄 **How LLM Uses This**

1. **Load `brain.rs`** → Know identity & rules
2. **Load `tools.rs`** → Know capabilities
3. **Load `runtime.rb`** → Know orchestration
4. **Execute based on config**
5. **Log to `trace.log`**

**Context Usage:** ~600 lines for full config = lightweight!

---

## 🎯 **Workspace Configurations**

### RVNx.BASE (SENTINEL)
```
Brain: Guardian-Synchronizer
Tools: FileValidator, ConflictResolver, GitPusher
Rules: Atomic ops, last-write-wins, checksum validation
```

### SYNTH.BASE (ALCHEMIST)
```
Brain: Creator-Architect
Tools: DeployValidator, CloudManager, CostTracker
Rules: Dev→Staging→Prod, rollback ready, cost aware
```

### OBSIDIAN.BASE (LIGHTHOUSE)
```
Brain: Librarian-Weaver
Tools: LibraryCatalog, LinkValidator, MOCGenerator
Rules: Link integrity, semantic connections, MOCs for 10+
```

---

## 🚀 **Quick Edit Workflow**

### Add New Tool
```bash
# Edit tools.rs only
# Add enum variant + implementation
# Commit: "feat: add email summarizer tool"
```

### Tune Agent Behavior
```bash
# Edit brain.rs only
# Update instructions or rules
# Commit: "tune: increase sync caution"
```

### Update Routing
```bash
# Edit runtime.rb only
# Modify Router::ROUTES
# Commit: "fix: update emergency routing"
```

---

## 📊 **Modularity & Versioning**

| File | Changes | Version | Lines |
|------|---------|---------|-------|
| `brain.rs` | Rare | v1.0.x | 150 |
| `tools.rs` | Often | v2.x.x | 200 |
| `runtime.rb` | Rare | v1.x.x | 250 |

**Independent versioning per file!**

---

## ✅ **Deployment**

### Copy to Workspace
```bash
cp -r .3ox.atomic/ /path/to/workspace/.3ox/
cd /path/to/workspace/.3ox/
git init
git add .
git commit -m "init: atomic .3ox structure"
```

### Customize
```rust
// Edit brain.rs
pub const MY_BRAIN: AgentConfig = AgentConfig {
    name: "MyAgent",
    brain: BrainType::Sentinel,
    // ...
};
```

### Test
```bash
ruby runtime.rb  # Should create session, receipt, log
```

---

## 🔗 **Integration with 3OX.Ai**

```
3OX.Ai/.3ox.index/
├── toolset.global.rs       # Master tool registry
└── TEMPLATES/
    └── .3ox.atomic/        # This template

RVNx.BASE/.3ox/
├── brain.rs                # Imports from global
├── tools.rs                # Subset of global tools
├── runtime.rb              # Uses global receipts
└── trace.log
```

---

## 📚 **References**

- **Global Policy:** `3OX.Ai/.3ox.index/POLICY/`
- **Receipt System:** `!BASE.OPERATIONS/receipt_manager.rb`
- **Routing:** `!BASE.OPERATIONS/router.py`
- **OpenAI Agents SDK:** Inspired by agent/tool/session pattern

---

**Status:** ACTIVE  
**Authority:** Atomic .3ox Standard v1.0  
**Maintained by:** CMD.BRIDGE

