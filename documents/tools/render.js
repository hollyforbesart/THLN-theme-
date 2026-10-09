// Render a document HTML to PDF + per-page PNG previews, and report overflow.
// Usage: node tools/render.js <doc.html> <out.pdf> [preview_dir]
const path = require('path');
const { execSync } = require('child_process');
let pw;
try { pw = require('playwright'); } catch (e) { pw = require(execSync('npm root -g').toString().trim() + '/playwright'); }

(async () => {
  const [src, out, prev] = process.argv.slice(2);
  const browser = await pw.chromium.launch();
  const page = await browser.newPage({ viewport: { width: 816, height: 1056 }, deviceScaleFactor: 2 });
  await page.goto('file://' + path.resolve(src), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const issues = await page.evaluate(() => {
    const out = [];
    document.querySelectorAll('.page').forEach((pg, i) => {
      const pr = pg.getBoundingClientRect();
      pg.querySelectorAll('.flow').forEach(f => {
        if (f.scrollWidth > f.clientWidth + 1) out.push(`page ${i + 1}: flow overflows into an extra column`);
        // free space in the last column
        const last = [...f.querySelectorAll('p, h3, .find')].pop();
      });
      pg.querySelectorAll('*').forEach(el => {
        const r = el.getBoundingClientRect();
        if (r.height && r.bottom > pr.bottom + 0.5 && getComputedStyle(el).position !== 'absolute') out.push(`page ${i + 1}: ${el.tagName}.${el.className} ends ${Math.round(r.bottom - pr.bottom)}px below page`);
      });
    });
    return out;
  });
  console.log(issues.length ? issues.slice(0, 20).join('\n') : 'no overflow');
  await page.pdf({ path: out, width: '8.5in', height: '11in', printBackground: true, preferCSSPageSize: true });
  if (prev) {
    const n = await page.locator('.page').count();
    for (let i = 0; i < n; i++) await page.locator('.page').nth(i).screenshot({ path: `${prev}/p${i + 1}.png` });
  }
  await browser.close();
})();
