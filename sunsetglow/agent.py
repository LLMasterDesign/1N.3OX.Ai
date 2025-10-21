"""
Street Banner Agent - Main Orchestrator

Multi-stage Cursor AI agent for street banner market research
and conceptual design generation.

This module coordinates the research, design, and preview components
to provide a complete banner solution workflow.
"""

import os
import sys
from datetime import datetime
from typing import Dict, List, Optional
import json

from .banner_cost_research import BannerCostResearch
from .banner_design import SunsetGlowDesigner
from .banner_preview import BannerPreview


class BannerAgent:
    """
    Main orchestrator for the street banner research and design agent.
    
    Coordinates multiple modules to provide end-to-end banner solutions:
    1. Market research and pricing analysis
    2. Design generation with brand specifications
    3. Preview and mockup visualization
    """
    
    def __init__(self, project_name: str = "banner_project"):
        """
        Initialize the banner agent.
        
        Args:
            project_name: Name for the project (used for file organization)
        """
        self.project_name = project_name
        self.output_dir = f"{project_name}_output"
        self.research_module = BannerCostResearch()
        self.preview_module = BannerPreview()
        
        # Create output directory
        os.makedirs(self.output_dir, exist_ok=True)
        
        print(f"🤖 Banner Agent initialized: {project_name}")
        print(f"📁 Output directory: {self.output_dir}/")
    
    def run_research_phase(self, export_data: bool = True) -> Dict:
        """
        Execute the research phase to gather pricing data.
        
        Args:
            export_data: Whether to export research data to files
            
        Returns:
            Dictionary containing pricing summary
        """
        print("\n" + "=" * 60)
        print("PHASE 1: Market Research & Pricing Analysis")
        print("=" * 60)
        
        # Collect vendor data
        print("\n📊 Collecting vendor pricing data...")
        self.research_module.simulate_vendor_research()
        
        # Generate analysis
        print("💰 Analyzing pricing trends...")
        summary = self.research_module.get_price_summary()
        
        # Display summary
        print("\n📈 Pricing Summary:")
        print(f"  Overall Range: ${summary['overall']['min_price']:.2f} - ${summary['overall']['max_price']:.2f}")
        print(f"  Average Price: ${summary['overall']['avg_price']:.2f}")
        print(f"  Median Price: ${summary['overall']['median_price']:.2f}")
        
        print("\n📏 Price by Size:")
        for size, data in summary['by_size'].items():
            print(f"  {size}: ${data['avg']:.2f} avg ({data['count']} vendors)")
        
        print("\n🎨 Price by Material:")
        for material, data in summary['by_material'].items():
            print(f"  {material.capitalize()}: ${data['avg']:.2f} avg")
        
        # Export if requested
        if export_data:
            csv_file = os.path.join(self.output_dir, "pricing_data.csv")
            json_file = os.path.join(self.output_dir, "pricing_summary.json")
            
            self.research_module.export_research_data(csv_file)
            self.research_module.export_summary_json(json_file)
            
            print(f"\n✓ Research data exported to {self.output_dir}/")
        
        return summary
    
    def get_budget_recommendations(self, budget: float, size: str = "3x10ft") -> List[Dict]:
        """
        Get vendor recommendations based on budget.
        
        Args:
            budget: Maximum budget
            size: Desired banner size
            
        Returns:
            List of recommended vendors
        """
        print(f"\n💡 Finding options for {size} banner within ${budget:.2f} budget...")
        
        recommendations = self.research_module.get_recommendations(budget=budget, size=size)
        
        if recommendations:
            print(f"\n✓ Found {len(recommendations)} options:")
            for i, rec in enumerate(recommendations[:5], 1):
                print(f"  {i}. {rec['vendor']}: ${rec['total_cost']:.2f}")
                print(f"     Material: {rec['material']}, Turnaround: {rec['turnaround_days']} days")
        else:
            print(f"  ⚠️  No vendors found within budget. Consider increasing budget.")
        
        return recommendations
    
    def run_design_phase(self, size: str = "3x10ft", text: str = "", 
                        styles: List[str] = None) -> Dict[str, any]:
        """
        Execute the design phase to create banner designs.
        
        Args:
            size: Banner size
            text: Text to display on banner
            styles: List of design styles to generate
            
        Returns:
            Dictionary containing designer and generated images
        """
        print("\n" + "=" * 60)
        print("PHASE 2: Design Generation")
        print("=" * 60)
        
        if styles is None:
            styles = ["gradient", "split", "geometric"]
        
        # Initialize designer
        print(f"\n🎨 Creating designer for {size} banner...")
        designer = SunsetGlowDesigner(size=size)
        
        # Display specifications
        specs = designer.get_design_specifications()
        print(f"  Resolution: {specs['resolution']['dpi']} DPI")
        print(f"  Dimensions: {specs['dimensions']['width_inches']}\" x {specs['dimensions']['height_inches']}\"")
        print(f"  Pixels: {specs['dimensions']['width_pixels']} x {specs['dimensions']['height_pixels']}")
        
        print("\n🌅 Color Palette:")
        print(f"  Grey-Blue: RGB{specs['color_palette']['grey_blue_rgb']}")
        print(f"  Orange: RGB{specs['color_palette']['orange_rgb']}")
        
        # Generate designs
        print(f"\n🖌️  Generating {len(styles)} design variations...")
        designs = {}
        
        for style in styles:
            print(f"  • Creating {style} design...")
            img = designer.create_design(text=text, style=style)
            designs[style] = img
            
            # Export PNG
            png_file = os.path.join(self.output_dir, f"design_{style}.png")
            designer.export_png(img, png_file)
        
        # Export print-ready CMYK version of best design
        print("\n📄 Creating print-ready files...")
        best_design = designs.get("geometric", list(designs.values())[0])
        
        cmyk_file = os.path.join(self.output_dir, "design_print_ready.tif")
        designer.export_cmyk_tiff(best_design, cmyk_file)
        
        svg_file = os.path.join(self.output_dir, "design_vector.svg")
        designer.create_svg_design(svg_file, text=text)
        
        # Export specifications
        spec_file = os.path.join(self.output_dir, "design_specifications.json")
        with open(spec_file, 'w') as f:
            json.dump(specs, f, indent=2)
        
        print(f"\n✓ All designs exported to {self.output_dir}/")
        
        return {
            "designer": designer,
            "designs": designs,
            "specifications": specs
        }
    
    def run_preview_phase(self, designs: Dict, create_mockups: bool = True) -> None:
        """
        Execute the preview phase to create mockups and visualizations.
        
        Args:
            designs: Dictionary of design images from design phase
            create_mockups: Whether to create contextual mockups
        """
        print("\n" + "=" * 60)
        print("PHASE 3: Preview & Visualization")
        print("=" * 60)
        
        if create_mockups:
            print("\n🏙️  Creating realistic mockups...")
            
            # Street scene mockup
            if "geometric" in designs:
                print("  • Street scene mockup...")
                street_mockup = self.preview_module.create_mockup_context(
                    designs["geometric"], 
                    context_type="street"
                )
                
                mockup_file = os.path.join(self.output_dir, "mockup_street")
                self.preview_module.export_all_formats(street_mockup, mockup_file)
            
            # Building mockup
            if "split" in designs:
                print("  • Building facade mockup...")
                building_mockup = self.preview_module.create_mockup_context(
                    designs["split"], 
                    context_type="building"
                )
                
                mockup_file = os.path.join(self.output_dir, "mockup_building")
                self.preview_module.export_all_formats(building_mockup, mockup_file)
        
        # Create comparison sheet
        if len(designs) > 1:
            print("\n📊 Creating design comparison sheet...")
            
            design_list = []
            labels = []
            
            for style, img in designs.items():
                resized = img.copy()
                resized.thumbnail((800, 800))
                design_list.append(resized)
                labels.append(f"{style.capitalize()} Style")
            
            comparison_file = os.path.join(self.output_dir, "design_comparison.png")
            self.preview_module.create_comparison_sheet(
                design_list, 
                labels, 
                comparison_file
            )
        
        print(f"\n✓ All previews exported to {self.output_dir}/")
    
    def run_complete_workflow(self, budget: float = 400, size: str = "3x10ft", 
                             text: str = "SUNSET GLOW") -> Dict:
        """
        Execute the complete banner agent workflow.
        
        Args:
            budget: Budget for banner
            size: Banner size
            text: Banner text
            
        Returns:
            Dictionary containing all results
        """
        print("\n" + "🌟" * 30)
        print("STREET BANNER AGENT - COMPLETE WORKFLOW")
        print("🌟" * 30)
        print(f"\nProject: {self.project_name}")
        print(f"Budget: ${budget:.2f}")
        print(f"Size: {size}")
        print(f"Text: {text}")
        print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        results = {}
        
        # Phase 1: Research
        pricing_summary = self.run_research_phase(export_data=True)
        results['pricing'] = pricing_summary
        
        # Get recommendations
        recommendations = self.get_budget_recommendations(budget=budget, size=size)
        results['recommendations'] = recommendations
        
        # Phase 2: Design
        design_results = self.run_design_phase(size=size, text=text)
        results['designs'] = design_results
        
        # Phase 3: Preview
        self.run_preview_phase(design_results['designs'], create_mockups=True)
        
        # Generate final report
        self._generate_final_report(results, budget, size, text)
        
        print("\n" + "=" * 60)
        print("✅ WORKFLOW COMPLETE")
        print("=" * 60)
        print(f"\n📁 All outputs saved to: {self.output_dir}/")
        print(f"📄 See project_report.txt for complete summary")
        
        return results
    
    def _generate_final_report(self, results: Dict, budget: float, 
                               size: str, text: str) -> None:
        """
        Generate a final project report.
        
        Args:
            results: Results from all workflow phases
            budget: Budget used
            size: Size used
            text: Text used
        """
        report_file = os.path.join(self.output_dir, "project_report.txt")
        
        with open(report_file, 'w') as f:
            f.write("=" * 60 + "\n")
            f.write("STREET BANNER PROJECT REPORT\n")
            f.write("=" * 60 + "\n\n")
            
            f.write(f"Project Name: {self.project_name}\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Banner Size: {size}\n")
            f.write(f"Banner Text: {text}\n")
            f.write(f"Budget: ${budget:.2f}\n\n")
            
            f.write("=" * 60 + "\n")
            f.write("PRICING ANALYSIS\n")
            f.write("=" * 60 + "\n\n")
            
            pricing = results['pricing']['overall']
            f.write(f"Price Range: ${pricing['min_price']:.2f} - ${pricing['max_price']:.2f}\n")
            f.write(f"Average Price: ${pricing['avg_price']:.2f}\n")
            f.write(f"Median Price: ${pricing['median_price']:.2f}\n\n")
            
            f.write("Recommendations:\n")
            for i, rec in enumerate(results.get('recommendations', [])[:3], 1):
                f.write(f"{i}. {rec['vendor']}: ${rec['total_cost']:.2f}\n")
                f.write(f"   Material: {rec['material']}, Turnaround: {rec['turnaround_days']} days\n")
            
            f.write("\n" + "=" * 60 + "\n")
            f.write("DESIGN SPECIFICATIONS\n")
            f.write("=" * 60 + "\n\n")
            
            specs = results['designs']['specifications']
            f.write(f"Resolution: {specs['resolution']['dpi']} DPI\n")
            f.write(f"Color Mode: {specs['resolution']['color_mode']}\n")
            f.write(f"Dimensions: {specs['dimensions']['width_inches']}\" x {specs['dimensions']['height_inches']}\"\n")
            f.write(f"Pixels: {specs['dimensions']['width_pixels']} x {specs['dimensions']['height_pixels']}\n\n")
            
            f.write("Color Palette:\n")
            f.write(f"  Grey-Blue RGB: {specs['color_palette']['grey_blue_rgb']}\n")
            f.write(f"  Orange RGB: {specs['color_palette']['orange_rgb']}\n\n")
            
            f.write("=" * 60 + "\n")
            f.write("GENERATED FILES\n")
            f.write("=" * 60 + "\n\n")
            
            f.write("Design Files:\n")
            f.write("  - design_gradient.png\n")
            f.write("  - design_split.png\n")
            f.write("  - design_geometric.png\n")
            f.write("  - design_print_ready.tif (CMYK)\n")
            f.write("  - design_vector.svg\n\n")
            
            f.write("Mockup Files:\n")
            f.write("  - mockup_street.[png/jpg/pdf]\n")
            f.write("  - mockup_building.[png/jpg/pdf]\n\n")
            
            f.write("Data Files:\n")
            f.write("  - pricing_data.csv\n")
            f.write("  - pricing_summary.json\n")
            f.write("  - design_specifications.json\n")
            f.write("  - design_comparison.png\n\n")
            
            f.write("=" * 60 + "\n")
        
        print(f"✓ Project report generated: {report_file}")


def main():
    """Main execution function."""
    print("\n" + "🎨" * 30)
    print("STREET BANNER RESEARCH & DESIGN AGENT")
    print("🎨" * 30)
    
    # Create agent
    agent = BannerAgent(project_name="sunset_glow_banner")
    
    # Run complete workflow
    results = agent.run_complete_workflow(
        budget=400,
        size="3x10ft",
        text="SUNSET GLOW"
    )
    
    print("\n" + "=" * 60)
    print("🎉 Agent execution complete!")
    print("=" * 60)
    print("\n💡 Next Steps:")
    print("  1. Review generated designs in the output folder")
    print("  2. Check pricing_data.csv for vendor comparisons")
    print("  3. Use design_print_ready.tif to submit to chosen vendor")
    print("  4. Show mockups to stakeholders for approval")
    print("\n:: ∎")


if __name__ == "__main__":
    main()
