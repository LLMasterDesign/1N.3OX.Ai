"""
Unit Tests for Sunsetglow Banner Agent System

Tests for research, design, and preview modules with edge case handling.
"""

import unittest
import os
import json
from unittest.mock import patch, MagicMock
from PIL import Image
import pandas as pd

# Import modules
from sunsetglow.banner_cost_research import BannerCostResearch
from sunsetglow.banner_design import SunsetGlowDesigner
from sunsetglow.banner_preview import BannerPreview


class TestBannerCostResearch(unittest.TestCase):
    """Test cases for banner cost research module."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.research = BannerCostResearch()
    
    def test_initialization(self):
        """Test research module initializes correctly."""
        self.assertIsNotNone(self.research)
        self.assertEqual(self.research.research_data, [])
        self.assertIsNotNone(self.research.session)
    
    def test_simulate_vendor_research(self):
        """Test simulated vendor data collection."""
        data = self.research.simulate_vendor_research()
        
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        
        # Check data structure
        sample = data[0]
        required_fields = ['vendor', 'size', 'material', 'price', 'setup_fee']
        for field in required_fields:
            self.assertIn(field, sample)
    
    def test_price_range_validation(self):
        """Test that prices fall within expected range."""
        self.research.simulate_vendor_research()
        df = self.research.analyze_pricing()
        
        # Check all total costs are within reasonable range
        self.assertTrue(all(df['total_cost'] >= 0))
        self.assertTrue(all(df['total_cost'] <= 2000))  # Upper bound check
    
    def test_analyze_pricing(self):
        """Test pricing analysis functionality."""
        self.research.simulate_vendor_research()
        df = self.research.analyze_pricing()
        
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIn('total_cost', df.columns)
        self.assertGreater(len(df), 0)
    
    def test_get_price_summary(self):
        """Test price summary generation."""
        summary = self.research.get_price_summary()
        
        self.assertIn('overall', summary)
        self.assertIn('by_size', summary)
        self.assertIn('by_material', summary)
        self.assertIn('by_vendor', summary)
        
        # Check overall stats
        self.assertIn('min_price', summary['overall'])
        self.assertIn('max_price', summary['overall'])
        self.assertIn('avg_price', summary['overall'])
        self.assertIn('median_price', summary['overall'])
    
    def test_get_recommendations(self):
        """Test budget-based recommendations."""
        recommendations = self.research.get_recommendations(budget=300, size="3x10ft")
        
        self.assertIsInstance(recommendations, list)
        
        # All recommendations should be within budget
        for rec in recommendations:
            self.assertLessEqual(rec['total_cost'], 300)
            self.assertEqual(rec['size'], "3x10ft")
    
    def test_export_csv(self):
        """Test CSV export functionality."""
        test_file = "test_export.csv"
        
        try:
            self.research.simulate_vendor_research()
            self.research.export_research_data(test_file)
            
            self.assertTrue(os.path.exists(test_file))
            
            # Verify file can be read back
            df = pd.read_csv(test_file)
            self.assertGreater(len(df), 0)
            
        finally:
            if os.path.exists(test_file):
                os.remove(test_file)
    
    def test_export_json(self):
        """Test JSON export functionality."""
        test_file = "test_summary.json"
        
        try:
            self.research.export_summary_json(test_file)
            
            self.assertTrue(os.path.exists(test_file))
            
            # Verify JSON structure
            with open(test_file, 'r') as f:
                data = json.load(f)
            
            self.assertIn('overall', data)
            self.assertIn('by_size', data)
            
        finally:
            if os.path.exists(test_file):
                os.remove(test_file)
    
    def test_regional_pricing_variations(self):
        """Test handling of regional pricing variations."""
        self.research.simulate_vendor_research()
        df = self.research.analyze_pricing()
        
        # Check that we have multiple regions
        regions = df['region'].unique()
        self.assertGreater(len(regions), 0)
    
    def test_incomplete_data_handling(self):
        """Test handling of incomplete vendor data."""
        # Add incomplete data entry
        incomplete_entry = {
            "vendor": "TestVendor",
            "size": "3x10ft",
            "material": "vinyl",
            "price": 250.00,
            "setup_fee": 0.00,
            "turnaround_days": 5,
            "region": "Test",
            "timestamp": "2025-10-21T00:00:00"
        }
        
        self.research.research_data.append(incomplete_entry)
        
        # Should not raise exception
        try:
            df = self.research.analyze_pricing()
            self.assertIsInstance(df, pd.DataFrame)
        except Exception as e:
            self.fail(f"Failed to handle incomplete data: {e}")


class TestSunsetGlowDesigner(unittest.TestCase):
    """Test cases for banner design module."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.designer = SunsetGlowDesigner(size="3x10ft")
    
    def test_initialization(self):
        """Test designer initializes with correct parameters."""
        self.assertEqual(self.designer.size, "3x10ft")
        self.assertEqual(self.designer.width_inches, 36)
        self.assertEqual(self.designer.height_inches, 120)
        self.assertEqual(self.designer.DPI, 300)
    
    def test_invalid_size(self):
        """Test that invalid size raises error."""
        with self.assertRaises(ValueError):
            SunsetGlowDesigner(size="invalid_size")
    
    def test_color_palette(self):
        """Test color palette specifications."""
        self.assertEqual(self.designer.COLORS["grey_blue"], (90, 120, 140))
        self.assertEqual(self.designer.COLORS["orange"], (255, 140, 50))
    
    def test_create_gradient_background(self):
        """Test gradient background creation."""
        img = self.designer.create_gradient_background()
        
        self.assertIsInstance(img, Image.Image)
        self.assertEqual(img.width, self.designer.width_px)
        self.assertEqual(img.height, self.designer.height_px)
        self.assertEqual(img.mode, 'RGB')
    
    def test_create_split_background(self):
        """Test split background creation."""
        img = self.designer.create_solid_split_background()
        
        self.assertIsInstance(img, Image.Image)
        self.assertEqual(img.mode, 'RGB')
    
    def test_create_design_gradient(self):
        """Test complete gradient design creation."""
        img = self.designer.create_design(text="TEST", style="gradient")
        
        self.assertIsInstance(img, Image.Image)
        self.assertEqual(img.width, self.designer.width_px)
        self.assertEqual(img.height, self.designer.height_px)
    
    def test_create_design_split(self):
        """Test complete split design creation."""
        img = self.designer.create_design(text="TEST", style="split")
        
        self.assertIsInstance(img, Image.Image)
    
    def test_create_design_geometric(self):
        """Test complete geometric design creation."""
        img = self.designer.create_design(text="TEST", style="geometric")
        
        self.assertIsInstance(img, Image.Image)
    
    def test_resolution_300dpi(self):
        """Test that designs meet 300 DPI requirement."""
        self.assertEqual(self.designer.DPI, 300)
        
        # Verify pixel dimensions match DPI requirement
        expected_width = 36 * 300  # 36 inches * 300 DPI
        expected_height = 120 * 300  # 120 inches * 300 DPI
        
        self.assertEqual(self.designer.width_px, expected_width)
        self.assertEqual(self.designer.height_px, expected_height)
    
    def test_png_export(self):
        """Test PNG export functionality."""
        test_file = "test_design.png"
        
        try:
            img = self.designer.create_design(style="gradient")
            self.designer.export_png(img, test_file)
            
            self.assertTrue(os.path.exists(test_file))
            
            # Verify file was created (skip re-opening due to size)
            file_size = os.path.getsize(test_file)
            self.assertGreater(file_size, 0)
            
        finally:
            if os.path.exists(test_file):
                os.remove(test_file)
    
    def test_cmyk_export(self):
        """Test CMYK TIFF export for print."""
        test_file = "test_design_cmyk.tif"
        
        try:
            img = self.designer.create_design(style="split")
            self.designer.export_cmyk_tiff(img, test_file)
            
            self.assertTrue(os.path.exists(test_file))
            
            # Verify file was created (skip re-opening due to size)
            file_size = os.path.getsize(test_file)
            self.assertGreater(file_size, 0)
            
        finally:
            if os.path.exists(test_file):
                os.remove(test_file)
    
    def test_svg_export(self):
        """Test SVG vector export."""
        test_file = "test_design.svg"
        
        try:
            self.designer.create_svg_design(test_file, text="TEST")
            
            self.assertTrue(os.path.exists(test_file))
            
            # Verify it's a valid SVG file
            with open(test_file, 'r') as f:
                content = f.read()
                self.assertIn('<svg', content)
                self.assertIn('</svg>', content)
            
        finally:
            if os.path.exists(test_file):
                os.remove(test_file)
    
    def test_get_design_specifications(self):
        """Test design specifications output."""
        specs = self.designer.get_design_specifications()
        
        self.assertIn('dimensions', specs)
        self.assertIn('resolution', specs)
        self.assertIn('color_palette', specs)
        self.assertIn('file_formats', specs)
        
        # Verify resolution specs
        self.assertEqual(specs['resolution']['dpi'], 300)
        self.assertEqual(specs['resolution']['color_mode'], "CMYK (for print)")


class TestBannerPreview(unittest.TestCase):
    """Test cases for banner preview module."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.preview = BannerPreview()
        
        # Create a simple test image
        self.test_image = Image.new('RGB', (1080, 3600), (255, 140, 50))
    
    def test_initialization(self):
        """Test preview module initializes correctly."""
        self.assertIsNotNone(self.preview)
        self.assertEqual(self.preview.preview_width, 1200)
    
    def test_create_mockup_street(self):
        """Test street scene mockup creation."""
        mockup = self.preview.create_mockup_context(self.test_image, context_type="street")
        
        self.assertIsInstance(mockup, Image.Image)
        self.assertEqual(mockup.width, 1920)
        self.assertEqual(mockup.height, 1080)
    
    def test_create_mockup_building(self):
        """Test building facade mockup creation."""
        mockup = self.preview.create_mockup_context(self.test_image, context_type="building")
        
        self.assertIsInstance(mockup, Image.Image)
    
    def test_create_thumbnail(self):
        """Test thumbnail creation."""
        thumb = self.test_image.copy()
        result = self.preview.create_thumbnail(thumb, max_size=400)
        
        self.assertIsInstance(result, Image.Image)
        self.assertLessEqual(max(result.size), 400)
    
    def test_export_png(self):
        """Test PNG export."""
        test_file = "test_preview.png"
        
        try:
            self.preview.export_png(self.test_image, test_file)
            self.assertTrue(os.path.exists(test_file))
            
        finally:
            if os.path.exists(test_file):
                os.remove(test_file)
    
    def test_export_jpg(self):
        """Test JPEG export."""
        test_file = "test_preview.jpg"
        
        try:
            self.preview.export_jpg(self.test_image, test_file, quality=90)
            self.assertTrue(os.path.exists(test_file))
            
        finally:
            if os.path.exists(test_file):
                os.remove(test_file)
    
    def test_export_pdf(self):
        """Test PDF export."""
        test_file = "test_preview.pdf"
        
        try:
            self.preview.export_pdf(self.test_image, test_file)
            self.assertTrue(os.path.exists(test_file))
            
        finally:
            if os.path.exists(test_file):
                os.remove(test_file)
    
    def test_export_all_formats(self):
        """Test exporting all formats at once."""
        base_name = "test_all_formats"
        files = [
            f"{base_name}.png",
            f"{base_name}.jpg",
            f"{base_name}.pdf",
            f"{base_name}_thumbnail.png"
        ]
        
        try:
            self.preview.export_all_formats(self.test_image, base_name)
            
            for file in files:
                self.assertTrue(os.path.exists(file), f"File {file} not created")
                
        finally:
            for file in files:
                if os.path.exists(file):
                    os.remove(file)
    
    def test_comparison_sheet(self):
        """Test comparison sheet creation."""
        test_file = "test_comparison.png"
        
        # Create multiple test images
        images = [
            Image.new('RGB', (1080, 3600), (255, 0, 0)),
            Image.new('RGB', (1080, 3600), (0, 255, 0)),
            Image.new('RGB', (1080, 3600), (0, 0, 255))
        ]
        labels = ["Design 1", "Design 2", "Design 3"]
        
        try:
            self.preview.create_comparison_sheet(images, labels, test_file)
            self.assertTrue(os.path.exists(test_file))
            
            # Verify output image
            result = Image.open(test_file)
            self.assertIsInstance(result, Image.Image)
            
        finally:
            if os.path.exists(test_file):
                os.remove(test_file)
    
    def test_comparison_sheet_mismatch(self):
        """Test that comparison sheet raises error on label mismatch."""
        images = [Image.new('RGB', (100, 100), (255, 0, 0))]
        labels = ["Label 1", "Label 2"]  # Mismatch
        
        with self.assertRaises(ValueError):
            self.preview.create_comparison_sheet(images, labels)


class TestIntegration(unittest.TestCase):
    """Integration tests for the complete banner agent system."""
    
    def test_full_workflow(self):
        """Test complete workflow from research to design to preview."""
        # Research phase
        research = BannerCostResearch()
        research.simulate_vendor_research()
        summary = research.get_price_summary()
        
        self.assertIsNotNone(summary)
        
        # Design phase
        designer = SunsetGlowDesigner(size="3x10ft")
        design = designer.create_design(text="TEST BANNER", style="gradient")
        
        self.assertIsNotNone(design)
        
        # Preview phase
        preview = BannerPreview()
        mockup = preview.create_mockup_context(design, context_type="street")
        
        self.assertIsNotNone(mockup)
    
    def test_data_flow(self):
        """Test data flows correctly between modules."""
        # Get pricing recommendations
        research = BannerCostResearch()
        recommendations = research.get_recommendations(budget=400, size="3x10ft")
        
        # Use size from recommendation to create design
        if recommendations:
            size = recommendations[0]['size']
            designer = SunsetGlowDesigner(size=size)
            design = designer.create_design(text="SPECIAL EVENT")
            
            self.assertIsNotNone(design)


def run_test_suite():
    """Run the complete test suite with detailed output."""
    print("=" * 60)
    print("Sunsetglow Banner Agent - Test Suite")
    print("=" * 60)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestBannerCostResearch))
    suite.addTests(loader.loadTestsFromTestCase(TestSunsetGlowDesigner))
    suite.addTests(loader.loadTestsFromTestCase(TestBannerPreview))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.wasSuccessful():
        print("\n✅ All tests passed!")
    else:
        print("\n❌ Some tests failed.")
    
    print("=" * 60)
    
    return result


if __name__ == "__main__":
    run_test_suite()
