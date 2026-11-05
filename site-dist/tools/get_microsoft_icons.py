from playwright.sync_api import sync_playwright
from pathlib import Path
urls={'excel':'https://www.microsoft.com/content/dam/microsoft/bade/images/icons/en-us/m365-app-icons-fy26/Excel-Icon-FY26.svg','sharepoint':'https://www.microsoft.com/content/dam/microsoft/bade/images/icons/en-us/m365-app-icons-fy26/SharePoint-Icon-FY26.svg'}
with sync_playwright() as p:
 b=p.chromium.launch(executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe',headless=True)
 page=b.new_page(accept_downloads=True)
 for name,url in urls.items():
  with page.expect_download() as d:
   try:page.goto(url)
   except Exception:pass
  d.value.save_as('about/tools/'+name+'.svg');print(name,'downloaded',flush=True)
 b.close()
