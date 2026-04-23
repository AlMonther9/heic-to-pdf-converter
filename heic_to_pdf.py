"""
Convert all HEIC images in the Book folder to a single PDF, sorted by date (filename).
Requires: pillow-heif, Pillow, fpdf2
Install with: pip install pillow-heif Pillow fpdf2
"""

import os
import sys
from pathlib import Path

# ── Dependencies check ──────────────────────────────────────────────────────
try:
    import pillow_heif
    from PIL import Image
    from fpdf import FPDF
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Run: pip install pillow-heif Pillow fpdf2")
    sys.exit(1)

# Register HEIC support with Pillow
pillow_heif.register_heif_opener()

# ── Config ──────────────────────────────────────────────────────────────────
BOOK_DIR = Path(__file__).parent / "Book"
OUTPUT_PDF = Path(__file__).parent / "Modern_Control_Book.pdf"

# ── Collect & sort HEIC files by filename (timestamp encoded in name) ───────
heic_files = sorted(
    BOOK_DIR.glob("*.heic"),
    key=lambda p: p.name  # filenames are YYYYMMDD_HHMMSS.heic → lexicographic == chronological
)

if not heic_files:
    print(f"No .heic files found in {BOOK_DIR}")
    sys.exit(1)

print(f"Found {len(heic_files)} HEIC files. Building PDF...")

# ── Build PDF ───────────────────────────────────────────────────────────────
pdf = FPDF(unit="pt")

for i, heic_path in enumerate(heic_files, 1):
    print(f"  [{i}/{len(heic_files)}] {heic_path.name}", end="\r")

    img = Image.open(heic_path)

    # Convert to RGB (HEIC may be RGBA or other modes)
    if img.mode != "RGB":
        img = img.convert("RGB")

    w_px, h_px = img.size
    # Use image's natural size in points (72 dpi baseline; keep aspect ratio)
    # Fit to A4 if image is huge, otherwise keep natural size
    MAX_W_PT = 595   # A4 width  in points
    MAX_H_PT = 842   # A4 height in points

    scale = min(MAX_W_PT / w_px, MAX_H_PT / h_px, 1.0)
    w_pt = w_px * scale
    h_pt = h_px * scale

    pdf.add_page(format=(w_pt, h_pt))

    # Save as temp JPEG in memory then embed
    import io
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=90)
    buf.seek(0)

    pdf.image(buf, x=0, y=0, w=w_pt, h=h_pt)

print(f"\nDone processing images. Saving PDF to: {OUTPUT_PDF}")
pdf.output(str(OUTPUT_PDF))
print(f"[DONE] PDF saved: {OUTPUT_PDF} ({OUTPUT_PDF.stat().st_size / 1024 / 1024:.1f} MB)")
