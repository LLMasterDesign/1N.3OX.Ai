# ///▙▖▙▖▞▞▙▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂
# ▛//▞▞ ⟦⎊⟧ :: ⧗-25.61 // DEPLOY ATOMIC .3OX TO R:// ▞▞
# Deploy atomic .3ox structure to R:// drive stations
# ///▙▖▙▖▞▞▙▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂

param(
    [switch]$DryRun = $false
)

$ErrorActionPreference = "Stop"

# ============================================================================
# Configuration
# ============================================================================

$SOURCE = "P:\!CMD.BRIDGE\3OX.Ai\3ox.index\TEMPLATES\.3ox.atomic"
$R_DRIVE = "R:\"

$STATIONS = @(
    @{ Name = "RVNx.BASE"; Brain = "RVNX_BRAIN"; Type = "SENTINEL" },
    @{ Name = "SYNTH.BASE"; Brain = "SYNTH_BRAIN"; Type = "ALCHEMIST" },
    @{ Name = "OBSIDIAN.BASE"; Brain = "OBSIDIAN_BRAIN"; Type = "LIGHTHOUSE" }
)

# ============================================================================
# Functions
# ============================================================================

function Write-Header {
    Write-Host ""
    Write-Host "  ///▙▖▙▖▞▞▙▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂" -ForegroundColor Cyan
    Write-Host "  ▛//▞▞ ⟦⎊⟧ :: ⧗-25.61 // ATOMIC .3OX DEPLOYMENT ▞▞" -ForegroundColor Cyan
    Write-Host "  ///▙▖▙▖▞▞▙▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂" -ForegroundColor Cyan
    Write-Host ""
}

function Get-SiriusTime {
    $reset = Get-Date "2025-08-08"
    $now = Get-Date
    $days = ($now - $reset).Days
    $year = $now.Year % 100
    return "⧗-$year.$days"
}

function Test-RDriveAccess {
    if (-not (Test-Path $R_DRIVE)) {
        Write-Host "  ❌ R:// drive not accessible!" -ForegroundColor Red
        Write-Host "  Please map R:// drive first." -ForegroundColor Yellow
        exit 1
    }
    Write-Host "  ✅ R:// drive accessible" -ForegroundColor Green
}

function Deploy-AtomicStructure {
    param($Station)
    
    $destPath = Join-Path $R_DRIVE $Station.Name ".3ox"
    
    Write-Host ""
    Write-Host "  📦 Deploying to: $($Station.Name)" -ForegroundColor Cyan
    Write-Host "     Brain Type: $($Station.Type)" -ForegroundColor Gray
    Write-Host "     Destination: $destPath" -ForegroundColor Gray
    
    if ($DryRun) {
        Write-Host "     [DRY RUN] Would copy atomic structure..." -ForegroundColor Yellow
        return
    }
    
    # Create .3ox directory if not exists
    if (-not (Test-Path $destPath)) {
        New-Item -ItemType Directory -Path $destPath -Force | Out-Null
        Write-Host "     ✅ Created .3ox directory" -ForegroundColor Green
    }
    
    # Copy atomic structure
    Copy-Item -Path "$SOURCE\*" -Destination $destPath -Recurse -Force
    Write-Host "     ✅ Copied atomic structure" -ForegroundColor Green
    
    # Customize brain.rs for this station
    $brainPath = Join-Path $destPath "brain.rs"
    if (Test-Path $brainPath) {
        $content = Get-Content $brainPath -Raw
        
        # Add station-specific constant at end
        $stationConfig = @"

// ============================================================================
// Station Configuration (Auto-generated)
// ============================================================================

/// Active brain for this station
pub const BRAIN: AgentConfig = $($Station.Brain);

/// Active rules for this station
pub const RULES: &[Rule] = match BRAIN.brain {
    BrainType::Sentinel => RVNX_RULES,
    BrainType::Alchemist => SYNTH_RULES,
    BrainType::Lighthouse => OBSIDIAN_RULES,
};

// Auto-generated: $(Get-SiriusTime)
// Station: $($Station.Name)
"@
        
        $content + $stationConfig | Set-Content $brainPath
        Write-Host "     ✅ Customized brain.rs for $($Station.Type)" -ForegroundColor Green
    }
    
    # Update runtime.rb with station ID
    $runtimePath = Join-Path $destPath "runtime.rb"
    if (Test-Path $runtimePath) {
        $content = Get-Content $runtimePath -Raw
        $content = $content -replace "ENV\['STATION_ID'\] \|\| 'UNKNOWN'", "'$($Station.Name)'"
        Set-Content $runtimePath $content
        Write-Host "     ✅ Configured runtime.rb with station ID" -ForegroundColor Green
    }
    
    # Initialize Git if not exists
    $gitPath = Join-Path $destPath ".git"
    if (-not (Test-Path $gitPath)) {
        Push-Location $destPath
        git init | Out-Null
        git add . | Out-Null
        git commit -m "init: atomic .3ox brain v1.0.0 ($($Station.Type))" | Out-Null
        Pop-Location
        Write-Host "     ✅ Initialized Git repository" -ForegroundColor Green
    }
    
    # Create trace.log if not exists
    $tracePath = Join-Path $destPath "trace.log"
    if (-not (Test-Path $tracePath)) {
        $timestamp = Get-SiriusTime
        "[${timestamp}] INIT | Atomic .3ox deployed | Station: $($Station.Name)" | Set-Content $tracePath
        Write-Host "     ✅ Created trace.log" -ForegroundColor Green
    }
    
    Write-Host "     🔥 Deployment complete!" -ForegroundColor Green
}

function Deploy-IOStructure {
    param($Station)
    
    $stationPath = Join-Path $R_DRIVE $Station.Name
    
    Write-Host ""
    Write-Host "  📂 Setting up I/O structure for: $($Station.Name)" -ForegroundColor Cyan
    
    # Create 1n.3ox (input)
    $inPath = Join-Path $stationPath "1n.3ox"
    if (-not (Test-Path $inPath)) {
        if (-not $DryRun) {
            New-Item -ItemType Directory -Path $inPath -Force | Out-Null
            Write-Host "     ✅ Created 1n.3ox (input boundary)" -ForegroundColor Green
        } else {
            Write-Host "     [DRY RUN] Would create 1n.3ox..." -ForegroundColor Yellow
        }
    }
    
    # Create 0ut.3ox (output) with Git
    $outPath = Join-Path $stationPath "0ut.3ox"
    if (-not (Test-Path $outPath)) {
        if (-not $DryRun) {
            New-Item -ItemType Directory -Path $outPath -Force | Out-Null
            
            # Initialize Git for output
            Push-Location $outPath
            git init | Out-Null
            "# Output Boundary`n`nFiles ready for delivery" | Set-Content "README.md"
            git add . | Out-Null
            git commit -m "init: output boundary" | Out-Null
            Pop-Location
            
            Write-Host "     ✅ Created 0ut.3ox (output boundary with Git)" -ForegroundColor Green
        } else {
            Write-Host "     [DRY RUN] Would create 0ut.3ox..." -ForegroundColor Yellow
        }
    }
}

function Show-Summary {
    Write-Host ""
    Write-Host "  ╔═══════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
    Write-Host "  ║           🔮 DEPLOYMENT COMPLETE $(Get-SiriusTime) 🔮              ║" -ForegroundColor Cyan
    Write-Host "  ╚═══════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "  Deployed to:" -ForegroundColor White
    foreach ($station in $STATIONS) {
        $brainIcon = switch ($station.Type) {
            "SENTINEL" { "🛡️ " }
            "ALCHEMIST" { "🧪" }
            "LIGHTHOUSE" { "🏛️ " }
        }
        Write-Host "    $brainIcon R:\$($station.Name)\.3ox\ ($($station.Type))" -ForegroundColor Gray
    }
    Write-Host ""
    Write-Host "  Structure:" -ForegroundColor White
    Write-Host "    ├── brain.rs      (Agent identity + rules)" -ForegroundColor Gray
    Write-Host "    ├── tools.rs      (Runtime toolset)" -ForegroundColor Gray
    Write-Host "    ├── runtime.rb    (Orchestration)" -ForegroundColor Gray
    Write-Host "    ├── trace.log     (Event log)" -ForegroundColor Gray
    Write-Host "    └── README.md     (Documentation)" -ForegroundColor Gray
    Write-Host ""
    Write-Host "  I/O Boundaries:" -ForegroundColor White
    Write-Host "    ├── 1n.3ox/       (Input)" -ForegroundColor Gray
    Write-Host "    └── 0ut.3ox/      (Output, Git-enabled)" -ForegroundColor Gray
    Write-Host ""
    
    if ($DryRun) {
        Write-Host "  ⚠️  DRY RUN MODE - No changes made" -ForegroundColor Yellow
        Write-Host "  Run without -DryRun to deploy" -ForegroundColor Yellow
    } else {
        Write-Host "  ✅ All stations operational!" -ForegroundColor Green
        Write-Host "  🔥 Atomic .3ox v1.0.0 deployed successfully" -ForegroundColor Green
    }
    Write-Host ""
}

# ============================================================================
# Main Execution
# ============================================================================

Write-Header

if ($DryRun) {
    Write-Host "  🔍 DRY RUN MODE - Simulating deployment..." -ForegroundColor Yellow
    Write-Host ""
}

# Check R:// drive access
Test-RDriveAccess

# Verify source exists
if (-not (Test-Path $SOURCE)) {
    Write-Host "  ❌ Source template not found: $SOURCE" -ForegroundColor Red
    exit 1
}
Write-Host "  ✅ Source template found" -ForegroundColor Green

# Deploy to each station
foreach ($station in $STATIONS) {
    Deploy-AtomicStructure -Station $station
    Deploy-IOStructure -Station $station
}

# Show summary
Show-Summary

# ///▙▖▙▖▞▞▙▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂
# Deployment Complete | Sirius ⧗-25.61
# ///▙▖▙▖▞▞▙▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂

