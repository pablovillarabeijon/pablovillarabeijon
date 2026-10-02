"""Write the canonical URL for Quarto from GitHub Pages metadata."""
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

base = sys.argv[1].rstrip('/') + '/'
parsed = urlparse(base)
if parsed.scheme != 'https' or not parsed.netloc:
    raise SystemExit('A real HTTPS Pages URL is required.')
Path('_quarto-ci.yml').write_text(json.dumps({'website': {'site-url': base}}, indent=2))
Path('robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: ' + base + 'sitemap.xml\n')
