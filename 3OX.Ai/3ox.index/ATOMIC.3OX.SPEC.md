# 🧬 ATOMIC .3OX SPECIFICATION

**Version:** v1.0.0  
**Sirius Time:** ⧗-25.61  
**Authority:** Core Architecture Standard

---

## 🎯 **Purpose**

Define the minimal, modular backend structure for every `.3ox` brain in the 3OX.Ai system.

**Design Goals:**
- ⚡ Minimal token usage (< 600 lines total config)
- 🦀 Type-safe execution (Rust for runtime)
- 💎 Elegant orchestration (Ruby for flow)
- 🔄 Independent versioning per component
- 📖 Human-readable when needed

---

## 📁 **Atomic Structure**

```
.3ox/
├── brain.rs          # Agent identity + rules (Rust, < 150 lines)
├── tools.rs          # Runtime toolset (Rust, < 200 lines, evolves)
├── runtime.rb        # Orchestration (Ruby, < 250 lines)
├── trace.log         # Event log (plain text, append-only)
└── README.md         # Human docs (optional)
```

**Total:** ~600 lines of active config

---

## 🦀 **brain.rs** - Agent Identity

### Purpose
Defines WHO the agent is and HOW it behaves

### Contents
- `AgentConfig` - Name, brain type, model, instructions
- `BrainType` - SENTINEL | ALCHEMIST | LIGHTHOUSE
- `Rule` - Behavior constraints and validation rules

### Language Choice
**Rust** because:
- Compiled (fast loading, zero runtime overhead)
- Type-safe (catches config errors at compile time)
- Memory-safe (no crashes from bad config)
- Stable (rarely changes once set)

### Example
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

### Purpose
Defines WHAT the agent can do (capabilities)

### Contents
- `Tool` enum - Available tools (subset of global registry)
- Tool implementations - Actual execution code
- Workspace-specific toolsets - RVNx, SYNTH, OBSIDIAN configs
- Version tracking - Independent tool versioning

### Language Choice
**Rust** because:
- Runtime execution (needs to be fast)
- Type-safe function signatures (prevents errors)
- Compiled (instant loading, no parsing)
- Changes often (tools added frequently, needs fast recompile)

### Global vs Local
```
3OX.Ai/.3ox.index/toolset.global.rs    # Master registry (all tools)
RVNx.BASE/.3ox/tools.rs                # Subset (only needed tools)
```

### Example
```rust
pub const RVNX_TOOLS: &[Tool] = &[
    Tool::FileValidator,
    Tool::ConflictResolver,
    Tool::GitPusher,
];
```

---

## 💎 **runtime.rb** - Orchestration

### Purpose
Defines HOW the agent operates (flow control)

### Contents
- `Session` - Context memory management
- `Receipt` - SHA256 receipt generation/validation
- `Router` - Handoff routing logic
- `Trace` - Event logging

### Language Choice
**Ruby** because:
- Dynamic orchestration (flexible routing)
- Elegant DSL (readable flow control)
- Integration with existing `receipt_manager.rb`
- Stable (orchestration logic rarely changes)

### Modules
```ruby
Session.init('workspace_001')     # Start session
Receipt.generate(file, :intake)   # Generate receipt
Router.handoff(:critical_error)   # Route to destination
Trace.log('EVENT', { data })      # Log event
```

---

## 📝 **trace.log** - Event Stream

### Purpose
Records WHAT the agent did (audit trail)

### Format
```
[⧗-25.61.12:30] AGENT_START | SENTINEL | session_001
[⧗-25.61.12:30] TOOL_CALL | FileValidator | test.md | OK
[⧗-25.61.12:31] HANDOFF | CMD.BRIDGE | critical_error
[⧗-25.61.12:31] AGENT_END | success | duration=1.2s
```

### Characteristics
- Plain text (universal, greppable)
- Append-only (never delete, audit trail)
- Sirius timestamps (cosmic alignment)
- Structured (easy parsing if needed)

---

## 🎯 **Brain Types**

### SENTINEL (Guardian-Synchronizer)
```yaml
Station: RVNx.BASE
Focus: Sync safety, data integrity, remote access
Thinking: Safety-first, protective, atomic operations
Tools: FileValidator, ConflictResolver, GitPusher
Rules: Atomic ops only, last-write-wins, checksum validation
```

### ALCHEMIST (Creator-Architect)
```yaml
Station: SYNTH.BASE
Focus: Rapid prototyping, deployment, creative synthesis
Thinking: Experimental, fast iteration, ship to learn
Tools: DeployValidator, CloudManager, CostTracker
Rules: Dev→Staging→Prod, rollback ready, cloud cost aware
```

### LIGHTHOUSE (Librarian-Weaver)
```yaml
Station: OBSIDIAN.BASE
Focus: Knowledge management, PKM, semantic connections
Thinking: Connected, semantic, graph-oriented
Tools: LibraryCatalog, LinkValidator, MOCGenerator
Rules: Link integrity checks, bidirectional links, MOCs for 10+
```

---

## 🔄 **LLM Consumption Pattern**

```
1. Agent starts
   ↓
2. Load .cursorrules (root-level config)
   ↓
3. .cursorrules → "Check .3ox/ for your config"
   ↓
4. Load brain.rs (~150 lines) → "I am SENTINEL"
   ↓
5. Load tools.rs (~200 lines) → "I can validate, sync, push"
   ↓
6. Load runtime.rb (~250 lines) → "I orchestrate via Session/Router/Receipt"
   ↓
7. User input: "Sync this file"
   ↓
8. Execute: Tool::FileValidator
   ↓
9. Log: trace.log
   ↓
10. Route: Router.handoff() if needed
```

**Total context:** ~600 lines for full capability map

---

## 📊 **Token Efficiency**

| Structure | Files | Lines | Tokens (est) | Context Left |
|-----------|-------|-------|--------------|--------------|
| **Old (verbose YAML)** | 8+ | ~1500 | ~4500 | Low |
| **Atomic (Rust/Ruby)** | 4 | ~600 | ~1800 | **High!** |

**Savings:** 60% reduction = more room for actual work

---

## 🚀 **Version Management**

Each file has independent versioning:

```
brain.rs    v1.0.x    (stable, rarely changes)
tools.rs    v2.x.x    (evolves, tools added frequently)
runtime.rb  v1.x.x    (stable, orchestration logic set)
```

### Example Git History
```
commit abc123: feat(tools): add EmailSummarizer v2.3.0
  Modified: tools.rs only

commit def456: tune(brain): increase sync caution v1.0.1
  Modified: brain.rs only

commit ghi789: fix(runtime): emergency routing v1.1.0
  Modified: runtime.rb only
```

**Clean diffs, targeted changes!**

---

## 🔧 **Quick Edit Workflow**

### Scenario 1: Add New Tool
```bash
User: "Add email summarizer tool"

AI edits: .3ox/tools.rs
Changes: +15 lines (new enum + impl)
Commit: "feat(tools): add EmailSummarizer"
Version: tools.rs v2.3.0 → v2.4.0
```

### Scenario 2: Tune Behavior
```bash
User: "Be more cautious with syncs"

AI edits: .3ox/brain.rs
Changes: ~5 lines (update instructions)
Commit: "tune(brain): increase caution"
Version: brain.rs v1.0.0 → v1.0.1
```

### Scenario 3: Update Routing
```bash
User: "Critical errors go to new emergency channel"

AI edits: .3ox/runtime.rb
Changes: ~3 lines (Router::ROUTES)
Commit: "fix(runtime): update emergency routing"
Version: runtime.rb v1.1.0 → v1.1.1
```

---

## 📦 **Deployment**

### Template Location
```
3OX.Ai/3ox.index/TEMPLATES/.3ox.atomic/
├── brain.rs
├── tools.rs
├── runtime.rb
└── README.md
```

### Deploy to R:// Drive
```bash
# Copy atomic structure to R:// stations
cp -r 3OX.Ai/3ox.index/TEMPLATES/.3ox.atomic/ R:/RVNx.BASE/.3ox/
cp -r 3OX.Ai/3ox.index/TEMPLATES/.3ox.atomic/ R:/SYNTH.BASE/.3ox/
cp -r 3OX.Ai/3ox.index/TEMPLATES/.3ox.atomic/ R:/OBSIDIAN.BASE/.3ox/
```

### Initialize Git
```bash
cd R:/RVNx.BASE/.3ox/
git init
git add .
git commit -m "init: atomic .3ox brain v1.0.0"
```

### Customize per Station
```rust
// R:/RVNx.BASE/.3ox/brain.rs
pub const BRAIN: AgentConfig = RVNX_BRAIN;  // Use SENTINEL preset

// R:/SYNTH.BASE/.3ox/brain.rs
pub const BRAIN: AgentConfig = SYNTH_BRAIN;  // Use ALCHEMIST preset
```

---

## 🔗 **Integration Points**

### Global Toolset
```
3OX.Ai/.3ox.index/toolset.global.rs    # Master tool registry
    ↓ (imports subset)
Station/.3ox/tools.rs                  # Local toolset
```

### Receipt System
```
!BASE.OPERATIONS/receipt_manager.rb    # Global receipt handler
    ↓ (used by)
Station/.3ox/runtime.rb                # Local Receipt module
```

### Routing
```
!BASE.OPERATIONS/router.py             # Global router
    ↓ (config in)
Station/.3ox/runtime.rb                # Local Router module
```

---

## ✅ **Validation**

### Compile Check
```bash
# Rust files must compile
rustc --crate-type lib brain.rs
rustc --crate-type lib tools.rs
```

### Runtime Check
```bash
# Ruby runtime must execute
ruby runtime.rb
# Should output: "✅ Runtime test complete!"
```

### Integration Check
```bash
# Full system test
cd Station/.3ox/
cargo build --release  # Compile Rust
ruby runtime.rb        # Test orchestration
cat trace.log          # Verify logging
```

---

## 🏆 **Success Criteria**

- ✅ Total config < 600 lines
- ✅ Rust compiles without errors
- ✅ Ruby executes without errors
- ✅ All 3 brain types supported
- ✅ Tools independently versionable
- ✅ LLM can load in < 1800 tokens
- ✅ Human-readable structure
- ✅ Git-friendly diffs
- ✅ Modular and scalable

---

## 📚 **References**

- **OpenAI Agents SDK:** Inspired agent/tool/session pattern
- **Global Policy:** `3OX.Ai/.3ox.index/POLICY/`
- **Receipt System:** `!BASE.OPERATIONS/RECEIPT.SYSTEM.MANUAL.md`
- **V10SL Spec:** `!BASE.OPERATIONS/V10SL.SPECIFICATION.md`

---

**Status:** ACTIVE  
**Authority:** Core Architecture Standard  
**Maintained by:** CMD.BRIDGE  
**Version:** v1.0.0 (⧗-25.61)

