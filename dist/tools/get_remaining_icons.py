from playwright.sync_api import sync_playwright
from pathlib import Path
import urllib.request,zipfile,io
urls={'excel':'https://www.microsoft.com/content/dam/microsoft/bade/images/icons/en-us/m365-app-icons-fy26/Excel-Icon-FY26.svg','sharepoint':'https://www.microsoft.com/content/dam/microsoft/bade/images/icons/en-us/m365-app-icons-fy26/SharePoint-Icon-FY26.svg','sap':'https://www.sap.com/dam/application/shared/logos/sap-logo-svg.svg.adapt.svg/1493030643828.svg','tableau':'https://www.tableau.com/themes/custom/tableau_www/logo.v2.svg'}
with sync_playwright() as p:
 b=p.chromium.launch(executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe',headless=True)
 page=b.new_page()
 for name,url in urls.items():
  try:
   r=page.goto(url,wait_until='load',timeout=20000);data=r.body()
   if b'<svg' in data:Path('about/tools/'+name+'.svg').write_bytes(data);print(name,'saved',len(data),flush=True)
   else:print(name,r.status,flush=True)
  except Exception as e:print(name,str(e)[:100],flush=True)
 page.goto('https://developers.openai.com/codex/app',wait_until='domcontentloaded')
 print('codex assets',page.locator('img').evaluate_all('(es)=>es.map(e=>({src:e.src,alt:e.alt}))'),flush=True)
 print('codex svgs',page.locator('a[href="/codex"] svg').evaluate_all('(es)=>es.map(e=>e.outerHTML)'),flush=True)
 Path('tools/verification/codex-app.html').write_text(page.content(),encoding='utf-8')
 b.close()
u='https://download.microsoft.com/download/498606aa-6d27-4f13-aa5c-1401078c153b/Dynamics-365-icons-scalable.zip'
z=zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(u).read()));Path('about/tools/dynamics-365.svg').write_bytes(z.read('Dynamics 365 Product Family Icons/Dynamics365_scalable.svg'))
