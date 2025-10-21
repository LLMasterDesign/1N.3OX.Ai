#!/usr/bin/env python3
"""
Quick Demo Script for Street Banner Agent

This script demonstrates the capabilities of the banner agent system
without generating large output files.
"""

from banner_cost_research import BannerCostResearch
from sunsetglow_banner_design import SunsetGlowDesigner
from banner_preview import BannerPreview
from PIL import Image


def demo_research():
    """Demonstrate research module capabilities."""
    print("\n" + "=" * 60)
    print("DEMO 1: Research Module")
    print("=" * 60)
    
    research = BannerCostResearch()
    
    # Collect data
    print("\n📊 Simulating vendor data collection...")
    data = research.simulate_vendor_research()
    print(f"✓ Collected data from {len(set([d['vendor'] for d in data]))} vendors")
    
    # Get summary
    summary = research.get_price_summary()
    print(f"\n💰 Price Range: ${summary['overall']['min_price']:.2f} - ${summary['overall']['max_price']:.2f}")
    print(f"   Average: ${summary['overall']['avg_price']:.2f}")
    
    # Get recommendations
    recommendations = research.get_recommendations(budget=300, size="3x10ft")
    print(f"\n💡 Found {len(recommendations)} options under $300:")
    for rec in recommendations[:3]:
        print(f"   • {rec['vendor']}: ${rec['total_cost']:.2f} ({rec['material']})")
    
    return research


def demo_design():
    """Demonstrate design module capabilities."""
    print("\n" + "=" * 60)
    print("DEMO 2: Design Module")
    print("=" * 60)
    
    # Use smaller size for demo to avoid huge files
    print("\n🎨 Creating designer for 3x10ft banner...")
    designer = SunsetGlowDesigner(size="3x10ft")
    
    specs = designer.get_design_specifications()
    print(f"✓ Resolution: {specs['resolution']['dpi']} DPI")
    print(f"✓ Dimensions: {specs['dimensions']['width_inches']}\" x {specs['dimensions']['height_inches']}\"")
    print(f"✓ Color Palette: Grey-Blue RGB{specs['color_palette']['grey_blue_rgb']}, Orange RGB{specs['color_palette']['orange_rgb']}")
    
    # Note: Not generating actual images in demo to save space/time
    print("\n🖌️  Design styles available:")
    print("   • Gradient - Smooth color transition")
    print("   • Split - Bold color blocking")
    print("   • Geometric - Modern patterns")
    
    return designer


def demo_preview():
    """Demonstrate preview module capabilities."""
    print("\n" + "=" * 60)
    print("DEMO 3: Preview Module")
    print("=" * 60)
    
    preview = BannerPreview()
    
    # Create small demo image
    print("\n🖼️  Preview capabilities:")
    print("   • Realistic street scene mockups")
    print("   • Building facade visualizations")
    print("   • Multi-format exports (PNG, JPEG, PDF)")
    print("   • Design comparison sheets")
    print("   • Thumbnail generation")
    
    demo_img = Image.new('RGB', (400, 1200), (255, 140, 50))
    thumb = demo_img.copy()
    preview.create_thumbnail(thumb, max_size=200)
    print(f"\n✓ Thumbnail created: {thumb.size[0]}x{thumb.size[1]} pixels")
    
    return preview


def demo_workflow():
    """Demonstrate complete workflow."""
    print("\n" + "=" * 60)
    print("DEMO 4: Complete Workflow")
    print("=" * 60)
    
    print("\n🔄 Standard Workflow:")
    print("\n   1. RESEARCH PHASE")
    print("      → Collect vendor pricing")
    print("      → Analyze market rates")
    print("      → Get budget recommendations")
    
    print("\n   2. DESIGN PHASE")
    print("      → Generate multiple design concepts")
    print("      → Create print-ready CMYK files")
    print("      → Export vector graphics")
    
    print("\n   3. PREVIEW PHASE")
    print("      → Create realistic mockups")
    print("      → Generate comparison sheets")
    print("      → Export in multiple formats")
    
    print("\n   4. DELIVERY")
    print("      → Organized output directory")
    print("      → Complete project report")
    print("      → Print-ready files for vendor")


def main():
    """Run all demos."""
    print("\n" + "🎨" * 30)
    print("STREET BANNER AGENT - QUICK DEMO")
    print("🎨" * 30)
    
    print("\nThis demo showcases the capabilities of each module")
    print("without generating large output files.\n")
    
    # Run demos
    demo_research()
    demo_design()
    demo_preview()
    demo_workflow()
    
    print("\n" + "=" * 60)
    print("✅ DEMO COMPLETE")
    print("=" * 60)
    
    print("\n📚 To run full workflow with output generation:")
    print("   python3 banner_agent.py")
    
    print("\n📚 To run individual modules:")
    print("   python3 banner_cost_research.py")
    print("   python3 sunsetglow_banner_design.py")
    print("   python3 banner_preview.py")
    
    print("\n🧪 To run tests:")
    print("   python3 test_banner_agent.py")
    
    print("\n:: ∎")


if __name__ == "__main__":
    main()
