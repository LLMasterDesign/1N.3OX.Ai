"""
Banner Preview and Visualization Module

This module provides mockup rendering and multi-format export capabilities
for street banner designs.
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import io
from typing import Tuple, Optional
import os


class BannerPreview:
    """
    Visualization module for rendering banner mockups and exporting
    to multiple formats.
    """
    
    def __init__(self):
        """Initialize the preview module."""
        self.preview_width = 1200  # Preview image width in pixels
        self.preview_quality = 95  # JPEG quality for previews
    
    def create_mockup_context(self, banner_img: Image.Image, 
                             context_type: str = "street") -> Image.Image:
        """
        Create a realistic mockup of the banner in context.
        
        Args:
            banner_img: The banner design image
            context_type: Type of mockup context ('street', 'building', 'event')
            
        Returns:
            Mockup image with banner in context
        """
        # Create canvas for mockup
        canvas_width = 1920
        canvas_height = 1080
        canvas = Image.new('RGB', (canvas_width, canvas_height), (240, 240, 245))
        
        # Resize banner for mockup (maintain aspect ratio)
        banner_width = int(canvas_width * 0.6)
        aspect_ratio = banner_img.height / banner_img.width
        banner_height = int(banner_width * aspect_ratio)
        
        banner_resized = banner_img.resize((banner_width, banner_height), Image.Resampling.LANCZOS)
        
        # Add perspective effect
        banner_with_perspective = self._add_perspective(banner_resized)
        
        # Add shadow
        banner_with_shadow = self._add_shadow(banner_with_perspective)
        
        # Create context background
        if context_type == "street":
            bg = self._create_street_background(canvas_width, canvas_height)
        elif context_type == "building":
            bg = self._create_building_background(canvas_width, canvas_height)
        else:
            bg = canvas
        
        # Composite banner onto background
        x_pos = (canvas_width - banner_with_shadow.width) // 2
        y_pos = (canvas_height - banner_with_shadow.height) // 2
        
        bg.paste(banner_with_shadow, (x_pos, y_pos), banner_with_shadow if banner_with_shadow.mode == 'RGBA' else None)
        
        return bg
    
    def _add_perspective(self, img: Image.Image, angle: float = 5.0) -> Image.Image:
        """
        Add subtle perspective effect to make banner look more realistic.
        
        Args:
            img: Input image
            angle: Perspective angle in degrees
            
        Returns:
            Image with perspective effect
        """
        # Convert to RGBA for transparency
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Simple perspective: slight rotation
        rotated = img.rotate(angle, expand=True, fillcolor=(0, 0, 0, 0))
        
        return rotated
    
    def _add_shadow(self, img: Image.Image, offset: Tuple[int, int] = (10, 10)) -> Image.Image:
        """
        Add drop shadow to banner.
        
        Args:
            img: Input image
            offset: Shadow offset (x, y)
            
        Returns:
            Image with shadow
        """
        # Ensure RGBA mode
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Create shadow layer
        shadow = Image.new('RGBA', 
                          (img.width + offset[0] * 2, img.height + offset[1] * 2),
                          (0, 0, 0, 0))
        
        # Create shadow shape
        shadow_mask = Image.new('L', img.size, 0)
        shadow_draw = ImageDraw.Draw(shadow_mask)
        shadow_draw.rectangle([(0, 0), img.size], fill=100)
        
        # Blur the shadow
        shadow_mask = shadow_mask.filter(ImageFilter.GaussianBlur(radius=15))
        
        # Paste shadow
        shadow.paste(shadow_mask, offset, shadow_mask)
        
        # Paste original image on top
        shadow.paste(img, (offset[0], offset[1]), img)
        
        return shadow
    
    def _create_street_background(self, width: int, height: int) -> Image.Image:
        """
        Create a simple street scene background.
        
        Args:
            width: Background width
            height: Background height
            
        Returns:
            Street background image
        """
        bg = Image.new('RGB', (width, height), (135, 170, 200))  # Sky blue
        draw = ImageDraw.Draw(bg)
        
        # Ground
        draw.rectangle([(0, height * 2 // 3), (width, height)], fill=(100, 100, 100))
        
        # Buildings silhouette
        building_heights = [height // 3, height // 2, height * 2 // 5, height // 4]
        building_width = width // len(building_heights)
        
        for i, h in enumerate(building_heights):
            x1 = i * building_width
            x2 = (i + 1) * building_width
            y1 = height * 2 // 3 - h
            draw.rectangle([(x1, y1), (x2, height * 2 // 3)], fill=(60, 70, 80))
            
            # Windows
            for w_y in range(int(y1) + 20, int(height * 2 // 3), 30):
                for w_x in range(int(x1) + 15, int(x2), 25):
                    if (w_x + w_y) % 2 == 0:  # Some windows lit
                        draw.rectangle([(w_x, w_y), (w_x + 10, w_y + 15)], fill=(255, 230, 150))
                    else:
                        draw.rectangle([(w_x, w_y), (w_x + 10, w_y + 15)], fill=(40, 50, 60))
        
        return bg
    
    def _create_building_background(self, width: int, height: int) -> Image.Image:
        """
        Create a building facade background.
        
        Args:
            width: Background width
            height: Background height
            
        Returns:
            Building background image
        """
        bg = Image.new('RGB', (width, height), (180, 170, 160))  # Concrete
        draw = ImageDraw.Draw(bg)
        
        # Add brick pattern
        brick_height = 20
        brick_width = 60
        
        for y in range(0, height, brick_height):
            offset = brick_width // 2 if (y // brick_height) % 2 else 0
            for x in range(-brick_width, width + brick_width, brick_width):
                draw.rectangle(
                    [(x + offset, y), (x + offset + brick_width - 2, y + brick_height - 2)],
                    fill=(160, 150, 140),
                    outline=(140, 130, 120)
                )
        
        return bg
    
    def create_thumbnail(self, img: Image.Image, max_size: int = 400) -> Image.Image:
        """
        Create thumbnail preview of banner.
        
        Args:
            img: Input image
            max_size: Maximum dimension for thumbnail
            
        Returns:
            Thumbnail image
        """
        img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
        return img
    
    def export_png(self, img: Image.Image, filename: str, optimize: bool = True):
        """
        Export as PNG with optimization.
        
        Args:
            img: Image to export
            filename: Output filename
            optimize: Whether to optimize file size
        """
        img.save(filename, "PNG", optimize=optimize)
        file_size = os.path.getsize(filename) / 1024  # KB
        print(f"✓ PNG exported: {filename} ({file_size:.1f} KB)")
    
    def export_jpg(self, img: Image.Image, filename: str, quality: int = 95):
        """
        Export as JPEG for web preview.
        
        Args:
            img: Image to export
            filename: Output filename
            quality: JPEG quality (0-100)
        """
        # Convert RGBA to RGB for JPEG
        if img.mode == 'RGBA':
            rgb_img = Image.new('RGB', img.size, (255, 255, 255))
            rgb_img.paste(img, mask=img.split()[3] if len(img.split()) == 4 else None)
            img = rgb_img
        
        img.save(filename, "JPEG", quality=quality, optimize=True)
        file_size = os.path.getsize(filename) / 1024  # KB
        print(f"✓ JPEG exported: {filename} ({file_size:.1f} KB)")
    
    def export_pdf(self, img: Image.Image, filename: str):
        """
        Export as PDF for print submission.
        
        Args:
            img: Image to export
            filename: Output filename
        """
        # Convert RGBA to RGB for PDF
        if img.mode == 'RGBA':
            rgb_img = Image.new('RGB', img.size, (255, 255, 255))
            rgb_img.paste(img, mask=img.split()[3] if len(img.split()) == 4 else None)
            img = rgb_img
        
        img.save(filename, "PDF", resolution=100.0)
        file_size = os.path.getsize(filename) / 1024  # KB
        print(f"✓ PDF exported: {filename} ({file_size:.1f} KB)")
    
    def export_all_formats(self, img: Image.Image, base_filename: str):
        """
        Export image in all supported formats.
        
        Args:
            img: Image to export
            base_filename: Base filename (without extension)
        """
        print(f"\n📦 Exporting '{base_filename}' in all formats...")
        
        self.export_png(img, f"{base_filename}.png")
        self.export_jpg(img, f"{base_filename}.jpg", quality=self.preview_quality)
        self.export_pdf(img, f"{base_filename}.pdf")
        
        # Create thumbnail
        thumb = img.copy()
        self.create_thumbnail(thumb, max_size=400)
        self.export_png(thumb, f"{base_filename}_thumbnail.png")
        
        print(f"✓ All formats exported for '{base_filename}'")
    
    def create_comparison_sheet(self, images: list, labels: list, 
                               output_filename: str = "comparison_sheet.png"):
        """
        Create a comparison sheet showing multiple designs side by side.
        
        Args:
            images: List of images to compare
            labels: List of labels for each image
            output_filename: Output filename
        """
        if len(images) != len(labels):
            raise ValueError("Number of images must match number of labels")
        
        # Calculate layout
        num_images = len(images)
        cols = min(3, num_images)
        rows = (num_images + cols - 1) // cols
        
        # Resize all images to same height
        target_height = 600
        resized_images = []
        for img in images:
            aspect_ratio = img.width / img.height
            new_width = int(target_height * aspect_ratio)
            resized = img.resize((new_width, target_height), Image.Resampling.LANCZOS)
            resized_images.append(resized)
        
        # Calculate canvas size
        max_width = max(img.width for img in resized_images)
        canvas_width = max_width * cols + 40 * (cols + 1)
        canvas_height = target_height * rows + 80 * rows + 40
        
        # Create canvas
        canvas = Image.new('RGB', (canvas_width, canvas_height), (250, 250, 250))
        draw = ImageDraw.Draw(canvas)
        
        # Place images
        for idx, (img, label) in enumerate(zip(resized_images, labels)):
            row = idx // cols
            col = idx % cols
            
            x = 40 + col * (max_width + 40)
            y = 40 + row * (target_height + 80)
            
            # Add border
            draw.rectangle(
                [(x - 2, y - 2), (x + img.width + 2, y + img.height + 2)],
                outline=(200, 200, 200),
                width=2
            )
            
            # Paste image
            canvas.paste(img, (x, y))
            
            # Add label
            try:
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
            except:
                font = ImageFont.load_default()
            
            label_bbox = draw.textbbox((0, 0), label, font=font)
            label_width = label_bbox[2] - label_bbox[0]
            label_x = x + (img.width - label_width) // 2
            label_y = y + img.height + 10
            
            draw.text((label_x, label_y), label, fill=(50, 50, 50), font=font)
        
        # Save comparison sheet
        canvas.save(output_filename, "PNG")
        print(f"✓ Comparison sheet created: {output_filename}")


def main():
    """Main execution function for preview module."""
    print("=" * 60)
    print("Banner Preview and Visualization Module")
    print("=" * 60)
    
    # Import design module to get sample banner
    try:
        from sunsetglow_banner_design import SunsetGlowDesigner
        
        # Create sample designs
        print("\n🎨 Creating sample banner designs...")
        designer = SunsetGlowDesigner(size="3x10ft")
        
        gradient_design = designer.create_design(text="SUNSET GLOW", style="gradient")
        split_design = designer.create_design(text="SUNSET GLOW", style="split")
        geometric_design = designer.create_design(text="SUNSET GLOW", style="geometric")
        
        # Initialize preview module
        preview = BannerPreview()
        
        # Create mockups
        print("\n🖼️  Creating mockup visualizations...")
        
        print("  • Street scene mockup...")
        street_mockup = preview.create_mockup_context(geometric_design, context_type="street")
        preview.export_all_formats(street_mockup, "mockup_street_scene")
        
        print("  • Building facade mockup...")
        building_mockup = preview.create_mockup_context(split_design, context_type="building")
        preview.export_all_formats(building_mockup, "mockup_building")
        
        # Create comparison sheet
        print("\n📊 Creating design comparison sheet...")
        designs = [gradient_design, split_design, geometric_design]
        labels = ["Gradient Style", "Split Style", "Geometric Style"]
        
        # Resize for comparison (reduce size for sheet)
        comparison_designs = []
        for design in designs:
            resized = design.copy()
            resized.thumbnail((800, 800), Image.Resampling.LANCZOS)
            comparison_designs.append(resized)
        
        preview.create_comparison_sheet(comparison_designs, labels, "design_comparison.png")
        
        print("\n✅ All previews and mockups created successfully!")
        print("\n📁 Generated files:")
        print("  - mockup_street_scene.png/.jpg/.pdf + thumbnail")
        print("  - mockup_building.png/.jpg/.pdf + thumbnail")
        print("  - design_comparison.png")
        
    except ImportError:
        print("\n⚠️  Design module not found. Creating demo preview...")
        
        # Create a simple demo banner
        demo_banner = Image.new('RGB', (1080, 3600), (255, 140, 50))
        draw = ImageDraw.Draw(demo_banner)
        draw.rectangle([(0, 1800), (1080, 3600)], fill=(90, 120, 140))
        
        preview = BannerPreview()
        demo_mockup = preview.create_mockup_context(demo_banner, context_type="street")
        preview.export_all_formats(demo_mockup, "demo_mockup")
        
        print("✓ Demo mockup created: demo_mockup.png/.jpg/.pdf")
    
    print("=" * 60)


if __name__ == "__main__":
    main()
