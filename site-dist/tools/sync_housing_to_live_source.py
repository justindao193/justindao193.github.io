from pathlib import Path
import re, shutil, subprocess

raise SystemExit('Retired: the duplicate Career portfolio was removed. Edit the canonical checkout directly.')

ROOT=Path(__file__).resolve().parents[1]
MIRROR=Path(r'C:\Users\justi\OneDrive\Documents\Career\Portfolio')
AUDIT=ROOT/'references/live-site-audit'
BACKUP=AUDIT/'career-copy-before-live-sync-2026-10-27'

def write(path,text):
    path.write_bytes(text.replace('\r\n','\n').replace('\n','\r\n').encode('utf-8'))

# The remote deployment and the four live HTML hashes were verified before
# this migration. Add only the housing card to the deployed home-page source.
base=(ROOT/'index.html').read_text(encoding='utf-8')
legacy=(MIRROR/'index.html').read_text(encoding='utf-8')
card=re.search(r'      <a class="proj" href="housing.html">.*?      </a>',legacy,re.S).group()
if 'href="housing.html"' not in base:
    start=base.index('<a class="proj" href="tstar.html">')
    end=base.index('      </a>',start)+len('      </a>')
    base=base[:end]+'\n\n'+card+'\n'+base[end:]
    base=base.replace('</head>','<link rel="stylesheet" href="housing/story.css">\n</head>',1)
    observer="<script>(function(){var io=new IntersectionObserver(function(es){es.forEach(function(e){e.target.classList.toggle('running',e.isIntersecting)})});document.querySelectorAll('.housing-thumb').forEach(function(e){io.observe(e)})})();</script>"
    base=base.replace('</body>',observer+'\n</body>',1)
    write(ROOT/'index.html',base)

shutil.copyfile(MIRROR/'housing.html',ROOT/'housing.html')
(ROOT/'housing').mkdir(exist_ok=True)
for name in ['data-2011.csv','original-presentation.pdf','pressure-map.svg','script.js','story.css','style.css']:
    shutil.copyfile(MIRROR/'housing'/name,ROOT/'housing'/name)

BACKUP.mkdir(parents=True,exist_ok=True)
public=[p for p in subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).decode().split('\0') if p]
changed=[]
for name in public:
    src=ROOT/name;dst=MIRROR/name
    if dst.exists() and src.read_bytes()!=dst.read_bytes():
        saved=BACKUP/name
        if not saved.exists():saved.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(dst,saved)
        changed.append(name)
    dst.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(src,dst)
shutil.copyfile(ROOT/'housing.html',MIRROR/'housing.html')
for name in ['data-2011.csv','original-presentation.pdf','pressure-map.svg','script.js','story.css','style.css']:
    shutil.copyfile(ROOT/'housing'/name,MIRROR/'housing'/name)

for path in [ROOT/'Portfolio_Requirements.md',MIRROR/'Portfolio_Requirements.md']:
    text=path.read_text(encoding='utf-8')
    text=text.replace('- Update the local portfolio at `C:\\Users\\justi\\OneDrive\\Documents\\Career\\Portfolio` first. Do not publish without a new request.','- Canonical source: `C:\\Users\\justi\\OneDrive\\Documents\\ChatGPT\\Portfolio`, the Git checkout behind the live site. Keep `C:\\Users\\justi\\OneDrive\\Documents\\Career\\Portfolio` as a synchronized local preview copy. Do not publish without a new request.')
    rule='- Source audit (27 October 2026): live GitHub Pages deployment was `cecd9190119a21888c5c72e9357ec52d1451a8d2` on `main`. The four public HTML pages matched the Git checkout after line-ending normalization; the Career copy was older. Rebase additions on the live source, preserving its tagline, strong green tags and project details.\n'
    if rule.strip() not in text:text+='\n'+rule
    write(path,text)
print('Canonical checkout updated; Career preview synchronized.')
print('Older public pages backed up:',changed)
print('Backup:',BACKUP)
print('Public source files mirrored:',len(public))
