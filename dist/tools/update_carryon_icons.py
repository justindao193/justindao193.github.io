from pathlib import Path
import re,json
p=Path('index.html');s=p.read_bytes().decode('utf-8')
# Preserve all existing edits outside the conveyor.
start=s.index('/* Carry-on conveyor belt (31 October 2026) */');end=s.index('</style>',start)
s=s[:start]+'''/* Carry-on: current brand marks, without visible labels (31 October 2026) */
.bp>*,.bp-f>div{min-width:0}
.bp-f .belt{position:relative;max-width:100%;overflow:hidden;margin-top:4px;padding:6px 0;-webkit-mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent)}
.bp-f .belt:after{content:"";position:absolute;left:0;right:0;bottom:0;height:2px;background:repeating-linear-gradient(90deg,var(--line) 0 10px,transparent 10px 18px);animation:beltrail 1.2s linear infinite}
.belt-track{list-style:none;margin:0;padding:0 0 10px;display:flex;gap:10px;width:max-content;animation:belt 42s linear infinite}
.bp-f .belt:hover .belt-track,.bp-f .belt:hover:after{animation-play-state:paused}
.belt-track li{flex:0 0 56px;display:grid;place-items:center;width:56px;height:56px;border:1px solid var(--line);border-radius:14px;background:#FFFBF6}
.belt-track img{display:block;width:34px;height:34px;object-fit:contain}
.belt-track .wide-mark{width:42px}
@keyframes belt{to{transform:translateX(calc(-50% - 5px))}}
@keyframes beltrail{to{background-position:18px 0}}
@media (prefers-reduced-motion:reduce){.belt-track,.bp-f .belt:after{animation:none}.belt-track{flex-wrap:wrap;width:auto}.bp-f .belt{-webkit-mask-image:none;mask-image:none}.belt-track .belt-copy{display:none}}
''' .replace('\n','\r\n')+s[end:]
icons=[('Python','python.svg'),('SQL','sql.svg'),('JavaScript','javascript.svg'),('HTML','html.svg'),('CSS','css.svg'),('Power BI','power-bi.svg'),('Excel','excel.svg'),('Tableau','tableau.ico'),('Figma','figma.svg'),('GitHub','github.svg'),('SAP','sap.png'),('Power Automate','power-automate.svg'),('SharePoint','sharepoint.svg'),('Dynamics 365','dynamics-365.svg'),('Claude','claude.svg'),('Codex','codex.svg')]
Path('about/tools/sql.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="none" stroke="#5B677A" stroke-width="2"><ellipse cx="16" cy="7" rx="10" ry="4"/><path d="M6 7v18c0 2.2 4.5 4 10 4s10-1.8 10-4V7M6 13c0 2.2 4.5 4 10 4s10-1.8 10-4M6 19c0 2.2 4.5 4 10 4s10-1.8 10-4"/></svg>',encoding='utf-8')
items=[]
for duplicate in [False,True]:
 for label,file in icons:
  attrs=' class="belt-copy" aria-hidden="true"' if duplicate else ''
  alt='' if duplicate else label
  wide=' class="wide-mark"' if label=='SAP' else ''
  items.append(f'<li{attrs} title="{label}"><img src="about/tools/{file}" alt="{alt}" width="34" height="34"{wide}></li>')
markup='<div class="belt" aria-label="Tools and languages"><ul class="belt-track">'+''.join(items)+'</ul></div>'
s,n=re.subn(r'<div class="belt" role="img".*?</ul></div>',lambda _:markup,s,count=1);assert n==1
p.write_bytes(s.encode('utf-8'))
r=Path('Portfolio_Requirements.md');raw=r.read_bytes();raw+=('\r\n- Carry-on icons (31 October 2026, supersedes the earlier line-icon rule): use current official product marks and established language logos in their original colours, with no visible name labels. Keep accessible names, a seamless conveyor, hover pause and a still wrapped list for reduced motion. HTML and CSS use separate marks. SQL uses a neutral database glyph because there is no single official SQL logo. Assets are stored locally in about/tools/.\r\n').encode('utf-8');r.write_bytes(raw)
print('Updated Carry-on with',len(icons),'icons and an aria-hidden duplicate set.')
