# Installing the THLN theme on WordPress

This puts the redesign on thehairlossnutritionist.com without a staging site. The new theme installs **next to** your current "Astra Child" theme, so going back is one click.

Plan for about an hour at a quiet time of day. Steps 1–3 change nothing visitors see.

---

## Before you start

- **Download the theme zip:** `dist/thln-astra-child.zip` in this repository (on GitHub, open the file and click **Download raw file**). Don't unzip it.

---

## 1. Back up (5 min)

**UpdraftPlus → Backup Now**, with both "database" and "files" ticked. Wait until it says the backup is complete.

## 2. Upload the theme (2 min)

**Appearance → Themes → Add Theme → Upload Theme**, choose `thln-astra-child.zip`, **Install Now**.
Do **not** click Activate yet.

## 3. Look before you switch (optional, 5 min)

On the new "THLN Astra Child" theme, click **Live Preview**. You'll see your current pages with the new header, footer, fonts and colors. The new page layouts don't exist yet, so pages still have their old content. Close the preview when you're done.

## 4. Activate (1 min)

**Appearance → Themes → THLN Astra Child → Activate.**

From this moment visitors see the new header and footer. Your existing pages keep their content until you replace them in step 7. If anything looks badly wrong, jump to **Going back** below.

## 5. Site settings (5 min)

**Appearance → Customize:**

- **Site Identity → Logo.** Optional. The theme already shows your THLN logo. Only set this if you want a different file.
- **THLN Site Settings:** check the header button text ("Get My Hair Roadmap") and the **DEEP ROOTS Navigator link** (`https://navigator.thehairlossnutritionist.com`). Every "Get My Hair Roadmap" button on the site uses this one link, so if the Navigator ever moves, you change it here once. You can also edit the footer tagline and add an optional footer disclaimer.

**Appearance → Menus.** The header already shows Home, About, Blog, Resources and Contact. You only need a menu if you want to change those:
create a menu, add the pages, tick **Primary Menu** under "Menu Settings", Save. The two footer columns work the same way ("Footer: Explore" and "Footer: The fine print").

## 6. Resources (5 min)

In the admin sidebar there's a new **Resources** item.

Click **Resources**. A blue box offers **Add starter resources**: click it. This creates the Hair Growth Grocery Guide, both iron tools and the 10 Nutrients guide, with your copy, links, icons and covers. To change a card's picture later, open the resource and use the **Card image** box on the right.

To add a resource later, use **Resources → Add resource**. Pick its section (Guides & paid resources, Free tools or Free downloads), Free or Paid, then fill in the text, button and link. **Order** (right side) sorts cards within a section: 1 comes first. Nothing on the Resources page needs editing; new resources just appear.

## 7. Build the four pages (20–30 min)

Each page starts from a ready-made pattern with your finalized copy and images already in place.

**How to create a page from a pattern:** **Pages → Add New**. When the "Choose a pattern" window appears, pick the pattern below (they're under **THLN: Full pages**). If the window doesn't appear, click the **+** (top left) → **Patterns** → **THLN: Full pages**.

| Page | Pattern | Page address (slug) |
| --- | --- | --- |
| Home | Homepage (full page) | `home` |
| About | About page (full page) | `about` |
| Resources | Resources page (full page) | `shop` |
| Contact | Contact page (full page) | `contact` |

**Keeping your current addresses (/about/, /shop/, /contact/):** WordPress won't let two pages share an address. For each page you already have:

1. Open the **old** page → in the right sidebar change its URL/slug to e.g. `about-old` → switch it to **Draft** → Save.
2. Then give the **new** page the real slug (`about`, `shop`, `contact`) and **Publish**.

Your old pages stay in Pages as drafts in case you want anything from them.

**Contact form.** The Contact pattern has a dashed placeholder box where the form goes.

1. In **WPForms → Add New**, make a simple form (Name, Email, a "What's this about?" dropdown with *A question / A resource request / Partnership / Something else*, Message) and save it.
2. Back on the Contact page, click the placeholder, press **+**, search **WPForms**, choose your form, then delete the placeholder paragraph.

The theme styles the form to match.

**Make the new Home page the homepage.** **Settings → Reading → Your homepage displays → A static page**. Set **Homepage** to the new Home and **Posts page** to your Blog page. Save.

## 8. Clear caches and check (5 min)

Click **Purge SG Cache** in the top admin bar. (If Super Page Cache is still active, also use **Super Page Cache → Purge cache**. See "Good to know" for why you can remove it.)

Then open the site on your phone and on a computer, logged out (or in a private window). Click through Home, About, Blog, Resources and Contact, and send yourself a test message through the contact form.

---

## Going back

If something is badly wrong at any point:

1. **Appearance → Themes → Astra Child → Activate.**
2. If you already changed the homepage: **Settings → Reading** → set it back to your old homepage.
3. If you renamed old pages: change their slugs back and publish them again.
4. Purge the cache (Purge SG Cache).

Your old theme and pages are untouched, so this restores the site as it was. UpdraftPlus (step 1) is the safety net behind all of that.

---

## Editing day to day

- **Text:** click it on the page and type. Every section is ordinary WordPress blocks.
- **Images:** click the image → **Replace** (toolbar) → pick from your Media Library.
- **Buttons:** click the button → the link icon to change where it goes. A button linked to `#roadmap` always goes to the Navigator link from **THLN Site Settings**.
- **Button styles:** select a button → right sidebar → **Styles**: Fill, Outline, Light purple or Text link.
- **Linking a DEEP ROOTS tile to a blog post** (when the posts are ready): select the tile's label text → link icon → choose the post. The whole tile becomes clickable and shows "Read more →". Unlinked tiles stay as they are, so you can link them one at a time. ROOTS steps work the same way.
- **Adding a section to any page:** **+** → **Patterns** → **THLN: Sections** (hero, DEEP ROOTS grid, ROOTS framework, Navigator banner, plum quote band, and more).
- **The blog** keeps Astra's layout with the new fonts, colors, header and footer. Redesigning the blog index and article template is the next project.

## Good to know

- **Elementor:** your existing Elementor pages keep working. Build the new pages in the regular WordPress editor (don't click "Edit with Elementor" on them).
- **Theme updates:** when the theme changes, you'll get a new zip. Upload it the same way and WordPress offers to **Replace current with uploaded**. Your pages, resources and settings stay.
- **Page images:** images placed by the patterns load from the theme folder. They're fine to keep, or swap for Media Library copies with **Replace**.
- **One cache is enough.** Your site is hosted on SiteGround and doesn't use Cloudflare, so SiteGround's **Speed Optimizer** already does the page caching. **Super Page Cache** adds a second cache on top, which can make visitors see old versions of pages after you edit. Recommended: Super Page Cache → **Purge cache**, then **Plugins → Deactivate** it, check the site still loads, and delete it a week later. In **Speed Optimizer → Caching**, make sure **Dynamic Caching** is on.
- **Code snippets:** snippets in WPCode or Code Snippets keep running under the new theme. A snippet written for Astra's old header or footer (for example, CSS that styles the old menu) would no longer apply.
