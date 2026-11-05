import urllib.request,re,concurrent.futures
from pathlib import Path
urls={'codexdocs':'https://developers.openai.com/codex','css':'https://www.w3.org/Style/CSS/','sap':'https://www.sap.com/design-system/','tableau':'https://www.tableau.com/about/media-relations','microsoftnews':'https://techcommunity.microsoft.com/blog/microsoft365insiderblog/new-microsoft-365-icons-for-the-ai-era/4458674'}
def f(item):
 k,u=item
 try:
  s=urllib.request.urlopen(u,timeout=15).read().decode();Path('tools/verification/'+k+'-assets.html').write_text(s,encoding='utf-8');print(k,re.findall(r'(?:src|href)=[\"\']([^\"\']*(?:logo|icon|favicon)[^\"\']*)',s)[:30],flush=True)
 except Exception as e:print(k,e,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:list(ex.map(f,urls.items()))
