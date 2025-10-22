# SunsetGlow Installation Guide

## 🌅 Installation Options

### Option 1: Direct Installation (Recommended for Development)

```bash
# Clone the repository
git clone https://github.com/LLMasterDesign/SunsetGlow.git
cd SunsetGlow

# Install dependencies
pip install -r requirements.txt

# Test installation
python3 test_sunsetglow.py
```

### Option 2: Editable Installation (For Development)

```bash
# Clone and navigate to repository
git clone https://github.com/LLMasterDesign/SunsetGlow.git
cd SunsetGlow

# Install in editable mode
pip install -e .

# Now you can use sunsetglow from anywhere
python -c "from sunsetglow import BannerAgent"
```

### Option 3: Package Installation (Future - PyPI)

```bash
# When published to PyPI
pip install sunsetglow
```

---

## 🔧 System Requirements

**Minimum:**
- Python 3.8 or higher
- 4GB RAM
- 500MB disk space

**Recommended:**
- Python 3.10+
- 8GB RAM
- 2GB disk space
- SSD for faster operations

---

## 📦 Dependencies

All dependencies are in `requirements.txt`:

```
requests>=2.31.0          # HTTP requests
beautifulsoup4>=4.12.0    # HTML parsing
pandas>=2.0.0             # Data analysis
Pillow>=10.0.0            # Image processing
svgwrite>=1.4.3           # Vector graphics
```

### Optional (for testing):
```
pytest>=7.4.0
pytest-cov>=4.1.0
```

---

## 🚀 Quick Start After Installation

### Verify Installation
```bash
# Run tests
python3 test_sunsetglow.py

# Expected: ✅ All 35 tests passed!
```

### Try the Demo
```bash
python3 demo.py
```

### Create Your First Banner
```python
from sunsetglow import BannerAgent

agent = BannerAgent(project_name="my_first_banner")
agent.run_complete_workflow(
    budget=400,
    size="3x10ft",
    text="HELLO WORLD"
)
```

### Or Use Command Line (after editable install)
```bash
# Run complete workflow
sunsetglow

# Run research only
sunsetglow-research

# Run design only
sunsetglow-design
```

---

## 🐛 Troubleshooting

### ImportError: No module named 'sunsetglow'

**Solution 1:** Install in editable mode
```bash
pip install -e .
```

**Solution 2:** Add to Python path
```bash
export PYTHONPATH="${PYTHONPATH}:/path/to/SunsetGlow"
```

### PIL.Image.DecompressionBombError

This is expected for 300 DPI images. Files are created correctly; this is just a safety warning.

**Solution:** Increase PIL limits (optional)
```python
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
```

### Missing Fonts

The system uses fallback fonts automatically. No action needed.

---

## 🔄 Updating

```bash
# Pull latest changes
git pull origin main

# Reinstall dependencies (if updated)
pip install -r requirements.txt --upgrade

# If installed with -e, changes are automatic
# Otherwise, reinstall:
pip install -e .
```

---

## 🗑️ Uninstallation

```bash
# If installed with pip
pip uninstall sunsetglow

# Remove directory
rm -rf SunsetGlow/
```

---

## ✅ Verify Installation Checklist

- [ ] Python 3.8+ installed (`python3 --version`)
- [ ] Dependencies installed (`pip list | grep -E "requests|pandas|Pillow"`)
- [ ] Tests passing (`python3 test_sunsetglow.py`)
- [ ] Demo runs (`python3 demo.py`)
- [ ] Can import package (`python -c "import sunsetglow"`)

---

## 📞 Get Help

If installation fails:

1. Check Python version: `python3 --version` (need 3.8+)
2. Update pip: `pip install --upgrade pip`
3. Try installing dependencies one by one
4. Check `SETUP_GUIDE.md` for detailed troubleshooting

---

**SunsetGlow Banner Agent v1.0.0**

:: ∎
