# Sunsetglow Banner Agent - Quick Start

## 🌅 Welcome to Sunsetglow!

This is your complete banner research and design system.

---

## ⚡ 30-Second Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run demo (no large files)
python3 demo.py

# 3. Run tests (verify everything works)
python3 test_sunsetglow.py

# 4. Create your first banner project
python3 -m sunsetglow.agent
```

---

## 📦 What You Get

**Sunsetglow Package** - All modules in one place:
```python
from sunsetglow import (
    BannerAgent,           # Main workflow orchestrator
    BannerCostResearch,    # Pricing research
    SunsetGlowDesigner,    # Design generation
    BannerPreview          # Mockup visualization
)
```

---

## 🎯 Common Tasks

### Research Banner Pricing
```bash
python3 -m sunsetglow.banner_cost_research
```
**Output:** `banner_research_data.csv`, `pricing_summary.json`

### Generate Banner Design
```bash
python3 -m sunsetglow.banner_design
```
**Output:** PNG designs (300 DPI), CMYK TIFF, SVG

### Create Full Project
```bash
python3 -m sunsetglow.agent
```
**Output:** Complete project folder with all assets

---

## 💡 Code Examples

### Quick Banner Creation
```python
from sunsetglow import SunsetGlowDesigner

# Create designer
designer = SunsetGlowDesigner(size="3x10ft")

# Generate design
banner = designer.create_design(
    text="SPECIAL EVENT",
    style="gradient"
)

# Export for printing
designer.export_cmyk_tiff(banner, "print_ready.tif")
```

### Get Pricing Recommendations
```python
from sunsetglow import BannerCostResearch

# Research vendors
research = BannerCostResearch()
research.simulate_vendor_research()

# Find options under budget
options = research.get_recommendations(
    budget=300,
    size="3x10ft"
)

for option in options:
    print(f"{option['vendor']}: ${option['total_cost']}")
```

### Complete Workflow
```python
from sunsetglow import BannerAgent

# Create agent
agent = BannerAgent(project_name="summer_festival")

# Run everything
results = agent.run_complete_workflow(
    budget=400,
    size="3x10ft",
    text="SUMMER FESTIVAL"
)
```

---

## 📁 Project Structure

```
sunsetglow/
├── __init__.py              # Import all modules easily
├── agent.py                 # Main orchestrator
├── banner_cost_research.py  # Pricing research
├── banner_design.py         # Design generation
└── banner_preview.py        # Mockup creation
```

---

## 🎨 Design Specifications

**Sunsetglow Color Palette:**
- Grey-Blue: `RGB(90, 120, 140)` - Professional base
- Orange: `RGB(255, 140, 50)` - Vibrant accents

**Print Ready:**
- 300 DPI resolution
- CMYK color mode
- Vector SVG included

---

## 🧪 Testing

```bash
# Run all 35 tests
python3 test_sunsetglow.py
```

**Expected:** ✅ All 35 tests passed!

---

## 📞 Need Help?

1. **Read the docs:** `README.md` - Complete documentation
2. **Setup guide:** `SETUP_GUIDE.md` - Troubleshooting
3. **Examples:** `demo.py` - Live demonstrations
4. **Summary:** `PROJECT_SUMMARY.md` - Executive overview

---

## 🚀 Next Steps

1. ✅ Run `demo.py` to see capabilities
2. ✅ Run `test_sunsetglow.py` to verify installation
3. ✅ Create your first project with `python3 -m sunsetglow.agent`
4. ✅ Review generated files in `[project]_output/` folder

---

**Brand:** Sunsetglow  
**Version:** 1.0.0  
**Built with:** Cursor AI

:: ∎
