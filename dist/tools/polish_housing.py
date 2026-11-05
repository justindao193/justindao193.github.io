from pathlib import Path
import csv, html, json, math, re

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT
SOURCE = ROOT/'references/toronto-housing/Toronto Housing - PC Handoff/03 - Source Data'
OUT = TARGET/'housing'

def write(path, value):
    path.write_bytes(value.replace('\r\n','\n').replace('\n','\r\n').encode('utf-8'))

# A north-up Mercator projection keeps local proportions; the former drawing
# scaled longitude and latitude as if the two represented equal distances.
geo = json.loads((SOURCE/'Income_Rent_2011.geojson').read_text(encoding='utf-8'))
def project(point):
    lon, lat = point[:2]
    return math.radians(lon), math.log(math.tan(math.pi/4+math.radians(lat)/2))

rings = [ring for f in geo['features'] for polygon in f['geometry']['coordinates'] for ring in polygon]
points = [project(point) for ring in rings for point in ring]
x0,y0 = min(p[0] for p in points),min(p[1] for p in points)
x1,y1 = max(p[0] for p in points),max(p[1] for p in points)
scale = min(900/(x1-x0),520/(y1-y0))
dx,dy = (1000-(x1-x0)*scale)/2,40+(520-(y1-y0)*scale)/2
def xy(point):
    x,y=project(point)
    return (x-x0)*scale+dx,(y1-y)*scale+dy

def simplify(points, tolerance=.42):
    if len(points)<3:return points
    a,b=points[0],points[-1]
    vx,vy=b[0]-a[0],b[1]-a[1]
    denominator=vx*vx+vy*vy
    def distance(p):
        if not denominator:return math.hypot(p[0]-a[0],p[1]-a[1])
        t=max(0,min(1,((p[0]-a[0])*vx+(p[1]-a[1])*vy)/denominator))
        return math.hypot(p[0]-a[0]-t*vx,p[1]-a[1]-t*vy)
    distances=[distance(p) for p in points[1:-1]]
    index=max(range(len(distances)),key=distances.__getitem__)+1
    if distances[index-1]>tolerance:
        return simplify(points[:index+1],tolerance)[:-1]+simplify(points[index:],tolerance)
    return [a,b]

palette=['#EDE3DD','#E8C4B8','#DCA18F','#C77561','#AA4636']
paths=[]
data=[]
centres={}
for f in geo['features']:
    prop=f['properties']; name=prop['Neighbourhood Name']; value=round(prop['Renters Spending 30 Percent or More']*100,1)
    d=''
    for polygon in f['geometry']['coordinates']:
        for ring in polygon:
            pts=simplify([xy(p) for p in ring])
            d+='M'+'L'.join(f'{x:.1f},{y:.1f}' for x,y in pts)+'Z'
    level=min(4,max(0,int((value-20)//10)))
    paths.append(f'<path data-name="{html.escape(name,quote=True)}" data-pressure="{value}" class="area tone-{level}" d="{d}" fill="{palette[level]}"><title>{html.escape(name)}: {value:.1f}% of renters above the 30% threshold · 2011</title></path>')
    # Area centroid of the largest exterior ring, for a small selection marker.
    largest=max(f['geometry']['coordinates'],key=lambda p:len(p[0]))[0]
    pts=[xy(p) for p in largest]; cross=[a[0]*b[1]-b[0]*a[1] for a,b in zip(pts,pts[1:])]
    total=sum(cross)
    centres[name]=[sum((a[0]+b[0])*c for a,b,c in zip(pts,pts[1:],cross))/(3*total),sum((a[1]+b[1])*c for a,b,c in zip(pts,pts[1:],cross))/(3*total)]
    data.append(dict(name=name,pressure=value,rent=prop['Average Monthly Rental Cost'],support=round(prop['Subsidized Tenant Share']*100,1)))

map_svg='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 620" role="img" aria-label="North-up map of Toronto’s 140 historical neighbourhoods, showing renter housing pressure in 2011"><g stroke="var(--map-line, #FDFAF6)" stroke-width="1.15" stroke-linejoin="round">'''+''.join(paths)+'''</g><g class="map-context" fill="var(--muted, #6F635A)" font-family="Geist, sans-serif"><text x="800" y="540" text-anchor="middle" font-size="19" letter-spacing="3">LAKE ONTARIO</text><path d="M943 85V45m-7 12 7-12 7 12" fill="none" stroke="currentColor" stroke-width="1.5"/><text x="943" y="30" text-anchor="middle" font-size="16">N</text></g><circle class="map-marker" cx="0" cy="0" r="6" fill="var(--ink, #1E1C1B)" stroke="var(--panel, #FDFAF6)" stroke-width="3"/></svg>'''
initial=centres['Newtonbrook West']
map_svg=map_svg.replace('cx="0" cy="0"',f'cx="{initial[0]:.1f}" cy="{initial[1]:.1f}"')
write(OUT/'pressure-map.svg',map_svg)

screen='''<div class="story-screen" aria-hidden="true">
  <div class="story-top"><span><i></i>Toronto housing</span><span>2011 · renter data</span></div>
  <div class="story-head"><span class="story-cost">Higher rent.</span><span class="story-pressure">Greater pressure?</span></div>
  <div class="story-grid">
    <div class="story-column"><span class="story-place"><i>01</i>Newtonbrook West</span><div class="story-values"><strong class="story-cost">$1,135</strong><strong class="story-pressure">60.3<span>%</span></strong></div><div class="story-unit"><span class="story-cost">monthly rental housing cost</span><span class="story-pressure">spending 30%+ of income on housing</span></div><div class="story-track"><i class="story-cost" style="--fill:56.75%"></i><i class="story-pressure" style="--fill:60.3%"></i></div></div>
    <div class="story-column"><span class="story-place"><i>02</i>Kingsway South</span><div class="story-values"><strong class="story-cost">$1,640</strong><strong class="story-pressure">36.1<span>%</span></strong></div><div class="story-unit"><span class="story-cost">monthly rental housing cost</span><span class="story-pressure">spending 30%+ of income on housing</span></div><div class="story-track"><i class="story-cost" style="--fill:82%"></i><i class="story-pressure" style="--fill:36.1%"></i></div></div>
  </div>
  <div class="story-bottom"><div><span class="chapter-cost">01 rental cost</span><span class="chapter-pressure">02 renter pressure</span></div><span>Same city. A different story.</span></div>
</div>'''

page=(TARGET/'housing.html').read_text(encoding='utf-8')
page=re.sub(r'<style>.*?</style>','<link rel="stylesheet" href="housing/style.css">\n<link rel="stylesheet" href="housing/story.css">',page,count=1,flags=re.S)
page=re.sub(r'<header id="overview">.*?<h1>','<header id="overview"><div class="housing-media" role="group" aria-label="Two-neighbourhood comparison: Newtonbrook West costs $1,135 with 60.3% of renters spending at least 30% of income on housing; Kingsway South costs $1,640 with 36.1% above the same threshold.">'+screen+'<button class="motion-control" type="button" aria-label="Pause the comparison animation">Pause</button></div><h1>',page,count=1,flags=re.S)
page=page.replace('Expensive rent.<br>A bigger story.','Looking beyond rent to understand housing pressure in Toronto')
page=page.replace('I explored 140 Toronto neighbourhoods to understand what rental prices leave out. The story moved from the cost of housing to the share of renters struggling to afford it.','I used Excel and Tableau to explore rental costs, income and housing support across 140 neighbourhoods. What began as a price ranking became a story about what makes housing harder to afford.')
# Keep the opening scope note brief; the year/population limits remain by the charts.
page=page.replace('A historical study using 2011 neighbourhood data, with a separate 2016 overview. It does not describe today’s rental market.','Historical data · 2011 renter analysis, with a separate 2016 overview')
page=page.replace('<p class="eb">The solution</p>','<p class="eb">The solution</p>')
page=page.replace('One question. Three views of the evidence.','A visual story, from price to pressure')
page=page.replace('The pressure does not fall evenly.','140 neighbourhoods. Uneven pressure.')
page=page.replace('Darker red means more renters cross that threshold.','Choose a neighbourhood to see how many renters cross that threshold.')
# Use the same accurate map in the small overview card.
page=re.sub(r'<div class="mini-points".*?</div>','',page,flags=re.S)
start=page.index('<div class="panel map-panel">')
end=page.index('<p class="caption">The map locates pressure.',start)
options=''.join(f'<option{ " selected" if d["name"]=="Newtonbrook West" else ""}>{html.escape(d["name"])}</option>' for d in sorted(data,key=lambda d:d['name']))
new_map='''<div class="panel map-panel"><div class="map-heading"><div><span class="number">2011 / Toronto</span><h3>Where renters feel the pressure</h3></div><span class="map-guide">Select an area or use the list ↓</span></div><div class="map-layout"><div class="map-canvas">'''+map_svg+'''<div class="map-legend"><span>Renters spending 30%+ of income on housing</span><div>'''+''.join(f'<span><i style="background:{c}"></i>{label}</span>' for c,label in zip(palette,['<30%','30–39%','40–49%','50–59%','60%+']))+'''</div></div></div><div class="map-inspector"><label for="area">Neighbourhood</label><select id="area">'''+options+'''</select><div id="area-result" aria-live="polite"></div><div class="area-bar"><i id="area-bar-fill"></i><span class="threshold-mark"></span></div><p class="area-note">of renters spend at least 30% of income on housing</p><div class="map-facts"><div><span>Monthly rental cost</span><b id="area-rent"></b></div><div><span>Subsidized tenants</span><b id="area-support"></b></div></div><p class="map-prompt">Compare the story’s neighbourhoods</p><div class="area-shortcuts">'''+''.join(f'<button type="button" data-area="{name}">{name}</button>' for name in ['Newtonbrook West','Kingsway South','Regent Park','South Parkdale'])+'''</div></div></div></div>'''
page=page[:start]+new_map+page[end:]
page=page.replace('<div class="plot-key"><span><i></i>All neighbourhoods</span><span><i></i>Newtonbrook West / Kingsway South</span></div>','<div class="plot-key"><span><i></i>All 140 neighbourhoods</span><span><b>1</b> Newtonbrook West</span><span><b>2</b> Kingsway South</span></div>')
page=page.replace('<p class="number">Newtonbrook West</p>','<p class="number"><span class="point-number">1</span> Newtonbrook West</p>').replace('<p class="number">Kingsway South</p>','<p class="number"><span class="point-number">2</span> Kingsway South</p>')
# Replace the old inline interaction script with the coordinated map/chart code.
page=re.sub(r'<script>\s*\(function\(\)\{\s*var data=.*?</script>','<script src="housing/script.js"></script>',page,count=1,flags=re.S)
write(TARGET/'housing.html',page)

home=(TARGET/'index.html').read_text(encoding='utf-8')
home=re.sub(r'<div class="thumb housing-thumb[^\"]*"[^>]*>.*?</div>\s*<div class="proj-meta">','<div class="thumb housing-thumb housing-media" aria-hidden="true">'+screen+'</div>\n        <div class="proj-meta">',home,count=1,flags=re.S)
# Remove the earlier thumbnail-only styles instead of layering overrides.
home=re.sub(r'/\* Toronto housing:.*?(?=</style>)','',home,count=1,flags=re.S)
home=home.replace('</head>','<link rel="stylesheet" href="housing/story.css">\n</head>',1) if 'href="housing/story.css"' not in home else home
home=home.replace("e.target.classList.toggle('in-view',e.isIntersecting)","e.target.classList.toggle('running',e.isIntersecting)")
# Preserve the phone metadata fix, unrelated home styling is untouched.
phone_meta='@media(max-width:650px){.proj-meta{display:flex;flex-direction:column;align-items:flex-start;gap:8px}.proj-meta>div{min-width:0}.proj-meta .yr{white-space:normal;text-align:left}}\n'
home=home.replace(phone_meta,'')
home=home.replace('</style>',phone_meta+'</style>',1)
write(TARGET/'index.html',home)
# Embed chart data so the case study also works through file://.
script=(ROOT/'tools/housing-script.js').read_text(encoding='utf-8').replace('/* PROJECT_DATA */',json.dumps(dict(areas=data,centres=centres),ensure_ascii=False,separators=(',',':')))
write(OUT/'script.js',script)
for src,name in [('housing-style.css','style.css'),('housing-story.css','story.css')]:
    write(OUT/name,(ROOT/'tools'/src).read_text(encoding='utf-8'))

for path in [ROOT/'Portfolio_Requirements.md']:
    text=path.read_text(encoding='utf-8')
    rule='- Housing visual polish: match TStar/Instacart typography, spacing and media treatment. Use an accurate north-up map with geographic context; do not use the flattened map as a repeated decorative hero.\n'
    if rule.strip() not in text:write(path,text+'\n'+rule)
print('Polished local housing page, home card, map and shared visual assets.')
print('Map aspect ratio:',round((x1-x0)/(y1-y0),3),'areas:',len(data),'SVG bytes:',len(map_svg.encode()))
