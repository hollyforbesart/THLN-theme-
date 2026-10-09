# THLN documents

| PDF | Source |
| --- | --- |
| `dist/food-for-your-follicles.pdf` (free, 5 pages) | `food-for-your-follicles.html` |
| `dist/mane-meals-everyday-edition.pdf` (paid, 7 pages) | `tools/build_mane_meals.py` + `tools/mane_meals_template.html` |

Both are US Letter HTML print layouts in the Manrope font, rendered to PDF with Chromium (Playwright).

## Rebuilding

```sh
python3 tools/build_tags_css.py         # only after changing tag colors in tools/tags.py
python3 tools/build_mane_meals.py       # Mane Meals copy and meal data live here
node tools/render.js food-for-your-follicles.html dist/food-for-your-follicles.pdf
node tools/render.js mane-meals.html dist/mane-meals-everyday-edition.pdf
```

`render.js` reports any text that overflows a page.

## Assets

- `tools/tags.py`: the 10 nutrient tag colors, shared by both documents.
- `assets/icons/`: icons cut from `Pastel Nutrition Icon Grid.png` and recolored to the tag colors (`tools/cut_icons.py`).
- `assets/photos/`: meal photos from the Mane Meals docx, square-cropped with a light shared grade (`tools/prep_photos.py`).
