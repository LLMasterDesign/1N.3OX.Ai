# .3ox - Master Infrastructure

**This folder contains shared infrastructure for all 3OX.Set boxes.**

## Structure

```
.3ox/
├── POLICY/     → Rust laws (compiled, immutable)
├── CORE/       → AI thinking brains (ecosystem-specific)
└── OPS/        → Operations (3 levels)
    ├── L1/     → Simple operations
    ├── L2/     → Smart operations
    └── L3/     → Intelligent operations
```

## Reference Locations

**Global Policy:** `!BASE.OPERATIONS/GLOBAL.POLICY/.3ox/`  
**Ecosystem Brains:**
- OBSIDIAN: `OBSIDIAN.BASE/!1N.3OX OBSIDIAN.BASE/.3ox.AI.BRAIN/`
- RVNx: `RVNx.BASE/!1N.3OX RVNX.BASE/.3ox.AI.BRAIN/`
- SYNTH: `SYNTH.BASE/!1N.3OX SYNTH.BASE/.3ox.AI.BRAIN/`

## How It Works

Individual `3OX.Set/` boxes **plug into** this infrastructure:
- Boxes define WHAT to do (.3ox.key, .3ox.config, .3ox.run)
- Infrastructure defines HOW (POLICY, CORE, OPS)

**Version:** V1.0  
**Date:** ⧗-25.58

