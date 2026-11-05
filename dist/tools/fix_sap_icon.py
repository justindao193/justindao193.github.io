import urllib.request,concurrent.futures
from pathlib import Path
urls=['https://ui5.sap.com/resources/sap/ui/core/mimes/logo/sap_50x26.png','https://ui5.sap.com/resources/sap/ui/core/mimes/logo/sap_73x36.gif','https://ui5.sap.com/resources/sap/ui/core/themes/base/img/SAPLogo.svg','https://www.sap.com/dam/application/shared/logos/sap-logo-svg.svg','https://dam.sap.com/asset/90e133b9-7b7d-0010-82c7-eda71af511fa/preview']
def f(u):
 try:
  r=urllib.request.urlopen(u,timeout=8);d=r.read();print(u,r.headers.get('Content-Type'),len(d),flush=True)
  if 'sap_50' in u:Path('tools/verification/sap-correct.png').write_bytes(d)
 except Exception as e:print(u,str(e),flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:list(ex.map(f,urls))
