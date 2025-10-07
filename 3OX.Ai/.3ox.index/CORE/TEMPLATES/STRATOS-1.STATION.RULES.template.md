///▙▖▙▖▞▞▙▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂
▛//▞▞ ⟦⎊⟧ :: ⧗-[CURRENT] // [STATION].RULES ▞▞
▞//▞ [Station].Rules :: ρ{station.governance}.φ{[STATION]}.τ{Rules}.λ{L2} ⫸
▙⌱[🏛️] ≔ [⊢{policy}⇨{implement}⟿{enforce}▷{operate}]
〔[station].rules.stratos1〕 :: ∎

# 🏛️ [STATION NAME] STATION RULES

**Stratos Level:** STRATOS-1 (Mega Station)  
**Authority:** L2 (Station Operations)  
**Parent:** 3OX.Ai/.3ox.index/ (CMD.BRIDGE)  
**Version:** 1.0

---

## 🎯 STATION IDENTITY

### Mission:
> [Define the core mission of this station in 1-2 sentences]

### Scope:
- **Primary Domain:** [e.g., Cloud infrastructure, Sync operations, Knowledge management]
- **Operational Scale:** STRATOS-1 (10+ sub-projects or critical infrastructure)
- **Strategic Importance:** [Mission-critical | Strategic | Core operations]

### Boundaries:
- **What This Station Handles:**
  - [List primary responsibilities]
  - [Key operational areas]
  - [Infrastructure components]

- **What This Station Does NOT Handle:**
  - [Clear boundaries to avoid scope creep]
  - [What belongs to other stations]

---

## 🧠 ECOSYSTEM BRAIN

**Brain File:** `[STATION].BASE/!1N.3OX [STATION].BASE/.3ox.AI.BRAIN/AI.THINKING.PROMPT.md`

**Thinking Style:**
- [Describe how this station's brain thinks]
- [Key personality traits of the brain]
- [What makes this brain unique]

**Activation:**
- Automatically when working in [STATION].BASE
- Manual invocation: `@[STATION]`

---

## 📊 SUB-PROJECTS REGISTRY

### Active Projects:
1. **[Project 1]** - [Brief description]
   - Stratos: [3 or 4]
   - Status: [Active/Paused/Archived]
   - Agent: [Agent name if any]

2. **[Project 2]** - [Brief description]
   - Stratos: [3 or 4]
   - Status: [Active/Paused/Archived]
   - Agent: [Agent name if any]

[Continue for all sub-projects...]

### Project Classification:
- STRATOS-3 projects: [Count]
- STRATOS-4 micro-tools: [Count]
- Total active: [Count]

---

## 🔧 OPERATIONAL PROTOCOLS

### Startup Procedure:
```yaml
1. Verify all critical services are running
2. Check resource availability (compute/storage/network)
3. Load station configuration from .3ox/
4. Initialize monitoring systems
5. Verify connectivity to CMD.BRIDGE
6. Begin health check cycle (every 15 minutes)
7. Report READY status via 0UT.3OX
```

### Shutdown Procedure:
```yaml
1. Notify CMD.BRIDGE of planned shutdown
2. Complete in-progress operations (or save state)
3. Gracefully stop all services
4. Flush logs and pending 0UT transmissions
5. Archive operational state
6. Report OFFLINE status
```

### Health Check Intervals:
- **System Health:** Every 15 minutes
- **Resource Usage:** Every 15 minutes
- **Error Scan:** Every 15 minutes
- **Performance Metrics:** Every 30 minutes

### Maintenance Windows:
- **Scheduled:** [Define regular maintenance schedule]
- **Duration:** [Typical maintenance duration]
- **Notification:** [How far in advance to notify CMD]

---

## ⚠️ ERROR ESCALATION

### Error Severity Levels:

#### L5: CRITICAL - System Down
**Definition:** Core infrastructure failure, station inoperable  
**Examples:**
- Complete system crash
- Data corruption detected
- Security breach
- All services offline

**Automatic Response:**
1. Immediate 0UT.3OX alert to CMD.BRIDGE (priority: CRITICAL)
2. Attempt automatic recovery if safe
3. Preserve all logs and state
4. Halt all operations to prevent further damage

**Escalation:** IMMEDIATE to CMD.BRIDGE  
**Human Notification:** YES (page/SMS if configured)

---

#### L4: MAJOR - Critical Service Impaired
**Definition:** Major service disrupted but station partially operational  
**Examples:**
- Key service crashed
- Database connection lost
- Critical dependency failed
- Performance degraded >80%

**Automatic Response:**
1. Send 0UT.3OX alert within 1 minute (priority: HIGH)
2. Attempt service restart (max 3 attempts)
3. Reroute traffic if possible
4. Log detailed error information

**Escalation:** Within 5 minutes to CMD.BRIDGE  
**Human Notification:** If not resolved in 15 minutes

---

#### L3: MODERATE - Non-Critical Issue
**Definition:** Issue affecting operations but system remains functional  
**Examples:**
- Non-critical service error
- Retry failures (with eventual success)
- Performance degraded 20-80%
- Resource warnings

**Automatic Response:**
1. Log error with full context
2. Attempt automatic remediation
3. Include in next status report (hourly)
4. Monitor for escalation

**Escalation:** If persists >1 hour or worsens  
**Human Notification:** No (unless escalates)

---

#### L2: MINOR - Transient Error
**Definition:** Temporary issues that self-resolve  
**Examples:**
- Network timeout (single occurrence)
- Rate limit hit (with backoff)
- Cache miss
- Temporary resource contention

**Automatic Response:**
1. Log for pattern analysis
2. Apply standard retry logic
3. Include in daily report summary

**Escalation:** Only if pattern emerges (>10 in 1 hour)  
**Human Notification:** No

---

#### L1: INFO - Expected Events
**Definition:** Normal operational events, not errors  
**Examples:**
- Service restarts
- Configuration reloads
- Planned operations
- Status changes

**Automatic Response:**
1. Log for audit trail
2. No alerts

**Escalation:** N/A  
**Human Notification:** No

---

## 💾 RESOURCE MANAGEMENT

### Compute Resources:
- **CPU Limits:** [Define max CPU usage]
- **Memory Limits:** [Define max RAM usage]
- **Scaling Rules:**
  - Scale up if: [Condition]
  - Scale down if: [Condition]
  - Max instances: [Number]

### Storage Allocation:
- **Primary Storage:** [Location and quota]
- **Backup Storage:** [Location and quota]
- **Archive Storage:** [Location and retention policy]
- **Temp Storage:** [Location and cleanup rules]

### Network Usage:
- **Bandwidth Limits:** [If applicable]
- **Rate Limits:** [API calls, requests, etc.]
- **Connection Limits:** [Concurrent connections]

### Cost Monitoring (if cloud-based):
- **Monthly Budget:** [Amount if applicable]
- **Cost Alerts:**
  - Warning at: [% of budget]
  - Critical at: [% of budget]
- **Optimization Reviews:** [Frequency]

---

## 🤝 COORDINATION RULES

### Inter-Project Communication:
- **Method:** [How projects communicate - shared state, messages, API, etc.]
- **Protocol:** [Format and standards]
- **Conflict Resolution:** [How conflicts between projects are resolved]

### Shared Resources:
- **Resource Pool:** [What resources are shared]
- **Allocation Strategy:** [First-come-first-serve, priority-based, etc.]
- **Locking Mechanism:** [How to prevent conflicts]

### Dependencies:
- **Internal Dependencies:** [Projects that depend on each other within station]
- **External Dependencies:** [Dependencies on other stations]
- **Dependency Checks:** [How often dependencies are verified]

### Agent Coordination:
- **Single Agent:** If one agent manages multiple projects, how does it prioritize?
- **Multiple Agents:** If multiple agents, how do they coordinate?
- **Handoffs:** Protocol for passing work between agents

---

## 📡 REPORTING TO CMD.BRIDGE

### Report Types and Frequency:

#### Health Check (Every 15 minutes):
```yaml
header:
  stratos: "STRATOS-1"
  station: "[STATION]"
  timestamp: "⧗-[CURRENT]"
  type: "health"

payload:
  status: "HEALTHY|DEGRADED|CRITICAL"
  services:
    - name: "[Service 1]"
      status: "up|down"
      uptime: "[duration]"
    - name: "[Service 2]"
      status: "up|down"
      uptime: "[duration]"
  resources:
    cpu_usage: "[%]"
    memory_usage: "[%]"
    storage_usage: "[%]"
  error_counts:
    L5_critical: 0
    L4_major: 0
    L3_moderate: 2
    L2_minor: 15
    L1_info: 127
```

#### Status Summary (Hourly):
```yaml
header:
  stratos: "STRATOS-1"
  station: "[STATION]"
  timestamp: "⧗-[CURRENT]"
  type: "status"

payload:
  operations_completed: [count]
  operations_in_progress: [count]
  queue_depth: [count]
  performance_metrics:
    average_response_time: "[ms]"
    throughput: "[ops/min]"
    error_rate: "[%]"
  notable_events:
    - "[Event 1]"
    - "[Event 2]"
```

#### Daily Report (End of Day):
```yaml
header:
  stratos: "STRATOS-1"
  station: "[STATION]"
  timestamp: "⧗-[CURRENT]"
  type: "daily_report"

payload:
  summary: "[High-level summary of day]"
  achievements:
    - "[What was accomplished]"
  challenges:
    - "[Issues encountered]"
  statistics:
    total_operations: [count]
    total_errors: [count]
    uptime_percentage: "[%]"
  tomorrow_plan:
    - "[Planned activities]"
```

#### Incident Alert (Real-time):
```yaml
header:
  stratos: "STRATOS-1"
  station: "[STATION]"
  timestamp: "⧗-[CURRENT]"
  type: "incident"
  priority: "CRITICAL|HIGH|NORMAL"

payload:
  severity: "L5|L4|L3"
  incident: "[Brief description]"
  impact: "[What's affected]"
  attempted_remediation:
    - "[What was tried]"
  current_status: "[Current state]"
  requires_cmd_intervention: true|false
```

---

## 🔐 SECURITY AND ACCESS

### .3OX File Access:
- **This Station's Rules:** READ ONLY (even for this station's agents)
- **Sub-Project .3ox Files:** READ ONLY
- **Modifications:** Only CMD.BRIDGE (L1) can modify

### Sensitive Data:
- **Location:** [Where sensitive data is stored]
- **Encryption:** [Yes/No and method]
- **Access Control:** [Who/what can access]

### API Keys and Secrets:
- **Storage:** [How secrets are stored - env vars, vault, etc.]
- **Rotation:** [How often keys are rotated]
- **Access:** [What services need which keys]

---

## 🎯 DOMAIN-SPECIFIC POLICIES

[This section is CUSTOMIZED per station - add station-specific policies here]

### For Cloud/SaaS Stations (like SYNTH):
- Deployment policies
- Environment management (dev/staging/prod)
- Version control and rollback procedures
- API versioning

### For Sync Stations (like RVNx):
- Conflict resolution strategies
- Data integrity checks
- Atomic operation requirements
- Cross-platform compatibility rules

### For Knowledge Stations (like OBSIDIAN):
- Link integrity maintenance
- Tag conventions
- Note organization standards
- Graph optimization rules

---

## ✅ COMPLIANCE CHECKLIST

Station operations must verify:
- [ ] All Global Policies respected (POLICY folder)
- [ ] Sirius time used in all transmissions
- [ ] Role invocations recognized
- [ ] .3ox files treated as READ ONLY
- [ ] Error escalation levels properly implemented
- [ ] Health checks running at correct intervals
- [ ] All 0UT transmissions properly formatted
- [ ] Resource limits respected
- [ ] Security policies enforced

---

## 🔄 RULE UPDATE PROTOCOL

These rules can only be updated by:
1. **CMD.BRIDGE** (L1 authority)
2. **After validation** against Global Policy
3. **With logging** in Captain's Log
4. **With notification** to affected agents

Agents cannot modify their own rules (prevents recursive loops).

---

## 🌟 STATION PHILOSOPHY

> [Add a custom philosophy statement that captures this station's essence]

**Example:** "This station prioritizes safety over speed, integrity over convenience, and coordination over chaos."

---

## 📝 NOTES AND CONTEXT

[Add any station-specific notes, historical context, or important considerations]

---

**Established:** ⧗-[CURRENT]  
**Last Updated:** ⧗-[CURRENT]  
**Managed By:** CMD.BRIDGE  
**Status:** ACTIVE

//▙▖▙▖▞▞▙▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂〘・.°𝚫〙

