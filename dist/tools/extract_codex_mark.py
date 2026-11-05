import struct,json
from pathlib import Path
p=Path(r'C:\Program Files\WindowsApps\OpenAI.Codex_26.1023.6621.0_x64__2p2nqsd0c76g0\app\resources\app.asar')
with p.open('rb') as f:
 a=struct.unpack('<4I',f.read(16));h=json.loads(f.read(a[3]))
 for n in ['codex-d905da579253.svg','codex-app-ga-logo-3e5209898ca3.png']:
  v=h['files']['webview']['files']['assets']['files'][n];f.seek(8+a[1]+int(v['offset']));data=f.read(v['size']);Path('tools/verification/'+n).write_bytes(data)
 print(Path('tools/verification/codex-d905da579253.svg').read_text()[:1000])
