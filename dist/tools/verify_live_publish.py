import urllib.request,hashlib,json
from pathlib import Path
for f in ['index.html','housing.html','housing/media/housing-film.mp4']:
 try:
  data=urllib.request.urlopen('https://justindao193.github.io/'+f+'?v=8e27e90',timeout=20).read()
  local=Path(f).read_bytes()
  if f.endswith('.html'):
   data=data.replace(b'\r\n',b'\n');local=local.replace(b'\r\n',b'\n')
  print(f,'matches local:',hashlib.sha256(data).digest()==hashlib.sha256(local).digest())
 except Exception as e:print(f,str(e))
