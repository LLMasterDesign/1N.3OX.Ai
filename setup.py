"""
Setup configuration for SunsetGlow Banner Agent

This allows installation via pip:
    pip install -e .
    pip install .
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="sunsetglow",
    version="1.0.0",
    author="LLMasterDesign",
    author_email="",
    description="Professional street banner research and design agent",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LLMasterDesign/SunsetGlow",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Topic :: Scientific/Engineering :: Visualization",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.31.0",
        "beautifulsoup4>=4.12.0",
        "lxml>=4.9.0",
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "Pillow>=10.0.0",
        "svgwrite>=1.4.3",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "sunsetglow=sunsetglow.agent:main",
            "sunsetglow-research=sunsetglow.banner_cost_research:main",
            "sunsetglow-design=sunsetglow.banner_design:main",
            "sunsetglow-preview=sunsetglow.banner_preview:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords=[
        "banner",
        "design",
        "print",
        "sunsetglow",
        "ai-agent",
        "automation",
        "graphics",
        "visualization",
    ],
    project_urls={
        "Bug Reports": "https://github.com/LLMasterDesign/SunsetGlow/issues",
        "Source": "https://github.com/LLMasterDesign/SunsetGlow",
        "Documentation": "https://github.com/LLMasterDesign/SunsetGlow/blob/main/README.md",
    },
)
