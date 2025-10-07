///▙▖▙▖▞▞▙▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂
▛//▞▞ ⟦⎊⟧ :: ⧗-25.58 // 0UT.3OX.GIT.PROTOCOL ▞▞
▞//▞ 0ut.Git.Protocol :: ρ{event.tracking}.φ{GLOBAL}.τ{Protocol}.λ{transmission} ⫸
▙⌱[📡] ≔ [⊢{0ut.3ox}⇨{git.commit}⟿{route}▷{destination}]
〔0ut.3ox.git.event.protocol〕 :: ∎

# 📡 0UT.3OX → GIT EVENT TRACKING PROTOCOL

**Purpose:** Git repo tracks ONLY 0ut.3ox transmission events (not general file sync)  
**Scope:** Event history, auto-routing, log preservation  
**Location:** CMD.BRIDGE folder (master event log)

---

## 🎯 ARCHITECTURE

```
Worker/Tool creates 0ut.3ox
    ↓
Local transmission to CMD.STATIONS/
    ↓
Git commit (event logged)
    ↓
Git push to master repo (the sky)
    ↓
Auto-routing logic checks destination
    ↓
If routable → Forward to target
If log-only → Archive in CMD.BRIDGE
```

---

## 🔄 SYNC ARCHITECTURE

### pCloud: General File Sync
```
CMD.BRIDGE ↔ pCloud ↔ RVNx.BASE
CMD.BRIDGE ↔ pCloud ↔ OBSIDIAN.BASE
CMD.BRIDGE ↔ pCloud ↔ SYNTH.BASE
```
**Purpose:** Keep working files in sync across stations

### Git: Event Tracking ONLY
```
0ut.3ox files → Git commits → Master repo
```
**Purpose:** Track events, preserve history, enable routing

**Key Difference:**
- **pCloud** = File sync (continuous, automatic)
- **Git** = Event log (commit per 0ut.3ox, historical)

---

## 📦 GIT REPO STRUCTURE

### What Goes in Git:
```
CMD.BRIDGE-Events/          ← Git repo (events only)
├── 0UT.3OX/               ← All 0ut.3ox transmissions
│   ├── SYNTH/
│   │   └── SGL.Ai/
│   │       └── status_⧗-25.58.yaml
│   ├── RVNX/
│   │   └── TP.Gen/
│   │       └── runtime_status_⧗-25.58.yaml
│   └── OBSIDIAN/
│       └── (future agents)
│
├── LOGS/                  ← Event logs
│   └── CAPTAINS.LOG.txt   ← Master log
│
└── ROUTING/               ← Auto-routing rules
    └── routing.rules.yaml
```

### What DOESN'T Go in Git:
- Working project files (use pCloud)
- Large binaries (use pCloud)
- Temp files
- Local workspace state

---

## 🚀 SETUP COMMANDS

### Initialize Event Git Repo:
```bash
cd "P:\!CMD.BRIDGE\3OX.Ai\.3ox.index\OPS\CMD.STATIONS"
git init
git add 0UT.3OX/ LOGS/ ROUTING/
git commit -m "⧗-25.58 Initialize 0ut.3ox event tracking"
git remote add origin https://github.com/YOUR_USERNAME/3OX-Events.git
git push -u origin main
```

### On Worker Transmission:
```python
# When worker creates 0ut.3ox
def transmit_to_cmd(status_data):
    # Write 0ut.3ox file
    write_yaml(f"0ut.3ox_{sirius_time()}.yaml", status_data)
    
    # Commit to Git (this logs the event)
    subprocess.run(['git', 'add', 'OX/*.yaml'])
    subprocess.run(['git', 'commit', '-m', f'⧗-{sirius_time()} Status from {agent_name}'])
    subprocess.run(['git', 'push', 'origin', 'main'])
    
    # Auto-routing logic
    route_if_applicable(status_data)
```

---

## 🗺️ AUTO-ROUTING LOGIC

### When 0ut.3ox Arrives:
```yaml
routing_rules:
  - condition: "type == 'error'"
    action: "Alert CMD.BRIDGE immediately"
    destination: "MONITOR/ALERTS/"
    
  - condition: "type == 'status_report'"
    action: "Archive in CMD.STATIONS/STATUS/"
    destination: "STATUS/{agent_name}/"
    
  - condition: "type == 'completion_report'"
    action: "Update Captain's Log"
    destination: "LOGS/CAPTAINS.LOG.txt"
    
  - condition: "requires_action == true"
    action: "Create CMD.BRIDGE task"
    destination: "QUEUE/CMD_TASKS.yaml"
```

### Routing Script:
```python
def auto_route(transmission):
    # Read 0ut.3ox file
    data = read_yaml(transmission)
    
    # Check routing rules
    for rule in routing_rules:
        if matches(data, rule.condition):
            # Route to destination
            copy_to(transmission, rule.destination)
            
            # Log the route
            log_event(f"Routed {transmission} → {rule.destination}")
            
            # Commit routing event
            git_commit(f"Auto-routed: {transmission}")
```

---

## 🌟 "1N.3OX in the Sky" - The Full Picture

```
                    ☁️ Git Master Repo
                  (Event History - 0ut.3ox only)
                            │
                            │ git push/pull
                            │
              ┌─────────────┴─────────────┐
              │                           │
          ☁️ pCloud                 🖥️ CMD.BRIDGE
    (File Sync - General)      (Master Portal)
              │                   ↓   ↑
              │              0ut.3ox events
              │                   ↓   ↑
    ┌─────────┴───────┬────┬──────┴────┬────────┐
    │                 │    │           │        │
RVNx.BASE      OBSIDIAN.BASE   SYNTH.BASE   (Others)
(Stations sync files via pCloud)
(Send events via 0ut.3ox → Git)
```

**Two separate systems working together:**
1. **pCloud:** Files sync continuously
2. **Git:** Events tracked permanently

---

## ✅ IMMEDIATE ACTIONS

1. Move RVNx's duplicate `.3ox.index` ✓ (doing now)
2. Create separate Git repo for events
3. Setup auto-routing in CMD.STATIONS
4. Configure !RUNTIME to git push 0ut.3ox
5. Test the flow

Want me to continue with the folder cleanup and create the auto-routing script?
