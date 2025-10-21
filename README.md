# Sunsetglow Banner Agent

A comprehensive multi-stage AI agent system for street banner market research and conceptual design generation, built for Cursor AI.

**Brand:** Sunsetglow  
**Version:** 1.0.0

## 🎯 Overview

This modular agent system provides end-to-end banner solutions:

1. **Market Research** - Automated pricing data collection and analysis
2. **Design Generation** - Print-ready banner designs with Sunset Glow palette
3. **Visualization** - Realistic mockups and multi-format exports

## 🏗️ Component Architecture

### 1. Research Module (`sunsetglow/banner_cost_research.py`)
- Web scraping capabilities for vendor pricing
- Data collection for multiple banner sizes and materials
- Statistical analysis and price comparisons
- Budget-based vendor recommendations

**Features:**
- Banner sizes: 3x10ft, 4x12ft, 2x8ft, 5x15ft
- Materials: vinyl, mesh, polyester, canvas
- Price tracking: $150 - $1200 range
- Export to CSV and JSON

### 2. Design Module (`sunsetglow/banner_design.py`)
- Print-ready design generation at 300 DPI
- Sunsetglow color palette implementation
- Multiple design styles (gradient, split, geometric)
- CMYK conversion for professional printing

**Design Specifications:**
- **Color Palette:**
  - Grey-Blue: RGB(90, 120, 140) - bottom half
  - Orange: RGB(255, 140, 50) - highlights
- **Resolution:** 300 DPI
- **Color Mode:** RGB working / CMYK for print
- **Output Formats:** PNG, TIFF (CMYK), SVG

### 3. Preview Module (`sunsetglow/banner_preview.py`)
- Realistic contextual mockups (street scenes, building facades)
- Thumbnail generation
- Multi-format export (PNG, JPEG, PDF)
- Design comparison sheets

### 4. Main Orchestrator (`sunsetglow/agent.py`)
- Coordinates all modules in unified workflow
- Automated report generation
- Project organization and file management

## 📦 Installation

### Requirements
- Python 3.8+
- pip package manager

### Setup

```bash
# Clone or navigate to project directory
cd /workspace

# Install dependencies
pip install -r requirements.txt
```

### Dependencies
- `requests` - HTTP requests for web scraping
- `beautifulsoup4` - HTML parsing
- `pandas` - Data analysis
- `Pillow` - Image processing
- `svgwrite` - Vector graphics generation

## 🚀 Usage

### Quick Start - Complete Workflow

```python
from sunsetglow import BannerAgent

# Create agent instance
agent = BannerAgent(project_name="my_banner_project")

# Run complete workflow
results = agent.run_complete_workflow(
    budget=400,
    size="3x10ft",
    text="YOUR BANNER TEXT"
)
```

### Individual Module Usage

#### Research Module
```python
from sunsetglow import BannerCostResearch

research = BannerCostResearch()
research.simulate_vendor_research()

# Get pricing summary
summary = research.get_price_summary()

# Get recommendations
recommendations = research.get_recommendations(budget=300, size="3x10ft")

# Export data
research.export_research_data("pricing.csv")
research.export_summary_json("summary.json")
```

#### Design Module
```python
from sunsetglow import SunsetGlowDesigner

designer = SunsetGlowDesigner(size="3x10ft")

# Create design
banner = designer.create_design(text="EVENT NAME", style="gradient")

# Export in various formats
designer.export_png(banner, "banner_design.png")
designer.export_cmyk_tiff(banner, "banner_print.tif")
designer.create_svg_design("banner_vector.svg", text="EVENT NAME")
```

#### Preview Module
```python
from sunsetglow import BannerPreview

preview = BannerPreview()

# Create mockup
mockup = preview.create_mockup_context(banner, context_type="street")

# Export all formats
preview.export_all_formats(mockup, "banner_mockup")
```

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
python3 test_sunsetglow.py

# Or use pytest
pytest test_sunsetglow.py -v
```

**Test Coverage:**
- ✅ Research module accuracy
- ✅ Design validation against print standards
- ✅ Price range cross-referencing
- ✅ Color accuracy verification
- ✅ Export format validation
- ✅ Edge case handling

## 📊 Output Files

After running the agent, you'll find these files in the output directory:

### Design Files
- `design_gradient.png` - Gradient style design (300 DPI)
- `design_split.png` - Split color design (300 DPI)
- `design_geometric.png` - Geometric pattern design (300 DPI)
- `design_print_ready.tif` - **CMYK TIFF for printing**
- `design_vector.svg` - Scalable vector graphic

### Mockup Files
- `mockup_street.[png/jpg/pdf]` - Street scene visualization
- `mockup_building.[png/jpg/pdf]` - Building facade visualization
- Thumbnails for web preview

### Data Files
- `pricing_data.csv` - Complete vendor pricing data
- `pricing_summary.json` - Statistical analysis summary
- `design_specifications.json` - Print specifications
- `design_comparison.png` - Side-by-side design comparison
- `project_report.txt` - Complete project summary

## 🎨 Design Specifications

### Print-Ready Standards
- **Resolution:** 300 DPI minimum
- **Color Mode:** CMYK (converted from RGB)
- **Bleed:** 2 inches recommended
- **Finishing:** Hemmed edges with grommets

### Color Accuracy
All colors are specified in both RGB (for digital) and CMYK (for print):
- Grey-Blue: RGB(90,120,140) / CMYK(36,14,0,45)
- Orange: RGB(255,140,50) / CMYK(0,45,80,0)

### Recommended Materials
- **Vinyl** - Durable, weather-resistant
- **Mesh** - Wind-resistant, outdoor use
- **Polyester** - Premium quality, vibrant colors

## ⚙️ Edge Case Handling

The system handles:
- ✅ Regional pricing variations
- ✅ Incomplete vendor data
- ✅ Print specification divergences
- ✅ Network timeouts during scraping
- ✅ Missing fonts (fallback to default)
- ✅ Budget constraints (alternative recommendations)

## 🔧 Command Line Usage

### Run Complete Workflow
```bash
python3 -m sunsetglow.agent
```

### Run Individual Modules
```bash
# Research only
python3 -m sunsetglow.banner_cost_research

# Design only
python3 -m sunsetglow.banner_design

# Preview only
python3 -m sunsetglow.banner_preview
```

## 📋 Project Structure

```
/workspace/
├── sunsetglow/                    # Main package
│   ├── __init__.py               # Package initialization
│   ├── agent.py                  # Main orchestrator
│   ├── banner_cost_research.py   # Research module
│   ├── banner_design.py          # Design module
│   └── banner_preview.py         # Preview module
├── test_sunsetglow.py            # Test suite
├── demo.py                       # Quick demo script
├── requirements.txt              # Dependencies
├── README.md                     # Documentation
├── SETUP_GUIDE.md               # Quick start guide
├── PROJECT_SUMMARY.md           # Executive summary
└── [project]_output/            # Generated outputs
    ├── design_*.png
    ├── mockup_*.png
    ├── pricing_data.csv
    └── project_report.txt
```

## 🚦 Workflow Stages

### Stage 1: Research Phase
1. Collect vendor pricing data
2. Analyze price ranges by size/material
3. Generate statistical summaries
4. Export research data

### Stage 2: Design Phase
1. Initialize designer with specifications
2. Generate multiple design variations
3. Create print-ready CMYK files
4. Export vector graphics
5. Save design specifications

### Stage 3: Preview Phase
1. Create realistic mockups
2. Generate comparison sheets
3. Export in multiple formats
4. Create thumbnails for web

### Stage 4: Reporting
1. Compile all results
2. Generate comprehensive report
3. Organize output files

## 💡 Tips for Best Results

1. **Budget Planning:** Run research first to understand market pricing
2. **Material Selection:** Check recommendations based on use case
3. **Print Submission:** Use the `design_print_ready.tif` CMYK file
4. **Client Approval:** Show mockups and comparison sheets
5. **Vector Backup:** Keep the SVG file for future size variations

## 🔍 Troubleshooting

**Issue:** Fonts not found
- **Solution:** System uses fallback fonts automatically

**Issue:** Web scraping timeout
- **Solution:** Module includes simulated data as fallback

**Issue:** Color not accurate
- **Solution:** Use CMYK file with professional printer

**Issue:** File size too large
- **Solution:** Use JPEG exports for web, TIFF for print only

## 📄 License

This project is designed for use with Cursor AI agent workflows.

## 🤝 Contributing

This is a modular system designed for extension:
- Add new vendor scrapers to research module
- Create new design styles in design module
- Add mockup contexts to preview module

## 📞 Support

For issues or questions:
1. Check test results: `python test_banner_agent.py`
2. Review project report in output folder
3. Verify all dependencies are installed

---

**Built with Cursor AI | Sunsetglow Brand | Designed for Print Excellence**

:: ∎
