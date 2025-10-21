# CAT Brain Examples

This folder contains domain-specific brain configurations for each CAT category.

## What's Here

- **CAT.DOMAINS.md** - Full documentation of all 6 CAT brain configurations
- **CAT.1.SELF.brain.rs** - Personal development specialist brain
- **CAT.2.EDUCATION.brain.rs** - Learning & knowledge specialist brain
- **CAT.3.BUSINESS.brain.rs** - Professional & career specialist brain
- **CAT.4.FAMILY.brain.rs** - Family & relationships specialist brain
- **CAT.5.SOCIAL.brain.rs** - Social life & community specialist brain

## Usage

These are **reference examples** showing how each CAT category can be specialized for its domain.

### Default Setup

When you run `python setup.py`, it creates:
- **CAT.0 ADMIN** with `CAT.ROUTER` brain (master orchestrator)
- **CAT.1-5** with generic brains

### Customizing Your CATs

To make each CAT domain-aware:

1. **Copy the appropriate example:**
   ```bash
   cp BRAINS/CAT.1.SELF.brain.rs "../(CAT.1) Self/.3ox/brain.rs"
   ```

2. **Recompile the brain:**
   ```bash
   cd "../(CAT.1) Self/.3ox"
   rustc brain.rs -o brain.exe --edition 2021
   ```

3. **Verify:**
   ```bash
   ./brain.exe config
   ```

### Why Domain-Specific Brains?

**Generic CAT:**
- Doesn't know what content belongs in its category
- Can't make intelligent routing decisions
- Just validates and logs

**Domain-Specific CAT:**
- Knows exactly what content it handles
- Can recognize relevant files
- Understands its knowledge area
- Makes smarter routing decisions

## Example: CAT.1 SELF

**Before (generic):**
```rust
name: "CAT.ROUTER",
instructions: "Routes files to appropriate categories..."
```

**After (domain-specific):**
```rust
name: "CAT.1.SELF",
instructions: "Personal development specialist. Handles: health tracking, 
fitness goals, personal projects, self-reflection journals..."
```

Now CAT.1 **knows** it's responsible for personal development content!

---

**See CAT.DOMAINS.md for complete configuration details.**

:: ∎

