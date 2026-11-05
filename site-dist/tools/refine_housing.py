from pathlib import Path
import re, json

ROOT=Path(__file__).resolve().parents[1]
def write(path,text):
    path.write_bytes(text.replace('\r\n','\n').replace('\n','\r\n').encode('utf-8'))

page=(ROOT/'housing.html').read_text(encoding='utf-8')
page=page.replace('<div class="topnav"><a href="index.html#work">← Work</a><span>Toronto housing</span></div>','<nav class="topnav" aria-label="Main"><a href="index.html#work">← Work / <b>Toronto housing</b></a><a href="index.html#about">About</a></nav>')
page=page.replace('I used Excel and Tableau to explore rental costs, income and housing support across 140 neighbourhoods. What began as a price ranking became a story about what makes housing harder to afford.','I used Excel and Tableau to explore housing pressure across 140 Toronto neighbourhoods. Higher rental costs did not always mean more renters struggling to afford housing.')
page=page.replace('A price ranking only tells half the story.','The same bill can leave very different room to live.')
page=page.replace('I started by asking where housing was most expensive. But a rental bill alone cannot tell me how hard it is to pay. I narrowed the question: how do rental costs, income and housing support relate to renter housing pressure?','I began with a price question: where is housing most expensive? The more useful question was how costs meet people’s resources. A simple budget illustration shows why that matters.')
page=page.replace('A visual story, from price to pressure','Three views, one clearer story')
page=page.replace('I built a visual data story connecting rental costs, income and housing support across Toronto neighbourhoods.','I connected a neighbourhood map, a cost comparison and a closer look at housing support. Each view answers a different part of the question.')
old=re.search(r'<div class="features">.*?</section>',page,re.S).group()
mini=re.search(r'<svg class="mini-points".*?</svg>',old,re.S).group()
features='''<div class="features">
  <a href="#map"><div class="feature-visual"><img src="housing/pressure-map.svg" alt="Toronto’s historical neighbourhood boundaries coloured by renter pressure"></div><div class="feature-copy"><span class="number">01 <i>locate</i></span><h3>Find the pressure</h3><p>See how the share of renters above the threshold varies across the city.</p></div></a>
  <a href="#cost"><div class="feature-visual">'''+mini+'''</div><div class="feature-copy"><span class="number">02 <i>compare</i></span><h3>Look beyond the price</h3><p>Higher rental costs did not always go with greater renter pressure.</p></div></a>
  <a href="#context"><div class="feature-visual"><div class="feature-support"><div><b>64.6%</b><span>Regent Park</span><i style="--w:64.6%"></i></div><div><b>17.9%</b><span>South Parkdale</span><i style="--w:17.9%"></i></div><p>Renters in subsidized housing</p></div></div><div class="feature-copy"><span class="number">03 <i>understand</i></span><h3>Bring support into view</h3><p>Two neighbourhoods show why income and housing support belong in the story.</p></div></a>
</div></section>'''
page=page.replace(old,features)
page=page.replace('Lower income. Less pressure. What else is different?','Housing support changes the picture.')
page=page.replace('<h3>Median monthly household income</h3>','<h3>Median monthly income <span>all households</span></h3>')
page=page.replace('<h3>Average monthly rental housing cost</h3>','<h3>Monthly housing cost <span>renters</span></h3>')
page=page.replace('<h3>Renters in subsidized housing</h3>','<h3>Subsidized housing <span>share of renters</span></h3>')
page=page.replace('<h3>Renters spending 30%+ of income on housing</h3>','<h3>Housing pressure <span>renters spending 30%+ of income</span></h3>')
page=page.replace('The gap in renter pressure between these two neighbourhoods. Housing support and lower costs offer context, but this comparison does not prove a cause.','Regent Park’s share of renters above the threshold was 21.8 percentage points lower. Lower costs and more housing support offer context; the comparison does not prove a cause.')
page=page.replace('2011 data. Income covers all households, including owners, and refers to 2010 before-tax income. Rental costs, support and pressure cover renters. The measures have different populations; dividing these area-level figures would not give an observed renter budget.','2011 data. Income includes owners and renters and refers to 2010 before-tax income. The other measures cover renters. These area-level figures cannot be combined into an observed renter budget.')
page=page.replace('I changed the question before polishing the charts.','The work behind the story')
page=page.replace('The work was about choosing what the data could support, then giving each visual a clear job.','I narrowed the question, kept the populations separate and chose one job for each visual.')
page=page.replace('I changed the question before polishing the charts.','The work behind the story')
page=page.replace('A clearer question makes a stronger data story.','What I would carry into the next analysis')
page=page.replace('The useful finding was not a list of expensive neighbourhoods. It was seeing why the same price-based explanation did not fit every part of the city.','A price ranking was easy to make. A useful explanation needed clearer questions, visible population definitions and comparisons that did not overstate what the data could prove.')

# A shared figure uses the same exact brand tokens as the surrounding pages.
for filename in ['housing.html','index.html']:
    text=page if filename=='housing.html' else (ROOT/filename).read_text(encoding='utf-8')
    text=text.replace('<span>Same city. A different story.</span>','<span class="story-scale"><span class="story-cost">Cost scale $0–$2,000</span><span class="story-pressure">Pressure scale 0–100%</span></span>')
    write(ROOT/filename,text)

# Keep the geographic shapes unchanged; add two stable, labelled reference points.
page=(ROOT/'housing.html').read_text(encoding='utf-8')
script=(ROOT/'housing/script.js').read_text(encoding='utf-8')
project=json.loads(re.search(r'var project=(.*?);\n',script,re.S).group(1))
start=page.index('<div class="map-canvas">')
svg_start=page.index('<svg ',start);svg_end=page.index('</svg>',svg_start)+len('</svg>')
pins=''
for index,name in enumerate(['Newtonbrook West','Kingsway South'],1):
    x,y=project['centres'][name]
    pins+=f'<button class="map-pin pin-{index}" type="button" data-area="{name}" style="left:{x/10:.3f}%;top:{y/6.2:.3f}%"><span>{index}</span><b>{name}</b></button>'
page=page[:svg_start]+'<div class="map-drawing">'+page[svg_start:svg_end]+pins+'</div>'+page[svg_end:]
write(ROOT/'housing.html',page)

story=(ROOT/'housing/story.css').read_text(encoding='utf-8')
replacements={'#252824':'#1E1C1B','#73786F':'#6F635A','#E0E2DA':'#E2D4C4','#E5E9E1':'#EAD5C9','#272B26':'#2F2B29','#EBEEE7':'#F3E6D8','#AAB3A3':'#A39587','#42493D':'#49403B','#20281F':'#302522','#29352555':'#3C2B2250'}
for a,b in replacements.items():story=story.replace(a,b)
story=story.replace('gap:3.8cqw','gap:7.6cqw')
story=story.replace('.story-grid{display:grid;grid-template-columns:1fr 1fr;gap:7.6cqw}', '.story-grid{display:grid;position:relative;grid-template-columns:1fr 1fr;gap:7.6cqw}.story-grid:before{content:"";position:absolute;left:50%;top:0;bottom:0;width:1px;background:var(--story-line)}')
story=story.replace('.story-column+.story-column{border-left:1px solid var(--story-line);padding-left:3.8cqw}', '.story-column{min-width:0}.story-column+.story-column{border:0;padding:0}')
story=story.replace('.story-bottom>div{display:flex;gap:14px}', '.story-bottom>div{display:flex;gap:14px}.story-scale{display:grid}.story-scale>span{grid-area:1/1}')
story=story.replace('.story-screen{width:86%;','.story-screen{width:84%;')
story=story.replace('border-radius:12px;background:var(--story-paper)','border-radius:14px;background:var(--story-paper)')
story=story.replace('box-shadow:0 18px 42px -24px','box-shadow:0 24px 60px -32px')
write(ROOT/'housing/story.css',story)

css=(ROOT/'housing/style.css').read_text(encoding='utf-8')
css=css.replace('--map-line:#FDFAF6;','--map-line:#FDFAF6;--map-0:#EFE5DD;--map-1:#E8C9BB;--map-2:#DAA38F;--map-3:#C6745C;--map-4:#B8392A;')
css=css.replace('--map-line:#302B28;','--map-line:#302B28;--map-0:#45342D;--map-1:#6B4235;--map-2:#95543F;--map-3:#BE7058;--map-4:#F07A66;')
css=css.replace('section{margin-top:clamp(64px,6.7vw,96px)}','section{margin-top:clamp(64px,7vw,96px)}')
css=css.replace('.lead{font-size:18px;line-height:1.75;color:var(--muted);margin-top:32px}', '.lead{font-size:18px;line-height:1.75;color:var(--muted);margin-top:28px}')
css=css.replace('margin:clamp(64px,7vw,88px) 0 0','margin:clamp(64px,7vw,96px) 0 0')
css=css.replace('padding:clamp(24px,3vw,40px)','padding:clamp(24px,4vw,48px)')
css=css.replace('font:12px/1.5 var(--mono);color:var(--red-deep)','font:13px/1.5 var(--mono);color:var(--red-deep)')
css=css.replace('.comparison{display:grid;grid-template-columns:1fr 1fr;gap:32px 40px;padding:32px}', '.comparison{display:grid;grid-template-columns:1fr 1fr;gap:36px 56px;padding:40px}')
css=css.replace('.compare-row h3{font-size:15px;margin:0 0 20px}', '.compare-row h3{font-size:17px;font-weight:500;margin:0 0 24px}.compare-row h3>span{display:block;color:var(--muted);font-size:14px;font-weight:400;margin-top:5px}')
css=css.replace('margin-top:16px;font-size:13px;align-items:center','margin-top:18px;font-size:15px;align-items:center')
css=css.replace('font-weight:500;font-size:15px;grid-column:2','font-weight:500;font-size:17px;grid-column:2')
css=css.replace('font:12px var(--mono);color:var(--muted);margin-bottom:10px','font:12px var(--mono);color:var(--muted);margin-bottom:12px')
css=css.replace('border-radius:6px;font-size:13px','border-radius:6px;font-size:15px')
css=css.replace('gap:12px;font-size:13px','gap:12px;font-size:14px')
css=css.replace('.map-prompt{font-size:12px','.map-prompt{font-size:14px')
css=css.replace('.area-shortcuts button{font-size:11px;padding:6px 9px','.area-shortcuts button{font-size:13px;padding:7px 10px')
css=css.replace('.area-note{margin-top:12px;font-size:14px','.area-note{margin-top:12px;font-size:15px')
css=css.replace('.map-guide{font-size:14px','.map-guide{font-size:14px')
css=css.replace('.map-inspector{padding:28px 24px','.map-inspector{padding:28px 28px')
css=css.replace('.map-layout{display:grid;grid-template-columns:minmax(0,1fr) 250px}', '.map-layout{display:grid;grid-template-columns:minmax(0,1fr) 280px}')
# The overview cards now follow the image-first TStar component.
css=re.sub(r'\.features\{.*?(?=\.map-panel\{)', '''.features{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:56px}
.features>a{display:flex;flex-direction:column;min-width:0;overflow:hidden;border:1px solid var(--line);border-radius:16px;background:var(--card);text-decoration:none;color:var(--ink);transition:transform .25s,border-color .25s}
.features>a:hover{border-color:var(--red-deep);transform:translateY(-3px)}
.feature-visual{height:190px;display:grid;place-items:center;padding:24px;background:var(--tint);overflow:hidden}
.feature-visual img{width:100%;height:100%;object-fit:contain}.feature-visual .mini-points{width:100%;height:100%;border-left:1px solid var(--line);border-bottom:1px solid var(--line)}
.feature-copy{padding:22px 20px 24px}.feature-copy h3{font-size:17px;line-height:1.4;margin:10px 0 8px;font-weight:500}.feature-copy p{font-size:15px;line-height:1.6;color:var(--muted)}
.feature-support{width:100%}.feature-support>div{position:relative;padding-bottom:10px;margin-bottom:16px}.feature-support b{font-size:25px;line-height:1;font-weight:500;color:var(--red-deep)}.feature-support span{display:block;margin-top:6px;font-size:11px;color:var(--muted)}.feature-support i{position:absolute;left:0;bottom:0;width:var(--w);height:4px;border-radius:4px;background:var(--red)}.feature-support>div:nth-child(2) b{color:var(--muted)}.feature-support>div:nth-child(2) i{background:var(--muted)}.feature-support>p{font-size:11px;line-height:1.4;color:var(--muted)}
''',css,count=1,flags=re.S)
# Remove the old card breakpoints; the new cards have a single, consistent stack.
css=css.replace('.features{gap:14px}.features>a{padding:20px}.features h3{font-size:16px}.features p{font-size:14px}','')
css=css.replace('.features{grid-template-columns:1fr}.features>a{display:grid;grid-template-columns:100px 1fr;gap:0 24px;padding:24px}.features .number{grid-column:1/-1}.features img,.mini-points,.mini-bars{grid-row:2/4;margin-top:20px;height:100px}.features h3{margin-top:20px}.features p{font-size:15px}','')
css=css.replace('.features>a{grid-template-columns:90px 1fr;gap:0 20px}','')
extras='''
/* Reference points share the chart’s numbering and the page’s red accent. */
.map-drawing{position:relative}.map-pin{position:absolute;display:flex;align-items:center;gap:7px;transform:translate(-10px,-10px);border:0;padding:0;background:none;color:var(--ink);font:500 13px/1.3 var(--sans);white-space:nowrap;text-shadow:0 1px 2px var(--panel),0 -1px 2px var(--panel)}
.map-pin span{display:grid;place-items:center;flex:0 0 20px;width:20px;height:20px;border-radius:50%;background:var(--ink);color:var(--panel);font:11px var(--mono);text-shadow:none}.map-pin b{font-weight:500}.map-pin.on span{background:var(--red-deep)}.map-pin.on{color:var(--red-deep)}
.map-canvas .tone-0{fill:var(--map-0)}.map-canvas .tone-1{fill:var(--map-1)}.map-canvas .tone-2{fill:var(--map-2)}.map-canvas .tone-3{fill:var(--map-3)}.map-canvas .tone-4{fill:var(--map-4)}
.map-legend>div>span:nth-child(1) i{background:var(--map-0)!important}.map-legend>div>span:nth-child(2) i{background:var(--map-1)!important}.map-legend>div>span:nth-child(3) i{background:var(--map-2)!important}.map-legend>div>span:nth-child(4) i{background:var(--map-3)!important}.map-legend>div>span:nth-child(5) i{background:var(--map-4)!important}
.process>div{display:grid;grid-template-columns:34px 1fr;column-gap:18px;align-content:start}.process .number{font:370 36px/1 var(--serif);color:var(--red)}.process h3{margin:0 0 12px}.process p{grid-column:2}.lessons>div{border-top:2px solid var(--red);padding-top:20px}.lessons h3{font-size:19px}
.bar-label span{font-weight:500}.budget .track{height:14px}.bill strong{color:var(--red-deep)}
.topnav a{color:var(--muted)}.topnav b{font-weight:500;color:var(--ink)}
@media(max-width:1100px){.features{grid-template-columns:1fr}.features>a{display:grid;grid-template-columns:40% 1fr}.feature-visual{height:210px}.feature-copy{padding:28px}.feature-support{max-width:180px}.feature-support span,.feature-support>p{font-size:12px}}
@media(min-width:1301px){.map-guide{font-size:13px}.map-inspector{padding:28px 24px}.map-facts>div{font-size:14px}}
@media(max-width:700px){.comparison{padding:28px}.feature-copy{padding:24px}.feature-visual{height:210px}.map-pin{font-size:12px}.map-pin b{max-width:110px;white-space:normal}.map-pin.pin-1 b{transform:translateY(-8px)}}
@media(max-width:480px){.features>a{display:flex}.feature-visual{height:210px;padding:28px}.feature-copy{padding:22px 24px 26px}.feature-support{max-width:230px}.feature-support span,.feature-support>p{font-size:13px}.feature-support>div{display:grid;grid-template-columns:auto 1fr;gap:12px;align-items:center;padding-bottom:16px;margin-bottom:20px}.feature-support span{margin:0}.map-pin b{display:none}.map-pin span{width:18px;height:18px;flex-basis:18px;font-size:10px}.map-legend>div{flex-wrap:wrap;gap:10px 14px}.map-facts>div{font-size:15px}.area-shortcuts button{font-size:13px}.map-legend>span{font-size:13px}.map-legend>div>span{font-size:12px}}
'''
css=css.replace('@media(prefers-reduced-motion:reduce)',extras+'\n@media(prefers-reduced-motion:reduce)',1)
write(ROOT/'housing/style.css',css)
script=script.replace("marker.setAttribute('cy',c[1]);", "marker.setAttribute('cy',c[1]);marker.style.display=(name==='Newtonbrook West'||name==='Kingsway South')?'none':'';")
write(ROOT/'housing/script.js',script)
req=ROOT/'Portfolio_Requirements.md';text=req.read_text(encoding='utf-8')
text+='\n- Housing refinement (27 October 2026): follow the existing TStar image-first feature cards, full-width alignment and shared Newsreader/Geist/Geist Mono scale. Use the portfolio’s warm cream/charcoal/red palette throughout; avoid the separate green dashboard palette. Make population definitions visible within data graphics.\n'
write(req,text)
print('Refined the housing page, shared home visual, chart styling and map reference points.')
