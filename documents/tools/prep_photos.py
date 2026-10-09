"""Square-crop and lightly grade the Mane Meals photos so they read as one set.

Usage: python3 -I prep_photos.py <media_dir> <out_dir>
"""
import sys
from pathlib import Path
from PIL import Image, ImageEnhance

SIZE = 600
# name: (center x, center y, crop size as a fraction of the short side)
CROPS = {
    "image1": (0.55, 0.5, 1.0),
    "image6": (0.5, 0.52, 0.82),
    "image17": (0.47, 0.5, 0.9),
    "image20": (0.55, 0.5, 0.92),
}

src, out = Path(sys.argv[1]), Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=True)
for f in sorted(src.glob("image*.*")):
    im = Image.open(f).convert("RGB")
    w, h = im.size
    cx, cy, k = CROPS.get(f.stem, (0.5, 0.5, 1.0))
    s = int(min(w, h) * k)
    x = min(max(int(cx * w - s / 2), 0), w - s)
    y = min(max(int(cy * h - s / 2), 0), h - s)
    im = im.crop((x, y, x + s, y + s)).resize((SIZE, SIZE), Image.LANCZOS)
    # Light, shared grade: a touch less saturation and a faint warm lift.
    im = ImageEnhance.Color(im).enhance(0.94)
    warm = Image.new("RGB", im.size, (250, 238, 222))
    im = Image.blend(im, warm, 0.05)
    im.save(out / f"{f.stem}.jpg", quality=84, optimize=True, progressive=True)
    print(f.stem, (w, h), "->", out / f"{f.stem}.jpg")
