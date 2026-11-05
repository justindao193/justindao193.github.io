from playwright.sync_api import sync_playwright
with sync_playwright() as p:
 b=p.chromium.launch(executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe',headless=True)
 page=b.new_page(viewport={'width':1440,'height':1000})
 for name in ['index.html','instacart.html']:
  page.goto('http://127.0.0.1:8000/'+name,wait_until='networkidle')
  print(name,page.evaluate('''() => [...document.images].filter(i=>i.getAttribute('src') && i.loading!=='lazy' && (!i.complete || !i.naturalWidth)).map(i=>i.src)'''))
 page.goto('http://127.0.0.1:8000/housing.html',wait_until='networkidle')
 page.screenshot(path='tools/verification/publish-housing-desktop.png')
 b.close()
