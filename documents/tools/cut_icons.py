"""Cut the 10 nutrient icons out of 'Pastel Nutrition Icon Grid.png' and
recolor each background circle to its tag color. Usage:
  python3 -I cut_icons.py <grid.png> <out_dir>"""
import sys, os
from collections import deque
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tags import TAGS
from PIL import Image, ImageDraw

src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGB")
W, H = im.size
px = im.load()

def is_bg(p):  # the page around the circles is near-white
    return min(p) > 246

# Find circle boxes: scan each grid cell (5 cols x 2 rows), ignore label rows.
cells = []
for row, (y0, y1) in enumerate([(90, 415), (500, 825)]):
    for col in range(5):
        x0, x1 = int(col * W / 5), int((col + 1) * W / 5)
        xs, ys = [], []
        for y in range(y0, y1, 2):
            for x in range(x0, x1, 2):
                if not is_bg(px[x, y]):
                    xs.append(x); ys.append(y)
        cells.append((min(xs), min(ys), max(xs), max(ys)))

def hexrgb(h): return tuple(int(h[i:i+2], 16) for i in range(1, 7, 2))

for (slug, label, bg, ink), (x0, y0, x1, y1) in zip(TAGS, cells):
    # The circle is the tallest/widest consistent shape; take a square around its center.
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    # Snap to the grid: columns and rows are evenly spaced.
    i = TAGS.index((slug, label, bg, ink))
    cx = [164, 468, 768, 1070, 1372][i % 5]
    cy = [268, 675][i // 5]
    r = 150  # all circles in the grid are the same size
    box = (int(cx - r), int(cy - r), int(cx + r), int(cy + r))
    tile = im.crop(box).convert("RGBA")
    tp = tile.load()
    n = tile.size[0]
    # Circle fill color: sample just inside the circle edge at several angles, take the most common.
    import math
    samples = []
    for a in range(0, 360, 15):
        sx = int(n / 2 + (n / 2 - 14) * math.cos(math.radians(a)))
        sy = int(n / 2 + (n / 2 - 14) * math.sin(math.radians(a)))
        samples.append(tp[sx, sy][:3])
    fill = max(set(samples), key=samples.count)
    target = hexrgb(bg)
    # Flood fill from the ring just inside the edge: replace pixels close to the circle fill.
    def close(p, ref, tol=22):
        return sum(abs(p[i] - ref[i]) for i in range(3)) <= tol
    seen = bytearray(n * n)
    q = deque()
    for a in range(0, 360, 3):
        sx = int(n / 2 + (n / 2 - 12) * math.cos(math.radians(a)))
        sy = int(n / 2 + (n / 2 - 12) * math.sin(math.radians(a)))
        if close(tp[sx, sy], fill):
            q.append((sx, sy)); seen[sy * n + sx] = 1
    while q:
        x, y = q.popleft()
        p = tp[x, y]
        # keep the original light/dark variation (soft gradients) by shifting toward target
        d = tuple(p[i] - fill[i] for i in range(3))
        tp[x, y] = tuple(max(0, min(255, target[i] + d[i])) for i in range(3)) + (255,)
        for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if 0 <= nx < n and 0 <= ny < n and not seen[ny * n + nx]:
                seen[ny * n + nx] = 1
                if close(tp[nx, ny], fill):
                    q.append((nx, ny))
    # Round mask so the page background around the circle is transparent.
    big = Image.new("L", (n * 4, n * 4), 0)
    ImageDraw.Draw(big).ellipse((6, 6, n * 4 - 7, n * 4 - 7), fill=255)
    mask = big.resize((n, n), Image.LANCZOS)
    tile.putalpha(mask)
    tile.save(os.path.join(out, f"{slug}.png"))
    print(slug, box, "fill", fill)
