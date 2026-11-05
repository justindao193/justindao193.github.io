import json
from pathlib import Path
from playwright.sync_api import sync_playwright
out=Path('tools/verification');out.mkdir(exist_ok=True)
results=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe',headless=True)
 page=b.new_page()
 errors=[]
 page.on('pageerror',lambda e:errors.append(str(e)))
 for name in ['index.html','housing.html','tstar.html','instacart.html']:
  for theme in ['light','dark']:
   for width in [390,800,1150,1440,1920]:
    page.set_viewport_size({'width':width,'height':1000})
    page.goto(f'http://127.0.0.1:8000/{name}?theme={theme}',wait_until='load')
    checks=page.evaluate('''() => ({overflow:document.documentElement.scrollWidth>innerWidth,theme:document.documentElement.dataset.theme,badImages:[...document.images].filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.src),textAlignment:[...document.querySelectorAll('main > section')].flatMap(s=>{let l=s.querySelector('.eb');if(!l)return [];let r=l.getBoundingClientRect().right;return [...s.children].filter(e=>['P','H2','H3'].includes(e.tagName)&&e!==l).filter(e=>Math.abs(e.getBoundingClientRect().right-r)>2).map(e=>({tag:e.tagName,text:e.textContent.slice(0,30)}))})})''')
    results.append({'page':name,'width':width,'theme':theme,**checks})
    if name=='housing.html' and width in [390,1440] and theme=='light':page.screenshot(path=str(out/f'publish-housing-{width}.png'),full_page=True)
  print(name,'checked',flush=True)
 page.emulate_media(reduced_motion='reduce')
 page.goto('http://127.0.0.1:8000/housing.html?theme=light',wait_until='load')
 assert page.locator('video').evaluate('(v)=>v.paused'),'reduced motion film playing'
 page.emulate_media(reduced_motion='no-preference'); page.locator('.motion-control').click()
 page.emulate_media(reduced_motion='no-preference'); page.locator('.motion-control').click()
 page.locator('#area').select_option(label='Regent Park')
 assert '26.8%' in page.locator('#area-result').inner_text()
 page.goto('http://127.0.0.1:8000/index.html?theme=light',wait_until='load')
 for case in ['sharepoint','tma']:
  locator=page.locator(f'[data-case="{case}"]')
  if locator.count():
   locator.click()
   page.wait_for_timeout(400)
   page.keyboard.press('Escape')
   page.wait_for_timeout(400)
 print('errors',errors)
 print('failures',json.dumps([r for r in results if r['overflow'] or r['badImages'] or r['textAlignment']]))
 (out/'publish-checks.json').write_text(json.dumps({'results':results,'errors':errors},indent=2))
 b.close()


