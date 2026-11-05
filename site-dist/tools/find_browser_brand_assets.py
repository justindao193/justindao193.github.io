from playwright.sync_api import sync_playwright
from pathlib import Path
with sync_playwright() as p:
 b=p.chromium.launch(executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe',headless=True)
 page=b.new_page()
 for name,url in [('excel','https://www.microsoft.com/en-us/microsoft-365/excel'),('sharepoint','https://www.microsoft.com/en-us/microsoft-365/sharepoint/collaboration'),('codex','https://openai.com/codex/')]:
  try:
   page.goto(url,wait_until='domcontentloaded',timeout=20000)
   Path('tools/verification/'+name+'-browser.html').write_text(page.content(),encoding='utf-8')
   print(name,page.title(),page.locator('link[rel*=icon]').evaluate_all('(es)=>es.map(e=>e.href)'))
   print(page.locator('img').evaluate_all('(es)=>es.filter(e=>/logo|icon|excel|sharepoint/i.test(e.src)).map(e=>({src:e.src,alt:e.alt})).slice(0,25)'))
  except Exception as e:print(name,str(e)[:150])
 b.close()
