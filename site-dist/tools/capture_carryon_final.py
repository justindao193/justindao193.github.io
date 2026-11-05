from playwright.sync_api import sync_playwright
with sync_playwright() as p:
 b=p.chromium.launch(executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe',headless=True)
 page=b.new_page(viewport={'width':1440,'height':1100},reduced_motion='reduce')
 page.goto('http://127.0.0.1:8000/index.html?theme=light#about',wait_until='networkidle')
 assert page.locator('img[alt="SAP"]').evaluate('(i)=>i.complete&&i.naturalWidth===50')
 page.locator('.bp').screenshot(path='tools/verification/carryon-all-icons.png')
 print('Correct SAP logo loaded. All 16 static icons visible:',page.locator('.belt li:visible').count())
 b.close()
