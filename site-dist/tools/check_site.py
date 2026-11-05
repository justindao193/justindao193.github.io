"""Check local root-page asset references without fetching external URLs."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('src', 'href', 'poster') and value:
                self.refs.append(value)

def main():
    missing = []
    pages = list(ROOT.glob('*.html'))
    for page in pages:
        parser = Links()
        parser.feed(page.read_text(encoding='utf-8'))
        for ref in parser.refs:
            url = urlsplit(ref)
            if url.scheme or url.netloc or not url.path:
                continue
            target = ROOT / unquote(url.path.lstrip('/')) if url.path.startswith('/') else page.parent / unquote(url.path)
            if not target.exists():
                missing.append(f'{page.name}: {ref}')
    print(f'Checked {len(pages)} root HTML pages.')
    for item in missing:
        print('Missing:', item)
    return bool(missing)

if __name__ == '__main__':
    raise SystemExit(main())
