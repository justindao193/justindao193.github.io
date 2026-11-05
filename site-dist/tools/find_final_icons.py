import urllib.request,json,re,concurrent.futures
urls={'codextree':'https://api.github.com/repos/openai/codex/git/trees/main?recursive=1','tableau':'https://public.tableau.com/app/discover','sap':'https://ui5.sap.com/resources/sap/ui/core/mimes/logo/icotxt_white_220x72_blue.png'}
def f(item):
 k,u=item
 try:
  raw=urllib.request.urlopen(u,timeout=20).read()
  if k=='codextree': print(k,[x['path'] for x in json.loads(raw)['tree'] if any(t in x['path'].lower() for t in ['logo','icon.png','icon.svg'])][:40],flush=True)
  elif k=='sap':
   from pathlib import Path
   Path('about/tools/sap.png').write_bytes(raw);print(k,len(raw),flush=True)
  else:print(k,re.findall(r'(?:href|src)="([^"]*(?:logo|icon)[^"]*)"',raw.decode())[:30],flush=True)
 except Exception as e:print(k,e,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:list(ex.map(f,urls.items()))
