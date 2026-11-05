import urllib.request
from pathlib import Path
u='https://raw.githubusercontent.com/lobehub/lobe-icons/master/packages/static-svg/icons/codex.svg'
try:
 data=urllib.request.urlopen(u).read();print(data.decode()[:300]);Path('tools/verification/codex-candidate.svg').write_bytes(data)
except Exception as e:print(e)
