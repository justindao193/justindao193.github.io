from pathlib import Path
import re
s=Path('tools/verification/codexdocs-assets.html').read_text(encoding='utf-8')
for match in re.finditer(r'codex.{0,100}(?:svg|png)|(?:svg|png).{0,80}codex',s,re.I):
 t=match.group(0)
 if 'icons/' not in t: print(t[:180])
