"""
Sunset Glow Banner Design Module

This module creates street banner designs with the specified color palette
and print-ready specifications.
"""

from PIL import Image, ImageDraw, ImageFont, ImageColor
import svgwrite
from typing import Tuple, Optional
import os


class SunsetGlowDesigner:
    """
    Design module for creating print-ready street banner designs
    with the Sunset Glow color palette.
    """
    
    # Color Palette Specifications
    COLORS = {
        "grey_blue": (90, 120, 140),      # RGB(90,120,140) - bottom half
        "orange": (255, 140, 50),          # RGB(255,140,50) - highlights
        "white": (255, 255, 255),
        "dark_grey": (45, 60, 70),         # Complementary color
        "light_orange": (255, 180, 100),   # Lighter accent
    }
    
    # CMYK conversions (approximations for reference)
    COLORS_CMYK = {
        "grey_blue": (36, 14, 0, 45),      # C:36% M:14% Y:0% K:45%
        "orange": (0, 45, 80, 0),          # C:0% M:45% Y:80% K:0%
    }
    
    # Design constraints
    DPI = 300
    COLOR_MODE = "RGB"  # PIL works in RGB, convert to CMYK for print
    
    # Standard banner sizes in inches
    BANNER_SIZES = {
        "3x10ft": (36, 120),    # inches
        "4x12ft": (48, 144),    # inches
        "2x8ft": (24, 96),      # inches
        "5x15ft": (60, 180),    # inches
    }
    
    def __init__(self, size: str = "3x10ft"):
        """
        Initialize designer with specified banner size.
        
        Args:
            size: Banner size key from BANNER_SIZES
        """
        if size not in self.BANNER_SIZES:
            raise ValueError(f"Invalid size. Choose from: {list(self.BANNER_SIZES.keys())}")
        
        self.size = size
        self.width_inches, self.height_inches = self.BANNER_SIZES[size]
        self.width_px = self.width_inches * self.DPI
        self.height_px = self.height_inches * self.DPI
    
    def create_gradient_background(self) -> Image.Image:
        """
        Create a gradient background transitioning from grey-blue to orange.
        
        Returns:
            PIL Image with gradient background
        """
        img = Image.new('RGB', (self.width_px, self.height_px), self.COLORS["white"])
        draw = ImageDraw.Draw(img)
        
        # Create vertical gradient
        for y in range(self.height_px):
            # Calculate blend factor (0 to 1)
            if y < self.height_px // 2:
                # Bottom half - grey-blue dominant
                factor = y / (self.height_px // 2)
                r = int(self.COLORS["grey_blue"][0] + (self.COLORS["orange"][0] - self.COLORS["grey_blue"][0]) * factor * 0.3)
                g = int(self.COLORS["grey_blue"][1] + (self.COLORS["orange"][1] - self.COLORS["grey_blue"][1]) * factor * 0.3)
                b = int(self.COLORS["grey_blue"][2] + (self.COLORS["orange"][2] - self.COLORS["grey_blue"][2]) * factor * 0.3)
            else:
                # Top half - transition to orange highlights
                factor = (y - self.height_px // 2) / (self.height_px // 2)
                r = int(self.COLORS["grey_blue"][0] + (self.COLORS["light_orange"][0] - self.COLORS["grey_blue"][0]) * factor)
                g = int(self.COLORS["grey_blue"][1] + (self.COLORS["light_orange"][1] - self.COLORS["grey_blue"][1]) * factor)
                b = int(self.COLORS["grey_blue"][2] + (self.COLORS["light_orange"][2] - self.COLORS["grey_blue"][2]) * factor)
            
            draw.line([(0, y), (self.width_px, y)], fill=(r, g, b))
        
        return img
    
    def create_solid_split_background(self) -> Image.Image:
        """
        Create a split background: grey-blue bottom, orange top highlights.
        
        Returns:
            PIL Image with split background
        """
        img = Image.new('RGB', (self.width_px, self.height_px), self.COLORS["white"])
        draw = ImageDraw.Draw(img)
        
        # Bottom half - grey-blue
        draw.rectangle(
            [(0, self.height_px // 2), (self.width_px, self.height_px)],
            fill=self.COLORS["grey_blue"]
        )
        
        # Top section - orange highlights with fade
        mid_point = self.height_px // 2
        accent_height = self.height_px // 4
        
        # Orange accent bar
        draw.rectangle(
            [(0, mid_point - accent_height), (self.width_px, mid_point)],
            fill=self.COLORS["orange"]
        )
        
        # Top section - lighter blend
        draw.rectangle(
            [(0, 0), (self.width_px, mid_point - accent_height)],
            fill=self.COLORS["light_orange"]
        )
        
        return img
    
    def add_geometric_elements(self, img: Image.Image) -> Image.Image:
        """
        Add geometric design elements to the banner.
        
        Args:
            img: Base image to add elements to
            
        Returns:
            Image with geometric elements
        """
        draw = ImageDraw.Draw(img)
        
        # Add diagonal stripes for visual interest
        stripe_width = self.width_px // 20
        
        for i in range(0, self.width_px + self.height_px, stripe_width * 3):
            # Orange stripes
            points = [
                (i, 0),
                (i + stripe_width, 0),
                (i + stripe_width - self.height_px, self.height_px),
                (i - self.height_px, self.height_px)
            ]
            draw.polygon(points, fill=(*self.COLORS["orange"], 50))  # Semi-transparent
        
        return img
    
    def add_text(self, img: Image.Image, text: str, position: str = "center") -> Image.Image:
        """
        Add text to the banner design.
        
        Args:
            img: Base image
            text: Text to add
            position: Text position ('top', 'center', 'bottom')
            
        Returns:
            Image with text
        """
        draw = ImageDraw.Draw(img)
        
        # Calculate font size based on banner dimensions
        font_size = self.height_px // 10
        
        try:
            # Try to use a nice font if available
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
        except:
            # Fallback to default font
            font = ImageFont.load_default()
        
        # Get text bounding box
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # Calculate position
        x = (self.width_px - text_width) // 2
        
        if position == "top":
            y = self.height_px // 8
        elif position == "bottom":
            y = self.height_px - self.height_px // 8 - text_height
        else:  # center
            y = (self.height_px - text_height) // 2
        
        # Add text shadow for better readability
        shadow_offset = font_size // 30
        draw.text((x + shadow_offset, y + shadow_offset), text, font=font, fill=self.COLORS["dark_grey"])
        
        # Add main text
        draw.text((x, y), text, font=font, fill=self.COLORS["white"])
        
        return img
    
    def create_design(self, text: str = "", style: str = "gradient") -> Image.Image:
        """
        Create complete banner design.
        
        Args:
            text: Text to display on banner
            style: Design style ('gradient', 'split', 'geometric')
            
        Returns:
            Complete banner design
        """
        if style == "gradient":
            img = self.create_gradient_background()
        elif style == "split":
            img = self.create_solid_split_background()
        elif style == "geometric":
            img = self.create_solid_split_background()
            img = self.add_geometric_elements(img)
        else:
            img = self.create_gradient_background()
        
        if text:
            img = self.add_text(img, text)
        
        return img
    
    def export_png(self, img: Image.Image, filename: str):
        """
        Export design as high-resolution PNG.
        
        Args:
            img: Image to export
            filename: Output filename
        """
        img.save(filename, "PNG", dpi=(self.DPI, self.DPI))
        print(f"✓ PNG exported: {filename} ({self.DPI} DPI)")
    
    def export_cmyk_tiff(self, img: Image.Image, filename: str):
        """
        Export design as CMYK TIFF for professional printing.
        
        Args:
            img: Image to export
            filename: Output filename
        """
        # Convert RGB to CMYK
        cmyk_img = img.convert('CMYK')
        cmyk_img.save(filename, "TIFF", dpi=(self.DPI, self.DPI), compression="tiff_lzw")
        print(f"✓ CMYK TIFF exported: {filename} ({self.DPI} DPI)")
    
    def create_svg_design(self, filename: str, text: str = ""):
        """
        Create vector SVG design for scalability.
        
        Args:
            filename: Output filename
            text: Text to display
        """
        dwg = svgwrite.Drawing(filename, size=(f"{self.width_inches}in", f"{self.height_inches}in"))
        
        # Add definitions for gradients
        gradient = dwg.defs.add(dwg.linearGradient(id="sunset_gradient", x1="0%", y1="0%", x2="0%", y2="100%"))
        gradient.add_stop_color(offset="0%", color=f"rgb{self.COLORS['light_orange']}")
        gradient.add_stop_color(offset="40%", color=f"rgb{self.COLORS['orange']}")
        gradient.add_stop_color(offset="100%", color=f"rgb{self.COLORS['grey_blue']}")
        
        # Add background rectangle with gradient
        dwg.add(dwg.rect(
            insert=(0, 0),
            size=(f"{self.width_inches}in", f"{self.height_inches}in"),
            fill="url(#sunset_gradient)"
        ))
        
        # Add text if provided
        if text:
            font_size = self.height_inches * 72 / 10  # Convert to points
            dwg.add(dwg.text(
                text,
                insert=(f"{self.width_inches/2}in", f"{self.height_inches/2}in"),
                text_anchor="middle",
                dominant_baseline="middle",
                font_size=f"{font_size}pt",
                font_family="Arial, sans-serif",
                font_weight="bold",
                fill="white",
                stroke="rgb(45,60,70)",
                stroke_width="2"
            ))
        
        dwg.save()
        print(f"✓ SVG exported: {filename}")
    
    def get_design_specifications(self) -> dict:
        """
        Get complete design specifications for print vendor.
        
        Returns:
            Dictionary with all design specifications
        """
        return {
            "dimensions": {
                "size": self.size,
                "width_inches": self.width_inches,
                "height_inches": self.height_inches,
                "width_pixels": self.width_px,
                "height_pixels": self.height_px
            },
            "resolution": {
                "dpi": self.DPI,
                "color_mode": "CMYK (for print)",
                "working_mode": "RGB"
            },
            "color_palette": {
                "grey_blue_rgb": self.COLORS["grey_blue"],
                "orange_rgb": self.COLORS["orange"],
                "grey_blue_cmyk": self.COLORS_CMYK["grey_blue"],
                "orange_cmyk": self.COLORS_CMYK["orange"]
            },
            "file_formats": {
                "raster": ["PNG (300 DPI)", "TIFF CMYK (300 DPI)"],
                "vector": ["SVG"]
            },
            "print_specifications": {
                "material_recommendations": ["vinyl", "mesh", "polyester"],
                "finishing": "hemmed edges with grommets",
                "bleed": "2 inches recommended"
            }
        }


def main():
    """Main execution function for design module."""
    print("=" * 60)
    print("Sunset Glow Banner Design Module")
    print("=" * 60)
    
    # Create designer for 3x10ft banner
    designer = SunsetGlowDesigner(size="3x10ft")
    
    # Display specifications
    print("\n📐 Design Specifications:")
    specs = designer.get_design_specifications()
    print(f"  Size: {specs['dimensions']['size']}")
    print(f"  Dimensions: {specs['dimensions']['width_inches']}\" x {specs['dimensions']['height_inches']}\"")
    print(f"  Resolution: {specs['resolution']['dpi']} DPI")
    print(f"  Pixels: {specs['dimensions']['width_pixels']} x {specs['dimensions']['height_pixels']}")
    
    print("\n🎨 Color Palette:")
    print(f"  Grey-Blue: RGB{specs['color_palette']['grey_blue_rgb']}")
    print(f"  Orange: RGB{specs['color_palette']['orange_rgb']}")
    
    # Create designs
    print("\n🖼️  Creating banner designs...")
    
    # Gradient design
    print("  • Gradient style...")
    gradient_design = designer.create_design(text="SUNSET GLOW", style="gradient")
    designer.export_png(gradient_design, "banner_gradient_300dpi.png")
    
    # Split design
    print("  • Split style...")
    split_design = designer.create_design(text="SUNSET GLOW", style="split")
    designer.export_png(split_design, "banner_split_300dpi.png")
    
    # Geometric design
    print("  • Geometric style...")
    geometric_design = designer.create_design(text="SUNSET GLOW", style="geometric")
    designer.export_png(geometric_design, "banner_geometric_300dpi.png")
    designer.export_cmyk_tiff(geometric_design, "banner_geometric_cmyk.tif")
    
    # Create SVG
    print("  • Vector SVG...")
    designer.create_svg_design("banner_design.svg", text="SUNSET GLOW")
    
    print("\n✅ All designs created successfully!")
    print("\n📁 Generated files:")
    print("  - banner_gradient_300dpi.png")
    print("  - banner_split_300dpi.png")
    print("  - banner_geometric_300dpi.png")
    print("  - banner_geometric_cmyk.tif (print-ready)")
    print("  - banner_design.svg (vector)")
    print("=" * 60)


if __name__ == "__main__":
    main()
