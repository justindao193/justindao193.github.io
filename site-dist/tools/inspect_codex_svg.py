from pathlib import Path
from bs4 import BeautifulSoup
s=BeautifulSoup(Path('tools/verification/codexdocs-assets.html').read_text(encoding='utf-8'),'html.parser')
for el in s.find_all('svg'):
 if any('codex' in str(el.get(x,'')).lower() for x in ['class','aria-label','data-icon','id']) or 'codex' in str(el.find('title')).lower():print(str(el)[:600])
print('near nav links')
for el in s.find_all('a',href='/codex')[:5]:print(str(el)[:1500])
