import urllib.request,re,concurrent.futures
from html.parser import HTMLParser
pages={'excel':'https://www.microsoft.com/en-us/microsoft-365/excel','sharepoint':'https://www.microsoft.com/en-us/microsoft-365/sharepoint/collaboration','powerbi':'https://www.microsoft.com/en-us/power-platform/products/power-bi','automate':'https://www.microsoft.com/en-us/power-platform/products/power-automate','dynamics':'https://www.microsoft.com/en-us/dynamics-365','claude':'https://claude.com','codex':'https://openai.com/codex/','figma':'https://www.figma.com/','tableau':'https://www.tableau.com','sap':'https://www.sap.com','github':'https://github.com/logos'}
class P(HTMLParser):
 def handle_starttag(self,t,a):
  d=dict(a)
  if t in ['img','link']:
   src=d.get('src') or d.get('href','')
   if any(x in src.lower() for x in ['icon','logo','brand','favicon']): print(self.name,str(d)[:700])
def run(item):
 k,u=item
 try:
  s=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=20).read().decode()
  from pathlib import Path
  Path('tools/verification/'+k+'-brand.html').write_text(s,encoding='utf-8')
  p=P();p.name=k;p.feed(s)
 except Exception as e: print(k,str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:list(pool.map(run,pages.items()))
