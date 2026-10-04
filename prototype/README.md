# THLN redesign — static prototype

Static prototype of the redesigned The Hair Loss Nutritionist site. It sets the visual system and layouts before the build moves into an Astra child theme.

## Pages

| File | Page |
| --- | --- |
| `index.html` | Homepage (priority). Uses the finalized homepage copy. |
| `about.html` | About. Uses the finalized About copy. |
| `blog.html` | Blog index |
| `article.html` | Representative blog article (reading template) |
| `resources.html` | Resources (lives at `/shop/` in WordPress; nav label is "Resources") |

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

- **Holly's photograph**: not in the repo yet. `.photo-placeholder` marks where it goes on Home and About (4:5 portrait).
- **Blog**: intro copy, topic list and all article titles/excerpts are layout placeholders. The sample article body is written only to exercise the reading template.
- **Resources**: names and descriptions for the two iron tools, the free download and the Grocery Guide description are not finalized. They are shown with striped `.tbd` highlighting. No prices are shown.
- **Links**: footer legal links, Contact Me and resource links point to `#`.

## Copy notes

Supplied copy is used as written, except for obvious typos fixed in the About page ("vis asking" → "via asking", "forCCCA" → "for CCCA") and a stray "okay" removed from the end of the footer tagline. Flag if any of those should go back.

## Moving into WordPress (Astra child theme)

The goal: Holly edits words, images, links and resources in WordPress; the theme only controls look and behavior.

**Theme owns** (`thln-astra-child/`)
- `style.css` → port of `thln.css` tokens and components
- `theme.json` → palette (5 brand colors + white), Manrope font family and the type scale, content width 680px / wide 1240px, spacing scale. This makes the brand colors and sizes show up as the only choices in the editor.
- Header/footer: Astra Header/Footer Builder configured with the logo, the 4 menu items (a WP menu, so editable) and a button set to the Navigator URL, styled by the child theme.
- `single.php` / block template for posts: TOC + 680px prose column + sticky Navigator aside.
- Blog archive template: featured latest post, 3-up grid with a fixed 3:2 image ratio, category pills from real categories, Navigator band after the first 6 posts.
- Block styles: `is-style-callout-takeaway`, `is-style-callout-note`, `is-style-callout-care` on the core Group block; `is-style-pull` on core Quote; `is-style-eyebrow` on Paragraph.

**Block patterns** (core blocks only, inserted once and then edited in place)
- Home hero, Problem/noise list, DEEP ROOTS grid, ROOTS track, Path forward, Holly split, Closing CTA, Navigator band, Inline article CTA.
- Each pattern is built from Group / Columns / Heading / Paragraph / Image / Buttons / List, so all text, images and links stay editable. The homepage is a normal page assembled from these patterns, not a hard-coded template.

**Resources (`/shop/`)**
- A `thln_resource` custom post type with fields: type (Tool, Quiz, Download, Guide), access (Free / Paid), short description, image, button label, URL, opens-externally flag, and menu order for sorting.
- The page uses Query Loop blocks filtered by type, one per section (Tools, Downloads, Guides), so adding, removing or reordering a resource never touches code. Card layout varies by type through block variations, and grids use `auto-fill` so any count works.
- The Navigator feature block at the top is a pattern, not a resource entry, so it always keeps top priority.
- No WooCommerce. Paid guides link out to Kit or another checkout.

**Navigator**: every "Get My Hair Roadmap" button points to `https://navigator.thehairlossnutritionist.com`. Keep that URL in one place (a theme option or a reusable synced pattern) so it can change once.
