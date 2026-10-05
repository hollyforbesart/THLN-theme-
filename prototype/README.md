# THLN redesign — static prototype

Static prototype of the redesigned The Hair Loss Nutritionist site. It sets the visual system and layouts before the build moves into an Astra child theme.

## Pages

| File | Page |
| --- | --- |
| `index.html` | Homepage (priority). Uses the finalized homepage copy. |
| `about.html` | About. Uses the finalized About copy. |
| `blog.html` | Blog index |
| `article.html` | Representative blog article (reading template) |
| `resources.html` | Resources (lives at `/shop/` in WordPress; nav label is "Resources"). Order: paid guides, Navigator, free tools, free downloads. |
| `contact.html` | Contact: copy from the About page's Talk to Me section, plus a contact form |

Open any file in a browser, or serve the folder: `python3 -m http.server` from `prototype/`.

## Structure

```
prototype/
  assets/css/thln.css   design system: tokens, type, layout, components
  assets/js/thln.js     progressive enhancement only (mobile menu, header line, blog filter, article TOC)
  assets/fonts/         Manrope variable font, self-hosted (OFL)
  assets/img/           optimized WebP copies of the supplied assets in the repo root
```

The original PNGs in the repo root are untouched. `assets/img` holds trimmed, resized WebP versions.

## Design system in one place

- **Color**: the five brand colors only, plus white. Deep plum for text, buttons and high-contrast sections. Medium purple is used for accents and the plum-section button, never for body text on cream. A darker `--purple-ink` (#6B4A8E) is used for small eyebrow text on light backgrounds so it passes contrast.
- **Type**: Manrope, one family, weights 400–800. H1 40→64px, H2 30→44px, H3 22→26px, body 17→18px, eyebrows 13px uppercase with 0.16em tracking. Sizes use `clamp()` so mobile gets its own composition instead of a straight scale-down.
- **Section rhythm (home)**: cream hero → plum problem → cream DEEP ROOTS → lavender ROOTS → sand path → white Holly → plum closing CTA → cream footer.
- **Cards** appear only where content really is a collection (blog posts, resources). Framework and story sections sit directly on the page.

## Placeholders to replace

Image assets still owed are tracked in [`ASSETS-NEEDED.md`](ASSETS-NEEDED.md).

- **Holly's photograph**: not in the repo yet. `.photo-placeholder` marks where it goes on Home and About (4:5 portrait).
- **Blog**: intro copy, topic list and all article titles/excerpts are layout placeholders. The sample article body is written only to exercise the reading template. They don't need replacing in the prototype: in WordPress the blog index, article template and topic buttons are filled automatically from the real posts, featured images and categories.
- **Resources**: the iron tools, 10 Nutrients download and Grocery Guide link to their live pages. Their short descriptions (and the full 10 Nutrients title) still need writing and are shown with striped `.tbd` highlighting. No prices are shown.
- **Contact form** doesn't send in the prototype. In WordPress it becomes a form plugin (Fluent Forms, WPForms or similar) dropped into the page.
- **Links**: footer legal links point to `#`.

## Copy notes

Supplied copy is used as written, except for obvious typos fixed in the About page ("vis asking" → "via asking", "forCCCA" → "for CCCA") and a stray "okay" removed from the end of the footer tagline. Flag if any of those should go back.

## Moving into WordPress

The WordPress version is built: see `thln-astra-child/` (the Astra child theme), `dist/thln-astra-child.zip` (upload this) and [`WORDPRESS-INSTALL.md`](../WORDPRESS-INSTALL.md) (step-by-step install and editing guide).

Page copy for the WordPress patterns lives in `tools/build_patterns.py`. After changing it, or any theme file, run `bash tools/build_zip.sh` to regenerate the patterns and editor CSS and rebuild the zip.
