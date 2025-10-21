# Street Banner Agent - Quick Setup Guide

## 🚀 Quick Start (3 Steps)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run Demo
```bash
python3 demo.py
```

### Step 3: Run Complete Workflow
```bash
python3 banner_agent.py
```

## 📋 What Each File Does

### Core Modules
- **`banner_agent.py`** - Main orchestrator that runs complete workflow
- **`banner_cost_research.py`** - Pricing research and vendor analysis
- **`sunsetglow_banner_design.py`** - Design generation with Sunset Glow palette
- **`banner_preview.py`** - Mockup creation and multi-format export

### Supporting Files
- **`test_banner_agent.py`** - Comprehensive test suite (35 tests)
- **`demo.py`** - Quick demo without large file generation
- **`requirements.txt`** - Python dependencies
- **`README.md`** - Complete documentation
- **`SETUP_GUIDE.md`** - This file

## 🎯 Common Usage Patterns

### Just Want Pricing Research?
```bash
python3 banner_cost_research.py
```
Output: `banner_research_data.csv`, `pricing_summary.json`

### Just Want a Design?
```bash
python3 sunsetglow_banner_design.py
```
Output: Multiple PNG designs + CMYK TIFF + SVG

### Want Everything?
```bash
python3 banner_agent.py
```
Output: Complete project folder with all assets

## 🧪 Testing

Run all 35 tests:
```bash
python3 test_banner_agent.py
```

Expected result: ✅ All 35 tests passing

## 📦 Dependencies

All required packages are in `requirements.txt`:
- requests (web scraping)
- beautifulsoup4 (HTML parsing)
- pandas (data analysis)
- Pillow (image processing)
- svgwrite (vector graphics)

## ⚡ Performance Notes

**Design Generation:**
- 300 DPI designs are large files (100+ MB for 3x10ft)
- First run may take 30-60 seconds
- Subsequent runs are faster

**File Sizes:**
- PNG designs: ~50-150 MB each
- CMYK TIFF: ~100-200 MB
- SVG: < 1 MB (scalable)
- Mockups: ~5-10 MB each

## 🎨 Customization

### Change Banner Size
```python
from sunsetglow_banner_design import SunsetGlowDesigner

# Options: "3x10ft", "4x12ft", "2x8ft", "5x15ft"
designer = SunsetGlowDesigner(size="4x12ft")
```

### Change Budget
```python
from banner_agent import BannerAgent

agent = BannerAgent(project_name="my_project")
agent.run_complete_workflow(budget=500, size="4x12ft")
```

### Change Design Text
```python
designer.create_design(text="YOUR TEXT HERE", style="gradient")
```

## 🐛 Troubleshooting

**Problem:** `python: command not found`
- **Solution:** Use `python3` instead

**Problem:** Module import errors
- **Solution:** Run `pip install -r requirements.txt`

**Problem:** PIL DecompressionBombError
- **Solution:** This is expected for large 300 DPI files. The files are created correctly; just can't be re-opened by PIL's safety check. Use professional image software to verify.

**Problem:** Out of memory
- **Solution:** Use smaller banner size for testing, or increase system RAM

## 📞 Support Checklist

Before asking for help:
1. ✅ Installed all dependencies?
2. ✅ Using Python 3.8+?
3. ✅ Ran test suite successfully?
4. ✅ Checked output directory for files?

## 🎓 Learning Path

**Beginner:**
1. Run `demo.py` to see capabilities
2. Run `banner_cost_research.py` individually
3. Review output CSV and JSON files

**Intermediate:**
1. Run complete workflow with `banner_agent.py`
2. Examine generated designs
3. Review project report

**Advanced:**
1. Modify design module for custom color palettes
2. Add new vendor scrapers to research module
3. Create custom mockup contexts in preview module
4. Extend test suite with additional edge cases

## 📄 File Outputs Reference

After running `banner_agent.py`, expect these files in `[project]_output/`:

```
[project]_output/
├── design_gradient.png          # Gradient style design
├── design_split.png             # Split color design  
├── design_geometric.png         # Geometric pattern design
├── design_print_ready.tif       # ⭐ CMYK for printing
├── design_vector.svg            # Scalable vector
├── mockup_street.png/jpg/pdf    # Street scene visualization
├── mockup_building.png/jpg/pdf  # Building visualization
├── pricing_data.csv             # Vendor pricing table
├── pricing_summary.json         # Statistical analysis
├── design_specifications.json   # Print specs
├── design_comparison.png        # Side-by-side comparison
└── project_report.txt           # ⭐ Complete summary
```

**Key Files for Printing:**
- `design_print_ready.tif` - Send this to your print vendor
- `design_specifications.json` - Share with printer for specs

**Key Files for Client Approval:**
- `mockup_street.jpg` - Show realistic visualization
- `design_comparison.png` - Show all design options

## 🔐 Best Practices

1. **Always run tests before production:** `python3 test_banner_agent.py`
2. **Check pricing before design:** Get budget first from research module
3. **Use CMYK TIFF for printing:** Not PNG or JPEG
4. **Keep SVG for size variations:** Vector scales perfectly
5. **Show mockups to clients:** Not raw designs

## ⏱️ Typical Execution Times

- Research module: ~1 second
- Design module: ~30-60 seconds (300 DPI generation)
- Preview module: ~20-30 seconds (mockups)
- Complete workflow: ~2-3 minutes
- Test suite: ~30-40 seconds

---

**Ready to create amazing banners!** 🎨

:: ∎
