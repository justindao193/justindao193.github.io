import struct,json
from pathlib import Path
p=Path(r'C:\Program Files\WindowsApps\OpenAI.Codex_26.1023.6621.0_x64__2p2nqsd0c76g0\app\resources\app.asar')
with p.open('rb') as f:
 a=struct.unpack('<4I',f.read(16));print(a);h=json.loads(f.read(a[3]))
 def walk(d,prefix=''):
  for n,v in d.get('files',{}).items():
   path=prefix+n
   if 'files' in v:yield from walk(v,path+'/')
   elif ('codex' in n.lower() and n.endswith(('.png','.svg','.ico'))) or n=='index.html':yield path,v
 matches=list(walk(h));print([(n,v.get('size')) for n,v in matches][:30])
 for n,v in matches:
  if n.endswith('index.html') and v.get('size',0)<200000:
   f.seek(8+a[1]+int(v['offset']));data=f.read(v['size']);Path('tools/verification/codex-installed-index.html').write_bytes(data);print('extracted',n)
