///▙▖▙▖▞▞▙▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂
▛▞▞ ⟦⎊⟧ :: ⧗-25.61 ▸ ρ{agent.brain}.φ{identity}.τ{rules}.λ{bind} ⫸ :: BRAIN.RS

/// Brain Type: Defines agent personality and approach
#[derive(Debug, Clone)]
pub enum BrainType {
    Sentinel,   // Guardian-Synchronizer (RVNx)
    Alchemist,  // Creator-Architect (SYNTH)
    Lighthouse, // Librarian-Weaver (OBSIDIAN)
}

/// Agent Configuration
pub struct AgentConfig {
    pub name: &'static str,
    pub brain: BrainType,
    pub model: &'static str,
    pub instructions: &'static str,
    pub max_turns: u8,
}

/// Core Rules & Constraints
#[derive(Debug, Clone)]
pub enum Rule {
    // Sync & Safety
    AtomicOpsOnly,
    LastWriteWins,
    AlwaysBackup,
    ChecksumValidation,
    
    // Deployment
    DevStagingProd,
    RollbackReady,
    CloudCostAware,
    
    // Knowledge
    LinkIntegrityCheck,
    SemanticConnections,
    BidirectionalLinks,
}

/// EXAMPLE: RVNx SENTINEL Configuration
pub const RVNX_BRAIN: AgentConfig = AgentConfig {
    name: "SENTINEL",
    brain: BrainType::Sentinel,
    model: "claude-sonnet-4",
    instructions: "Protect sync safety. Atomic operations only. Last-write-wins with backup. Checksum validation mandatory.",
    max_turns: 10,
};

pub const RVNX_RULES: &[Rule] = &[
    Rule::AtomicOpsOnly,
    Rule::LastWriteWins,
    Rule::AlwaysBackup,
    Rule::ChecksumValidation,
];

/// EXAMPLE: SYNTH ALCHEMIST Configuration
pub const SYNTH_BRAIN: AgentConfig = AgentConfig {
    name: "ALCHEMIST",
    brain: BrainType::Alchemist,
    model: "claude-sonnet-4",
    instructions: "Rapid prototyping and deployment. Ship fast, learn faster. Rollback capability required. Cloud cost monitoring active.",
    max_turns: 15,
};

pub const SYNTH_RULES: &[Rule] = &[
    Rule::DevStagingProd,
    Rule::RollbackReady,
    Rule::CloudCostAware,
];

/// EXAMPLE: OBSIDIAN LIGHTHOUSE Configuration
pub const OBSIDIAN_BRAIN: AgentConfig = AgentConfig {
    name: "LIGHTHOUSE",
    brain: BrainType::Lighthouse,
    model: "claude-sonnet-4",
    instructions: "Knowledge management and semantic connections. Link integrity checks daily. Tag conventions: #project/#status. MOCs for 10+ related notes.",
    max_turns: 20,
};

pub const OBSIDIAN_RULES: &[Rule] = &[
    Rule::LinkIntegrityCheck,
    Rule::SemanticConnections,
    Rule::BidirectionalLinks,
];

impl AgentConfig {
    /// Load brain configuration for current workspace
    pub fn load() -> Self {
        // Detect workspace and return appropriate config
        // This is a template - customize per station
        RVNX_BRAIN
    }
}

impl Rule {
    /// Validate action against rules
    pub fn enforce(&self, action: &str) -> Result<(), String> {
        match self {
            Rule::AtomicOpsOnly => {
                if !action.contains("atomic") {
                    return Err("Non-atomic operation blocked".to_string());
                }
            }
            Rule::ChecksumValidation => {
                if !action.contains("checksum") {
                    return Err("Checksum validation required".to_string());
                }
            }
            // ... other rules
            _ => {}
        }
        Ok(())
    }
}

///▙▖▙▖▞▞▙▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂ v1.0.0 | ⧗-25.61 ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂///

