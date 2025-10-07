# 📋 3OX TEMPLATES

**Purpose:** Standard templates for creating new stations and projects  
**Authority:** CORE  
**Usage:** CMD.BRIDGE uses these when initializing new entities

---

## 📂 AVAILABLE TEMPLATES

### STRATOS-1.STATION.RULES.template.md
**For:** Large mega-stations (RVNx, SYNTH, etc.)  
**Stratos Level:** 1  
**Complexity:** High - Comprehensive operational rules

**When to Use:**
- Creating a new major station/ecosystem
- 10+ sub-projects or critical infrastructure
- Multi-agent coordination required
- Complex resource management needed

**Usage:**
```bash
# Copy template to new station
cp STRATOS-1.STATION.RULES.template.md \
   ../../[STATION].BASE/![STATION].OPS/.3ox/STATION.RULES.md

# Replace all [STATION] and [PLACEHOLDER] markers
# Customize sections for station-specific needs
```

---

### STRATOS-2.STATION.RULES.template.md
**For:** Medium stations (OBSIDIAN, future stations)  
**Stratos Level:** 2  
**Complexity:** Medium - Standard operational rules

**When to Use:**
- Creating a new medium-scale station
- 3-10 sub-projects
- Focused domain operations
- Moderate complexity

**TODO:** Create this template (simplified version of STRATOS-1)

---

### STRATOS-3.PROJECT.BRAIN.template.md
**For:** Individual projects (SunsetGlow, Glyphbit, etc.)  
**Stratos Level:** 3  
**Complexity:** Low - Project-specific context

**When to Use:**
- Creating a new project within a station
- Single-purpose or bounded scope
- Needs project-specific context for AI
- Inherits most rules from parent station

**Usage:**
```bash
# Copy template to new project
cp STRATOS-3.PROJECT.BRAIN.template.md \
   ../../[STATION].BASE/[PROJECT]/.3ox/PROJECT.BRAIN.md

# Replace all [PROJECT] and [PLACEHOLDER] markers
# Fill in project-specific details
```

---

## 🔧 TEMPLATE USAGE WORKFLOW

### For CMD.BRIDGE Creating New Station:

```yaml
1. Determine stratos level (use algorithm in STRATOS.RULES.MATRIX.md)

2. Create folder structure:
   [STATION].BASE/
   ├── ![STATION].OPS/
   │   └── .3ox/
   └── !1N.3OX [STATION].BASE/
       └── .3ox.AI.BRAIN/

3. Copy appropriate template:
   - STRATOS-1 → STRATOS-1.STATION.RULES.template.md
   - STRATOS-2 → STRATOS-2.STATION.RULES.template.md

4. Search and replace:
   [STATION] → Actual station name
   [CURRENT] → Current Sirius time
   [PLACEHOLDER] → Actual values

5. Customize sections:
   - Mission and scope
   - Domain-specific policies
   - Resource limits
   - Operational protocols

6. Register in CMD.STATIONS/REGISTRY.yaml

7. Create AI.THINKING.PROMPT.md (station brain)

8. Test 1N/0UT communication

9. Activate monitoring
```

---

### For Station OPS Creating New Project:

```yaml
1. Determine if project needs STRATOS-3 or STRATOS-4
   - If STRATOS-4 (micro), skip .3ox folder entirely
   - If STRATOS-3 (project), continue:

2. Create .3ox folder in project root:
   [PROJECT]/.3ox/

3. Copy PROJECT.BRAIN template:
   cp STRATOS-3.PROJECT.BRAIN.template.md \
      [PROJECT]/.3ox/PROJECT.BRAIN.md

4. Fill in all sections:
   - Mission and scope
   - Technology stack
   - Current phase
   - Success criteria
   - Agent instructions

5. Link to parent station (automatic via file path)

6. Configure 0UT reporting (on-event basis)

7. Notify CMD.BRIDGE via 0UT (new project created)
```

---

## 🎯 PLACEHOLDER REFERENCE

All templates use these placeholders that must be replaced:

### Required Replacements:
- `[STATION]` → Station name (SYNTH, RVNx, OBSIDIAN, etc.)
- `[PROJECT]` → Project name (SunsetGlow, Glyphbit, etc.)
- `[CURRENT]` → Current Sirius time (⧗-YY.DD)
- `[START_DATE]` → Project start date in Sirius time
- `[TARGET_DATE]` → Target completion date (if applicable)

### Context-Specific:
- `[Brief description]` → 1-2 sentence description
- `[Location]` → File path or folder location
- `[Purpose]` → Why this component exists
- `[Agent name]` → Name of AI agent (if any)
- `[PLACEHOLDER]` → Generic marker for any custom value

---

## ✅ TEMPLATE VALIDATION

After creating a new station/project from template, verify:

### For STRATOS-1 Station:
- [ ] All [STATION] placeholders replaced
- [ ] Mission and scope defined
- [ ] All 6 required rule files created
- [ ] Error escalation levels (L1-L5) defined
- [ ] Resource limits specified
- [ ] Health check interval set (≤15min)
- [ ] 0UT reporting configured
- [ ] Registered in CMD.STATIONS

### For STRATOS-3 Project:
- [ ] All [PROJECT] placeholders replaced
- [ ] Mission and success criteria defined
- [ ] Current phase specified
- [ ] Parent station identified
- [ ] Key files/structure documented
- [ ] Agent instructions clear
- [ ] 0UT reporting configured (on-event)

---

## 🔄 TEMPLATE EVOLUTION

Templates should be updated when:
- New best practices emerge
- Global policy changes
- System architecture evolves
- Feedback from station/project creation

**Update Process:**
1. CMD.BRIDGE identifies improvement need
2. Updates template in CORE/TEMPLATES/
3. Logs change in Captain's Log
4. Optionally updates existing stations/projects (if breaking change)

---

## 📚 ADDITIONAL RESOURCES

- `GENESIS.SYSTEM.ARCHITECTURE.md` - Overall system design
- `STRATOS.RULES.MATRIX.md` - Detailed stratos specifications
- `MASTER.ROUTING.BRAIN.md` - How brains route and activate

---

**Maintained By:** CMD.BRIDGE  
**Last Updated:** ⧗-25.60  
**Status:** ACTIVE

