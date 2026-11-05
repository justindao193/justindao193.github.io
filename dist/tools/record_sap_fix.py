import json
from pathlib import Path
p=Path('references/Carryon-Icon-Sources-2026-10-31.json');d=json.loads(p.read_text());d['sources']['sap.png']='https://ui5.sap.com/resources/sap/ui/core/mimes/logo/sap_50x26.png';p.write_text(json.dumps(d,indent=2),encoding='utf-8')
