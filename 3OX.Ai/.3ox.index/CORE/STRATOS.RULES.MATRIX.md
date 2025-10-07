///▙▖▙▖▞▞▙▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂
▛//▞▞ ⟦⎊⟧ :: ⧗-25.60 // STRATOS.RULES.MATRIX ▞▞
▞//▞ Stratos.Rules :: ρ{scale.classification}.φ{CORE}.τ{Rules.Matrix}.λ{specification} ⫸
▙⌱[📊] ≔ [⊢{stratos}⇨{classify}⟿{apply.rules}▷{operation}]
〔stratos.classification.rules〕 :: ∎

# 📊 STRATOS RULES MATRIX

**Authority Level:** CORE  
**Version:** 1.0  
**Purpose:** Define scale-specific operational rules for all Atlas.Legacy entities

---

## 🎯 OVERVIEW

Different scales require different rules. This matrix defines:
- What rules each stratos MUST have
- What rules are optional
- Reporting requirements
- Operational guidelines

---

## 🌊 STRATOS-1: MEGA STATION

### Classification Criteria:
- **Scale:** 10+ active sub-projects or complex infrastructure
- **Team:** Multi-agent coordination required
- **Strategic:** Mission-critical to entire system
- **Examples:** RVNx.BASE, SYNTH.BASE

### Required Files:
```
[STATION].BASE/
├── ![STATION].OPS/
│   └── .3ox/
│       ├── STATION.RULES.md ✅ REQUIRED
│       ├── OPS.PROTOCOLS.md ✅ REQUIRED
│       ├── ERROR.ESCALATION.md ✅ REQUIRED
│       ├── RESOURCE.MANAGEMENT.md ✅ REQUIRED
│       ├── COORDINATION.RULES.md ✅ REQUIRED
│       └── MONITORING.CONFIG.yaml ✅ REQUIRED
└── !1N.3OX [STATION]/
    └── .3ox.AI.BRAIN/
        └── AI.THINKING.PROMPT.md ✅ REQUIRED
```

### Operational Rules:

#### STATION.RULES.md Must Define:
- Station mission and scope
- Operational boundaries
- Integration points with other stations
- Domain-specific policies
- Performance standards

#### OPS.PROTOCOLS.md Must Define:
- Startup/shutdown procedures
- Health check intervals (recommended: every 5-15 min)
- Deployment processes
- Backup and recovery procedures
- Maintenance windows

#### ERROR.ESCALATION.md Must Define:
- Error severity levels (L1-L5)
- Automatic responses per level
- Escalation thresholds
- Who gets notified when
- Recovery procedures

#### RESOURCE.MANAGEMENT.md Must Define:
- Compute resource limits
- Storage allocation
- Network usage policies
- Cost monitoring (if cloud-based)
- Scaling rules (when to expand/contract)

#### COORDINATION.RULES.md Must Define:
- How sub-projects communicate
- Conflict resolution between agents
- Shared resource protocols
- Inter-project dependencies
- Lock/mutex handling

### Reporting Requirements:
```yaml
frequency:
  health_check: "every 15 minutes"
  status_summary: "hourly"
  daily_report: "end of day (local time)"
  incident_alert: "immediate (real-time)"

content:
  health:
    - system_status
    - active_processes
    - resource_usage
    - error_counts
  status:
    - completed_operations
    - in_progress_work
    - queue_depth
    - performance_metrics
  incidents:
    - error_details
    - impact_assessment
    - mitigation_actions
    - requires_cmd_intervention
```

### 0UT.3OX Format:
```yaml
header:
  stratos: "STRATOS-1"
  station: "[STATION_NAME]"
  timestamp: "⧗-25.60"
  type: "health|status|incident"

payload:
  # Detailed metrics and data
  
routing:
  priority: "high"
  destination: "CMD.BRIDGE/OPS/MONITOR/STRATOS-1/"
```

---

## 🏛️ STRATOS-2: STATION

### Classification Criteria:
- **Scale:** 3-10 active sub-projects
- **Team:** Single or few coordinating agents
- **Strategic:** Important but more contained
- **Examples:** OBSIDIAN.BASE

### Required Files:
```
[STATION].BASE/
├── ![STATION].OPS/
│   └── .3ox/
│       ├── STATION.RULES.md ✅ REQUIRED
│       ├── OPS.PROTOCOLS.md ✅ REQUIRED
│       └── ERROR.HANDLING.md ✅ REQUIRED
└── !1N.3OX [STATION]/
    └── .3ox.AI.BRAIN/
        └── AI.THINKING.PROMPT.md ✅ REQUIRED
```

### Optional Files:
- `RESOURCE.MANAGEMENT.md` (if needed)
- `COORDINATION.RULES.md` (if multi-agent)

### Operational Rules:

#### STATION.RULES.md Must Define:
- Station mission and scope
- Operational boundaries
- Domain-specific policies
- Performance standards

#### OPS.PROTOCOLS.md Must Define:
- Startup/shutdown procedures
- Health check intervals (recommended: every 30-60 min)
- Basic maintenance procedures

#### ERROR.HANDLING.md Must Define:
- Error severity levels (L1-L3)
- Automatic responses
- When to escalate to CMD.BRIDGE

### Reporting Requirements:
```yaml
frequency:
  health_check: "every 4 hours"
  daily_report: "end of day"
  incident_alert: "immediate"

content:
  health:
    - system_status
    - error_counts
  daily:
    - completed_work
    - any_issues
  incidents:
    - error_details
    - needs_help
```

### 0UT.3OX Format:
```yaml
header:
  stratos: "STRATOS-2"
  station: "[STATION_NAME]"
  timestamp: "⧗-25.60"
  type: "health|daily|incident"

payload:
  # Standard metrics
  
routing:
  priority: "normal"
  destination: "CMD.BRIDGE/OPS/MONITOR/STRATOS-2/"
```

---

## 🤖 STRATOS-3: PROJECT

### Classification Criteria:
- **Scale:** Single project or focused tool
- **Team:** One worker agent (or small team)
- **Strategic:** Tactical importance, part of larger strategy
- **Examples:** SunsetGlow, Glyphbit, TP.Gen

### Required Files:
```
Project/
└── .3ox/
    ├── PROJECT.BRAIN.md ✅ REQUIRED
    └── project.state.yaml ⚙️ AUTO-GENERATED
```

### Optional Files:
- `custom.rules.md` (if project needs specific policies)
- `error.config.yaml` (if custom error handling needed)

### Operational Rules:

#### PROJECT.BRAIN.md Must Define:
- Project purpose and goals
- Current phase/status
- Key files and structure
- Special considerations
- Success criteria

**Note:** Most operational rules are inherited from parent station.

### Reporting Requirements:
```yaml
frequency:
  on_completion: "when task done"
  on_error: "immediate"
  status_check: "optional (can be requested)"

content:
  completion:
    - what_was_done
    - outcomes
    - any_issues
    - next_steps
  error:
    - what_failed
    - error_details
    - attempted_fixes
```

### 0UT.3OX Format:
```yaml
header:
  stratos: "STRATOS-3"
  station: "[PARENT_STATION]"
  project: "[PROJECT_NAME]"
  timestamp: "⧗-25.60"
  type: "completion|error"

payload:
  # Event-specific data
  
routing:
  priority: "normal"
  destination: "CMD.BRIDGE/OPS/PROJECTS/"
```

---

## 🔧 STRATOS-4: MICRO

### Classification Criteria:
- **Scale:** Single script/tool, minimal state
- **Team:** No dedicated agent
- **Strategic:** Tactical utility
- **Examples:** Helper scripts, one-off tools

### Required Files:
- None (inherits everything)

### Optional Files:
```
Script/
└── .3ox/
    └── micro.config.yaml ⚙️ OPTIONAL
```

### Operational Rules:
- Inherits ALL rules from parent project/station
- No custom rules needed

### Reporting Requirements:
```yaml
frequency:
  on_error: "optional"
  
content:
  error:
    - basic_error_info
```

### 0UT.3OX Format:
```yaml
# Minimal format, only if error
header:
  stratos: "STRATOS-4"
  parent: "[PARENT]"
  timestamp: "⧗-25.60"
  type: "error"

payload:
  error: "description"
```

---

## 📊 STRATOS COMPARISON MATRIX

| Feature | STRATOS-1 | STRATOS-2 | STRATOS-3 | STRATOS-4 |
|---------|-----------|-----------|-----------|-----------|
| **Station Rules** | ✅ Required | ✅ Required | ⬜ Inherits | ⬜ Inherits |
| **OPS Protocols** | ✅ Required | ✅ Required | ⬜ Inherits | ⬜ Inherits |
| **Error Handling** | ✅ Detailed | ✅ Standard | ⬜ Basic | ⬜ Inherited |
| **Resource Mgmt** | ✅ Required | ⚠️ Optional | ⬜ N/A | ⬜ N/A |
| **Coordination** | ✅ Required | ⚠️ Optional | ⬜ N/A | ⬜ N/A |
| **Project Brain** | ⬜ N/A | ⬜ N/A | ✅ Required | ⬜ Inherits |
| **AI Thinking** | ✅ Required | ✅ Required | ⬜ Inherits | ⬜ Inherits |
| **Health Checks** | Every 15min | Every 4hr | On-event | None |
| **Status Reports** | Hourly | Daily | On-complete | None |
| **Incident Alerts** | Real-time | Real-time | On-error | Optional |
| **0UT Priority** | High | Normal | Normal | Low |

---

## 🔄 STRATOS DETERMINATION ALGORITHM

CMD.BRIDGE uses this to classify new entities:

```python
def determine_stratos(entity):
    # Count indicators
    indicators = {
        'sub_projects': count_sub_projects(entity),
        'complexity': assess_complexity(entity),
        'critical_infrastructure': has_critical_infra(entity),
        'multi_agent': requires_coordination(entity),
        'strategic_importance': rate_importance(entity)
    }
    
    # STRATOS-1: Mega Station
    if (indicators['sub_projects'] >= 10 or
        indicators['complexity'] == 'very_high' or
        indicators['critical_infrastructure'] and 
        indicators['multi_agent']):
        return 'STRATOS-1'
    
    # STRATOS-2: Station
    elif (indicators['sub_projects'] >= 3 or
          indicators['complexity'] == 'high' or
          indicators['strategic_importance'] >= 8):
        return 'STRATOS-2'
    
    # STRATOS-3: Project
    elif (indicators['sub_projects'] > 0 or
          indicators['complexity'] >= 'medium' or
          has_project_scope(entity)):
        return 'STRATOS-3'
    
    # STRATOS-4: Micro
    else:
        return 'STRATOS-4'
```

---

## 🎯 SPECIAL CASES

### Hybrid Entities:
Some entities may span multiple stratos:
- **Solution:** Classify at highest applicable stratos
- **Reason:** Better to over-specify than under-specify

### Growing Projects:
Projects can evolve up the stratos levels:
- **STRATOS-3 → STRATOS-2:** When project spawns 3+ sub-projects
- **STRATOS-2 → STRATOS-1:** When complexity/criticality increases
- **Migration:** CMD.BRIDGE orchestrates rule file creation

### Temporary Downgrades:
During maintenance or sunset:
- **STRATOS-1 → STRATOS-2:** When decomissioning sub-systems
- **Process:** Update rules, adjust reporting, notify agents

---

## 🚀 IMPLEMENTATION WORKFLOW

### For New STRATOS-1 Station:
```bash
1. CMD.BRIDGE creates folder structure
2. Generates all required rule files from templates
3. Registers in CMD.STATIONS/REGISTRY.yaml
4. Configures monitoring at 15min intervals
5. Tests 1N/0UT communication
6. Activates and begins tracking
```

### For New STRATOS-3 Project:
```bash
1. CMD.BRIDGE or Station OPS creates .3ox/
2. Generates PROJECT.BRAIN.md
3. Links to parent station for rule inheritance
4. Configures on-event reporting
5. Tests 0UT transmission
6. Marks as active
```

---

## ✅ VALIDATION CHECKLIST

When reviewing a stratos classification:

### STRATOS-1:
- [ ] All 6 required files present
- [ ] Health checks configured (≤15min)
- [ ] Error escalation defined (5 levels)
- [ ] Resource limits established
- [ ] Coordination rules documented
- [ ] AI thinking prompt customized

### STRATOS-2:
- [ ] 3 required files present
- [ ] Health checks configured (≤4hr)
- [ ] Error handling defined (3 levels)
- [ ] AI thinking prompt customized

### STRATOS-3:
- [ ] PROJECT.BRAIN.md present
- [ ] Parent station identified
- [ ] 0UT reporting configured
- [ ] Success criteria defined

### STRATOS-4:
- [ ] Parent project identified
- [ ] (That's it - inherits everything)

---

## 🌟 PHILOSOPHY

> _"Not all operations are equal. A mega-station orchestrating cloud infrastructure needs different rules than a single-purpose script. The stratos system honors this reality while maintaining unified communication."_

**Core Insight:** Scale-appropriate governance enables both robust control and lightweight execution.

---

## 🔗 RELATED FILES

- `GENESIS.SYSTEM.ARCHITECTURE.md` - Overall system design
- `MASTER.ROUTING.BRAIN.md` - How routing works
- Individual station `STATION.RULES.md` files

//▙▖▙▖▞▞▙▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂〘・.°𝚫〙

