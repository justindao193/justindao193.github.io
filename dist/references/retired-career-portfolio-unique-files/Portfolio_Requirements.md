# Justin Dao — Portfolio Requirements

Use this sheet every time a project is added or changed on the portfolio. The TStar page is the reference example: match it.

- Live website: https://justindao193.github.io (GitHub repo justindao193/justindao193.github.io; this is the newest version)
- Portfolio artifact (older Claude copy): https://claude.ai/artifact/3zZufYwFgGxpnMTvvmzbPU
- Brand guide (colours, type, components): https://claude.ai/artifact/F7zKAUeqKwwV8pPs25zNJ9
- Saved copy on Justin's computer: `C:\Users\justi\OneDrive\Documents\Career\Portfolio\`
- Style references Justin likes: https://ducngo.xyz/ , https://ducngo.xyz/airbnb , https://www.rachelchen.tech/ , https://www.rachelchen.tech/projects/1password , https://www.rachelchen.tech/projects/etch

- Site icon: the red badge (a question mark that ends as a J, cream on red #DC4A36). Files: `Career\Portfolio\Brand-Guide\Icon\`. Every page uses it as the browser-tab icon, not inside the page.

- Light and dark mode: a sun/moon button in the nav (and the case-study sidebar). Light mode shows the Toronto clock, dark mode shows the Saigon clock. With no saved choice, the site is light from 7 am to 7 pm Toronto time and dark otherwise. The choice carries across all pages.

- No playful extras on the home page (a bouncing dot, cycling "why" text, a cat mascot and scribble underlines were tried on Oct 23, 2026 and removed). Keep only the light-switch animation (sun and moon roll in and out) and the clock city swap (light mode shows whichever of Toronto or Saigon is in daytime (7am to 7pm), dark mode shows whichever is at night, Toronto first).

- Fonts: the Newsreader serif is used for headings everywhere, including case studies (project pages); he brought it back to the case studies on Oct 23, 2026. Body text is Geist and labels are Geist Mono. Serif weight 370.
- Case study intro (title, lead, Role/Skills/Duration) uses the full body width so it lines up with the section labels: the title and lead run the full width of the page (no narrow cap, they end where the label lines end), and the meta row sits under a hairline in three equal columns.
- Right after "The problem", every case study has a "The solution" section that says in one line what the product is, then shows its 2 to 3 main features as cards with a real screen (Oct 24, 2026).
- Card rows (solution features, roadmap, launch plan) use white cards (`card` #FFFBF6 with a thin `line` border) sitting on the page, not inside a panel. Each card label is "01" in red-deep Geist Mono, then a lowercase word in muted mono ("01 browse"). Never "1 · BROWSE" in capitals (Oct 24, 2026).
- All case study section text (headings and paragraphs under each label) also runs the full body width, ending where the label lines end. No narrow 720px text column (Oct 24, 2026). **Every page, every section, no exceptions:** each paragraph, heading and sub-heading must end exactly where the section label line ends. Check with a script that the right edge of every text column matches the label line on desktop and phone before publishing (TStar was missed once; fixed Oct 24, 2026).
- Light mode is the default on every page for first-time visitors; the toggle and ?theme= still persist a choice.

## Non-negotiables

1. **Never invent results.** No fake test results, quotes, metrics or users. If something has not been tested, call it a plan ("Next step"), not a finding.
2. **Visual, not wordy.** If a section can be a picture, chart or screen, it should be. Short sentences. Cut anything a reviewer would skim past.
3. **Serif only as an accent.** Use it for page titles, section headings and big numbers. Body text, quotes, captions, tags and card text are all in the sans font (Geist on the site, Inter in app mockups).
4. **Light panels.** In light mode, content panels (charts, timelines, tables) are a near-white warm panel (#FDFAF6) with a thin `line` border, and anything inside them uses a slightly darker tint (#F3EDE5). Do not use the older darker beige panel (#EFE6DB); text, especially red, was hard to read on it (Oct 24, 2026). Dark mode is unchanged.
5. **Brand red for page accents.** Charts, bars, numbered lessons and rules on the page use the brand red, never a project colour. A project colour (like TStar night blue) stays inside its own media: films, mockups and the prototype stage (Oct 24, 2026).
   - **Green tags must read as green.** Positive tags (Selected, Tested, Excited, Open to chat) use background `#C4E4CB` with text `#1A5E34`; dark mode `#24503A` with `#B4ECC8`. Never the old pale mint (`#DDF1E4`, `#DFEEE1`, `#E3F6EC`), which looked grey (Oct 24, 2026).
6. **No boxes inside boxes.** No sticky-note cards and no card-in-a-card. Separate content with thin lines and white space.
7. **No tiny grey captions or footnotes.** If it is worth saying, say it at normal size. If not, delete it.
8. **No AI credit line** unless Justin asks for one. When a project was AI-assisted and Justin asks to show it (as with Buy it again), use a plain "My role" section: what I did, and where AI helped. Never imply he built everything alone.
9. **Writing voice:** plain, no contractions, first person, no buzzwords. Team credit is "Me + N designers" (no names). Duration shows the real project dates only.

## Home page

- **Home page layout:** like Rachel Chen's. On desktop: "Justin Dao" top-left, a fixed left sidebar (work, about, contact, linkedin, plus the clock) centred vertically like the project pages, with a red dot on the current section. On tablets and phones it falls back to the top menu.

- **Intro:** "An analyst who designs, and a designer who checks *the numbers.*" (red italic on "the numbers.", changed Oct 24, 2026) with no sub-intro line under it.
- **Project list:** one column, newest or strongest first. The job search assistant project is removed and stays off.
- **Each project card** (motion-design style, like https://www.rachelchen.tech/):
  - The thumbnail is 16:9 on a soft tinted background in that project's colour (sage, lilac, sky, night blue and so on).
  - Inside is **one large, isolated UI component**, centred with even padding on every side, not a small full-page screenshot. It is built in HTML from the real product's look (real names, photos, colours and copy).
  - It **shows the core idea in motion**: the thing that makes the project special. For an algorithm, animate how it works (for Buy it again: past orders → scores → re-rank → top five list). For an app, animate the key interaction (for TStar: Shoot a Star → star bursts → chat opens).
  - The motion is smooth and staged: the card rises in, elements stagger in, a cursor clicks real controls, the UI reacts, then everything fades out and loops. It plays only while on screen and stays still for reduced-motion users.
  - Text never touches the card edges. Names show in full, nothing is cut off, and columns and headings line up.
  - Under the thumbnail: the title, a one-line description that says what the thing is in plain words (for example "A grocery recommendation algorithm that suggests what you will buy again"), context and year on the right, then skill chips.
- **Case-study hero:** use the same live motion as the home card, told in short numbered chapters (01, 02, 03 chips), instead of a separate screen-recording video.
- Mockups may use placeholder brand names when there is no real one, but swap in the real name if it exists. Never show real company data.

## Project (case study) page format

**Layout** (Rachel Chen / Duc Ngo):
- A fixed **left sidebar** at the far left: a ← back arrow, then **8–9 grouped** lowercase links, like Duc Ngo (for example overview, research, ideas, design process, final solution, product thinking, try it, learning). Group related sections under one link instead of listing every section. The link stays highlighted while you scroll through any section in its group.
- The main body is **centred**, matching the home page. The text column is about 720px; wide visual panels are about 1040px.
- On small screens the sidebar becomes a top nav.
- Every project page opens at the top (turn off scroll restoration and scroll to the top on load, unless the link has a #section).

**Section order** (adapt to the project):
1. **Hero:** a promotional film or the strongest visual, then the title (a one-sentence outcome headline), a lead paragraph (2–3 lines, including what *I* did), and a meta row: Team / Skills / Duration.
2. The problem, with one visual stat block.
3. Research: themes as a clean 2×2 with big numbers and one line each.
4. Persona: a profile layout (avatar, facts list, a big quote, Goals / Pains / Needs in three columns, trait sliders).
5. Journey: Today vs With [product], as card rows.
6. Ideas: an impact vs effort chart with dots (it becomes a ranked list on small screens).
7. Prototypes (lo-fi → mid-fi → hi-fi): what was tested → what changed.
8. Final design: short looping feature clips (one per key feature).
9. What changed (before/after screens) and my decisions (why I chose X over Y).
10. Product thinking (funnel, safety, competitors) where relevant.
11. **Try it:** a live clickable prototype centred on a wide dark stage, with an "Open full screen" link. Not a beige box.
12. Next step (a test plan, until real results exist).
13. Reflection: a short intro, 3–4 lessons in two columns with real examples, then "What I would do next".

**Data / ML project variant** (Buy it again is the reference): hero film → overview numbers → problem split into "what data can test" and "what only people can test" → scope (in / left out) → fair-test design → methods ladder → final results → the trade-off decision → prototype clips and states → user sessions with their limits → follow-up experiment → how I worked → my role → what I learned → try it → next step. Show every trade-off honestly (for example "trees scored higher, I still chose the simpler rule").

**Real company data or brand:** add a visible independent-project note near the title ("Not affiliated with or endorsed by …"). A desktop prototype goes on a soft tinted stage, scaled to fit, with a screenshot and an "Open the prototype" button on phones.

**Visuals:**
- **Screens have no phone frames.** Show clean screen cut-outs with rounded corners and a soft shadow.
- **Redraw research artifacts on-brand** (affinity maps, personas, journeys, matrices) instead of pasting old screenshots.
- **Film and clips:**
  - The film should feel like a launch ad: smooth eased zooms into the feature being shown, minimal text (small numbered chips only), and a plain star logo with no box.
  - Feature clips are trimmed so they never start or end mid-transition, so there are no ghost phones or glitches when they loop.

**Responsive (required before publishing):**
- Check every section at 390, 800, 1150, 1440 and 1920px wide. There must be no sideways scrolling and nothing cut off or squished.
- Grids wrap; persona and similar blocks stack by the space they actually have (container queries), not only the window width.

## App / prototype mockup polish

- Icons and text line up: star + label chips centred on one line, and side-bar icons aligned with their rows.
- Use drawn graphics, not stock photos, for small thumbnails. Art fills its box edge to edge with no stray shapes.
- Sticky bottom buttons sit flush with the bottom, with nothing peeking underneath.
- Sheet titles have breathing room above the content.
- Keep labels simple: for example "+7" instead of "+7 ★", and no extra helper lines like "Say hi when it feels right."

## Process for adding a project

1. Collect the material: the reports, files, old site and real numbers. Ask Justin for anything missing. Do not fill gaps with guesses.
2. Build the project page in this format, then its home page card (animated, realistic product screen).
3. Check the responsive widths, alignment and the film or clip loops.
4. Publish to the portfolio artifact and save a copy to the Career\Portfolio folder.
5. Answer artifact comments in their thread, fix the issue, then resolve.

## Open items (as of Oct 23, 2026)

- TStar hi-fi test with 5 students (script: `Career\Portfolio\TStar_Hi-fi_Test_Script.md`). Real results replace the "Next step" section.
- Buy it again case study is live on the portfolio (instacart.html). Public hosting and a review of the Instacart logo and photo use remain open.
- The next full case study could be the SharePoint assistant or travel booking redesign.
- SharePoint assistant: confirm what Vale allows to be shown.
- Travel photo section: waiting on photos from Justin.


## Spacing (case studies)
- Every section is the same distance apart: 96px on desktop, 64px on phones (clamp 64–96px), measured from the end of one section to the next section label. No extra divider lines between sections (Oct 24, 2026).
- Generous, never cramped. Label to heading: 20px. Heading to body text: 24px. Body line-height 1.75. Paragraph to paragraph: 18px. Text to panel: 56px.
- Hero title line-height 1.2, 64 to 88px below the film; lead text 32px below the title.
- List rows in panels: 14px apart with a hairline between; two-column splits 72px apart.

## Section labels
- Every section label on the site uses one style: small Geist Mono capitals, wide letter spacing (.12em), muted colour, followed by a thin line running to the right edge (e.g. "SELECTED WORK", "EXPERIENCE", "LIFE LATELY", and every case study eyebrow like "THE PROBLEM"). Home uses `.ab-label`, case studies use `.eb`.
- No separate divider line above a section when its label already has the line.
- The label line always stretches the full width of the main body (same width as the wide panels), even when the text column under it is narrower.

## Home views
- The home page shows one view at a time: work (hero + project cards), about, places. The side rail stays the same and switches views; the URL hash (#work, #about, #places) opens a view directly. No long continuous scroll.
- "Let's build something useful." headline shows on the work view only. The contact row below it sits at the bottom of every view (pinned to the bottom of the screen on short pages): email with Copy, and a LinkedIn button. LinkedIn is not in the rail. Resume lives in the side rail ("resume ↗") and the mobile menu only (Justin-Dao-Resume.pdf, from Resumes-and-Transcripts/2026-09-01_Justin-Dao_Resume.pdf).
- Footer reads "© 2026 Justin Dao" (no "built with Claude"). Contact email: justindao193@gmail.com.
- Switching views plays a split-flap "Next stop" board that flips to the page name, then fades into the page. The rail stays visible during it.
- Mobile top nav: name on its own line, then Work, About, Places.

## About page
- Top of About is a boarding pass card: photo on the left, then "Boarding pass" / "JD · 2004", passenger "DAO / JUSTIN", route YYZ Toronto to NEXT "Ready for a new challenge", a short intro ("I like figuring out how things work and how I can make them better. I love learning new skills, so I am always up to something."), and four fields only: Home base / Next stop / Carry-on / Off duty. Carry-on is grouped by role (PM, analyst, designer), three lines: kept short, only the most important: "Analysis: Power BI, SQL, Python" / "Design: Figma, user testing" / "Product and AI: Claude, AI assistants". No mention of side projects. Do not add separate Working on or Side projects fields (he rejected them). Right stub: gate JD in mono and a fixed-height barcode with no number. Stacks under 1180px. An editorial version was tried and reverted; the user prefers the boarding pass.
- Then an "Experience" timeline, then "Life lately": a tight justified photo collage (3 rows, small gaps, no tilts, no borders, no wasted space) with a small label chip on each photo (red tag + short caption).
- Justin does NOT want: tilted/slanted photos, the icon "Off the clock" cards, or big gaps between photos.
- Photos live in about/ (from his Oct 23, 2026 Drive email): friends-night, climbing, theo, vale-team, food, seoul, nyc, toronto, plus me-mine. He removed IMG_2439 and IMG_2458. The GoPro video GX015906 (17 MB) was too large to pull from Drive.

## Places section (on the home page, id "places")
- Lives on the home page between About and Contact, linked as "places" in the side rail. No separate page.
- Interactive world map, Pacific-centred, red pins for visited places, bigger ringed pins for places lived (Saigon, Seoul, Vancouver, Saint John NB, Toronto).
- Map data loads as a module from jsDelivr (world-atlas countries-50m `+esm`), because the artifact page blocks plain data fetches.
- Place data lives in the `P` list in the places script. Each place can take `when`, `note` and `photos` (file paths). Empty fields stay hidden. Never invent trip details.
- Card shows status, city, country, local time and distance from Toronto.

## GitHub
- Grocery recommendations code is public at https://github.com/justindao193/instacart-grocery-recommendations (53 files after the reviewed update; analysis code is a historical snapshot, not a reproducible pipeline; commits authored by Justin with no Claude co-author trailers). The case page has a "View code on GitHub" button and links to the weighted recency code and SQL, discovery code, held-back check and prototype (Oct 24, 2026).


## Workplace project summaries — 26 October 2026

- Work locally first. Do not upload these changes until Justin asks.
- Vale and TMA use concise project summaries in the existing slide-out panels: role, problem, contribution and outcome.
- Keep confidential client/company material private. Use clearly labelled illustrative or recreated visuals, with no internal screens, records or implementation details.
- Vale: show the completed knowledge hub separately from the assistant still in development. Do not claim measured assistant accuracy or time savings.
- TMA: highlight research, the 9-to-6-step flow and collaboration. Omit the 25% task-completion figure from this summary because its measurement details are not recorded here.
- Panel layout (Oct 26, 2026): mono meta line, serif title, muted lead, skill chips (Geist, line border); a visual in a white stage (Vale: Before → Knowledge hub [Done] → AI assistant [Building]; TMA: 9 vs 6 step dots); big serif numbers in white cards; "What I did" as 01/02/03 rows with red-deep numbers and no line above the first row. Vale "Also during my co-op" shows three short resume facts: 10+ CRM workflow issues triaged with IT; up to 60% less manual work for 4 teams through automation; 3 Power BI dashboards used by leadership and 20+ people. No tags on the Vale or TMA thumbnails. TMA note: "The visuals are a recreated example, not the client's product. The fixes were a team effort." The TMA panel still leaves out the 25% figure.
- Updated local source: index.html. The publishing folder and live site have not been changed for this revision.

## Toronto housing — 27 October 2026

- Canonical source: `C:\Users\justi\OneDrive\Documents\ChatGPT\Portfolio`, the Git checkout behind the live site. Keep `C:\Users\justi\OneDrive\Documents\Career\Portfolio` as a synchronized local preview copy. Do not publish without a new request.
- Place Toronto housing directly after TStar. Use the established cream/red brand and a visual narrative with maps, charts and short takeaways.
- Keep 2011 renter measures separate from the 2016 assessed owner-and-renter overview. Income in the 2011 comparison covers all households, not renters alone. Do not claim causal findings or current-market conditions.

- Housing visual polish: match TStar/Instacart typography, spacing and media treatment. Use an accurate north-up map with geographic context; do not use the flattened map as a repeated decorative hero.

- Source audit (27 October 2026): live GitHub Pages deployment was `cecd9190119a21888c5c72e9357ec52d1451a8d2` on `main`. The four public HTML pages matched the Git checkout after line-ending normalization; the Career copy was older. Rebase additions on the live source, preserving its tagline, strong green tags and project details.
