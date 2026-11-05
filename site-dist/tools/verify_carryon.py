from playwright.sync_api import sync_playwright
from pathlib import Path
import json
out=Path('tools/verification')
with sync_playwright() as p:
 b=p.chromium.launch(executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe',headless=True)
 page=b.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)));checks=[]
 for theme in ['light','dark']:
  for width in [390,800,1150,1440,1920]:
   page.set_viewport_size({'width':width,'height':1100})
   page.goto(f'http://127.0.0.1:8000/index.html?theme={theme}#about',wait_until='networkidle')
   page.locator('.bp').scroll_into_view_if_needed()
   page.wait_for_timeout(350)
   checks.append({'width':width,'theme':theme,**page.evaluate('''() => ({overflow:document.documentElement.scrollWidth>innerWidth,icons:[...document.querySelectorAll('.belt img')].every(i=>i.complete&&i.naturalWidth>0),labels:[...document.querySelectorAll('.belt li')].every(i=>i.innerText===''),unique:document.querySelectorAll('.belt li:not(.belt-copy)').length,aligned:[...document.querySelectorAll('.belt li')].every(i=>{let r=i.getBoundingClientRect(),c=i.firstElementChild.getBoundingClientRect();return Math.abs((r.top+r.bottom-c.top-c.bottom)/2)<1})})''')})
   if width in [390,1440]:page.screenshot(path=str(out/f'carryon-{width}-{theme}.png'))
 page.set_viewport_size({'width':1440,'height':1100})
 page.goto('http://127.0.0.1:8000/index.html?theme=light#about',wait_until='networkidle')
 page.locator('.belt').hover()
 assert page.locator('.belt-track').evaluate('(e)=>getComputedStyle(e).animationPlayState')=='paused'
 page.emulate_media(reduced_motion='reduce')
 assert page.locator('.belt-track').evaluate('(e)=>getComputedStyle(e).animationName')=='none'
 assert page.locator('.belt-copy:visible').count()==0
 assert page.locator('.belt li:visible').count()==16
 page.locator('.bp').screenshot(path=str(out/'carryon-all-icons.png'))
 page.goto('http://127.0.0.1:8000/index.html?theme=light#work',wait_until='networkidle')
 for case in ['sharepoint','tma']:
  page.locator(f'[data-case="{case}"]').click();page.wait_for_timeout(200);page.keyboard.press('Escape');page.wait_for_timeout(200)
 print(json.dumps({'checks':checks,'pageErrors':errors,'hoverPause':True,'reducedMotion':True,'panels':'opened and dismissed'},indent=2))
 (out/'carryon-checks.json').write_text(json.dumps({'checks':checks,'pageErrors':errors},indent=2))
 b.close()
