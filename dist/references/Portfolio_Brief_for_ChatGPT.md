# Portfolio brief: Justin Dao

Paste this file into ChatGPT. Also attach:
1. `Portfolio_Requirements.md` (full rules, in Career\Portfolio)
2. `Brand-Guide\Justin-Dao_Brand-Guide.md` (colours, type, components)
3. The HTML file you want changed (`index.html`, `instacart.html`, `tstar.html` or `places.html`)

If anything here conflicts with Portfolio_Requirements.md, the requirements file wins.

## Your job

Help me edit my portfolio website. Make only the change I ask for. Give me back the full edited file (or the exact old → new snippets) so I can paste it in. Keep answers short. After each change, tell me in one line what changed and update Portfolio_Requirements.md if I set a new rule.

## The site

- Live: https://justindao193.github.io (GitHub repo `justindao193/justindao193.github.io`, GitHub Pages).
- Local copy: `C:\Users\justi\OneDrive\Documents\Career\Portfolio\`. Plain HTML/CSS/JS, one file per page, no build step.
- Pages: home `index.html` (work, about with boarding pass, places), case studies `instacart.html` (Grocery recommendations) and `tstar.html`, `places.html`.
- Vale and TMA are not full pages. They open as slide-out panels on the home page (`<template id="c-sharepoint">`, `<template id="c-tma">`).
- **Status right now:** the local `index.html` has newer Vale/TMA panels than the live site. The live site has a newer home tagline and clearer green tags than the local file. Merge carefully; do not lose either side.
- Do not tell me to push to GitHub unless I ask. Never force-push. Commits are authored as `Justin Dao <justindao193@users.noreply.github.com>`.

## Hard rules

1. **Never invent results.** No fake numbers, quotes, users or tests. Untested ideas are called a plan or "next step".
2. **Visual, not wordy.** Short headings, one or two short sentences, then a visual. Cut anything a recruiter would skim past.
3. **Voice:** plain, first person, no contractions, no buzzwords.
4. **No tiny grey captions or footnotes.** No boxes inside boxes. No tilted photos. No playful extras on the home page.
5. **Confidential work (Vale, TMA):** illustrations only, never internal screens. The Vale assistant is still being built, so no results for it. Leave the TMA 25% figure out of the portfolio.
6. Keep my CRLF line endings and existing code style. Change only what I asked.

## Branding

- Colours: paper #F8F1E9 (background), card #FFFBF6, ink #1E1C1B, muted #6F635A, line #E4D6C7, red #DC4A36 (big accents only), red-deep #B8392A (small red text, buttons). Dark mode: charcoal (#1C1A19 background).
- Fonts: Newsreader weight 370 for titles, section headings and big numbers only. Geist for all reading text. Geist Mono for labels, dates and meta.
- Section label: mono capitals, 0.12em letter spacing, muted, with a hairline to the right edge.
- Text always runs the full body width and ends where the section label line ends.
- Every section is the same distance apart (96px desktop, 64px phone).
- Light content panels: #FDFAF6 with a thin line border; items inside use #F3EDE5.
- Card rows: white cards (#FFFBF6, thin line border) sitting on the page. Labels read "01 browse": red-deep number, lowercase muted word. Never "1 · BROWSE".
- Status tags: green bg #C4E4CB / text #1A5E34 (Done, Selected); amber bg #FFF0C9 / text #8A6200 (Building, Explored); red-soft / red-deep (Stopped).
- Page accents use brand red, not project colours. A project's own colours stay inside its media.
- Every case study has "The solution" right after "The problem": one line on what the product is, then 2 to 3 feature cards with real screens.

## Before you hand back a change

- Check it on desktop and phone width, in light and dark mode.
- Check text still lines up with the section label lines.
- Check you did not invent any fact.
