#!/usr/bin/env bash
# Rebuild generated files and package the theme for upload to WordPress.
# Usage (from the repo root):  bash tools/build_zip.sh
set -euo pipefail
cd "$(dirname "$0")/.."
python3 tools/build_patterns.py
python3 tools/build_editor_css.py
for f in thln-astra-child/functions.php thln-astra-child/inc/*.php; do php -l "$f" >/dev/null; done
mkdir -p dist
rm -f dist/thln-astra-child.zip
zip -qr dist/thln-astra-child.zip thln-astra-child -x '*.DS_Store'
ls -lh dist/thln-astra-child.zip
