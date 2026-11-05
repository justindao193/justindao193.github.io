from pathlib import Path
import re
s=Path('tools/verification/github-brand.html').read_text(encoding='utf-8')
print('\n'.join(re.findall(r'href="([^"]+)"',s)[-40:]))
