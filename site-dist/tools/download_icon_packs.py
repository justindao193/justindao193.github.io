import urllib.request,zipfile,io
from pathlib import Path
urls={'powerplatform':'https://download.microsoft.com/download/498606aa-6d27-4f13-aa5c-1401078c153b/Power-Platform-icons-scalable.zip','github':'https://brand.github.com/GitHub_Logos.zip'}
for name,u in urls.items():
 try:
  raw=urllib.request.urlopen(u,timeout=25).read(); z=zipfile.ZipFile(io.BytesIO(raw));Path('tools/verification/'+name+'.zip').write_bytes(raw);print(name,z.namelist())
 except Exception as e:print(name,e)
