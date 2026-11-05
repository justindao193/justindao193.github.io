import urllib.request
from pathlib import Path
for name,u in [('tableau.ico','https://public.tableau.com/favicon.ico'),('codex.ico','https://chatgpt.com/codex/favicon.ico')]:
 try:
  r=urllib.request.urlopen(u,timeout=15);data=r.read();print(name,r.headers.get('Content-Type'),len(data));Path('tools/verification/'+name).write_bytes(data)
 except Exception as e:print(e)
