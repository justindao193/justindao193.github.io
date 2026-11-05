# Justin Dao — Portfolio Requirements

Use this sheet every time a project is added or changed on the portfolio. The TStar page is the reference example: match it.

- Live website: https://justindao193.github.io (GitHub repo justindao193/justindao193.github.io; this is the newest version)
- Portfolio artifact (older Claude copy): https://claude.ai/artifact/3zZufYwFgGxpnMTvvmzbPU
- Brand guide (colours, type, components): https://claude.ai/artifact/F7zKAUeqKwwV8pPs25zNJ9
- Saved copy on Justin's computer: `C:\Users\justi\OneDrive\Documents\Career\Portfolio\`
- Style references Justin likes: https://ducngo.xyz/ , https://ducngo.xyz/airbnb , https://www.rachelchen.tech/ , https://www.rachelchen.tech/projects/1password , https://www.rachelchen.tech/projects/etch

- Site icon: the take-off J logo (see "Logo", 1 November 2026, at the end of this sheet). Every page uses it as the browser-tab icon, not inside the page.

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

- **Intro:** see "Recruiter feedback update — 2 November 2026" (new positioning line).
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
- Panel layout (Oct 26, 2026): mono meta line, serif title, muted lead, skill chips (Geist, line border); a visual in a white stage (Vale: Before → Knowledge hub [Done] → AI assistant [Building]; TMA: 9 vs 6 step dots); big serif numbers in white cards; "What I did" as 01/02/03 rows with red-deep numbers and no line above the first row. Vale "Also during my co-op" shows three short resume facts: 10+ CRM workflow issues triaged with IT; up to 60% less manual work for 4 teams through automation; 3 Power BI dashboards used by leadership and 20+ people. No tags on the Vale or TMA thumbnails. The TMA panel still leaves out the 25% figure.
- Updated local source: index.html. The publishing folder and live site have not been changed for this revision.

## Workspace update - 26 October 2026
- This ChatGPT/Portfolio folder is the working checkout. The original Career/Portfolio folder remains unchanged.
- Preserve the live home tagline and strong green tags when merging newer local panels.
- Newer rules override older brand-guide conflicts: Newsreader 370, full-width text, first-visit light mode and consistent section spacing.
- Publish only on request; the current request authorizes this live update.

## Panel copy update - 26 October 2026
- Remove the closing confidentiality/illustration note from Vale and the closing recreated-visuals/team-effort note from TMA. Do not restore these footer notes. Keep the underlying confidentiality and honest attribution rules.

## Toronto housing — 27 October 2026

- Canonical source: `C:\Users\justi\OneDrive\Documents\ChatGPT\Portfolio`, the Git checkout behind the live site. The older `C:\Users\justi\OneDrive\Documents\Career\Portfolio` duplicate was retired at Justin’s request; do not recreate it. Do not publish without a new request.
- Place Toronto housing directly after TStar. Use the established cream/red brand and a visual narrative with maps, charts and short takeaways.
- Keep 2011 renter measures separate from the 2016 assessed owner-and-renter overview. Income in the 2011 comparison covers all households, not renters alone. Do not claim causal findings or current-market conditions.

- Housing visual polish: match TStar/Instacart typography, spacing and media treatment. Use an accurate north-up map with geographic context; do not use the flattened map as a repeated decorative hero.

- Source audit (27 October 2026): live GitHub Pages deployment was `cecd9190119a21888c5c72e9357ec52d1451a8d2` on `main`. The four public HTML pages matched the Git checkout after line-ending normalization; the Career copy was older. Rebase additions on the live source, preserving its tagline, strong green tags and project details.

- Single working portfolio (27 October 2026): keep only the Git checkout in `Documents\ChatGPT\Portfolio`. Unique files from the retired Career copy are preserved under `references/retired-career-portfolio-unique-files`; that archive is local source material, not a second working site.

## Career folder access — 27 October 2026

- Justin wants the portfolio accessible in Career. `C:\Users\justi\OneDrive\Documents\Career\Portfolio` is a Windows junction to the single Git checkout in `Documents\ChatGPT\Portfolio`; both paths open the same files. Keep one working copy.
- Career organization: current documents stay in Applications, Resumes-and-Transcripts, Cover-Letters and Tracker. Historical portfolio exports, screenshots, reports, backups and the former publishing folder live under `Career\Archives\Portfolio`. Use `Career\START-HERE.txt` for the folder guide.

- Housing refinement (27 October 2026): follow the existing TStar image-first feature cards, full-width alignment and shared Newsreader/Geist/Geist Mono scale. Use the portfolio’s warm cream/charcoal/red palette throughout; avoid the separate green dashboard palette. Make population definitions visible within data graphics.

- Housing intro metadata (27 October 2026): use the existing case-study labels Role / Skills / Duration, with short factual values. Remove Context / My work / Tools and the separate historical-data note under the metadata. Keep year and population limits beside the relevant evidence. Only show Duration when Justin provides the actual project dates.

- Housing metadata confirmed by Justin (27 October 2026): Role is Data analyst; Duration is Oct 2026. Skills should describe the actual analysis work and tools.

- Housing analytical review (30 October 2026): show the pattern across all 140 neighbourhoods, not just hand-picked examples. The scatterplot splits cost and pressure at the renter-weighted Toronto averages (about $1,026 and 43.5%), which reproduce the cost/burden groups in the cleaned data (58 lower on both, 29 higher on both, 27 higher cost/lower pressure, 26 lower cost/higher pressure; 53 break the expected pattern). Do not use a dashed line at 30% on the pressure axis.
- Housing map headline reflects that pressure was widespread: 138 of 140 neighbourhoods had at least 30% of renters above the threshold (median 42.8%, highest Newtonbrook West 60.3%, lowest Regent Park 26.8%).
- Housing has a "What I measured" definitions row in The problem and a Limits section ("Can show" / "Cannot show") holding the 2016 note. Note small renter bases (Kingsway South: 535 renter households). Rank facts may be stated from the data; correlation coefficients are not shown unless Justin approves adding that method.

- Housing cohesion (30 October 2026): no "View the original presentation" button. Solution cards follow TStar: white card with line border, white top picture area (card colour with a hairline under it; Justin did not like the beige tint), "01 locate" label, 17px/600 title, short muted line; three across until 760px, then stacked. Process and lessons use the TStar "What I learned" style (red top rule, large serif number, 17px/600 title). "What I would do next" uses the TStar white roadmap cards (01 income, 02 data, 03 maps, 04 trend).

- Housing strengthening (30 October 2026, approved by Justin): Housing support includes an "Across all 140 neighbourhoods" check grouping areas by subsidized-renter share (5% or less: 22 areas, $1,156, 44.9%; 5–15%: 57, $1,055, 42.2%; 15–30%: 46, $900, 42.8%; over 30%: 15, $777, 38.7%; correlation −0.40), framed as an association. A "So what" section recommends pairing rent with income and support data, reviewing the 53 areas that break the pattern, and using renter-only income.

- Housing trim (30 October 2026): no grey captions under housing charts. Put year, population and unit notes inside the visual (headings, axis labels, key, rank lines). Limits is a two-column checklist of a bold label plus a short note.

- Case-study meta row (30 October 2026, all case studies): Role / Skills / Duration columns use a 16px gap so they line up exactly with the three-card rows below.
- Housing solution-card pictures (30 October 2026): the map card uses a cropped copy (housing/pressure-map-card.svg) so Toronto fills the frame; the dot card fills its frame; the support card uses large serif numbers. Pictures must stay inside the frame at every width.

- Housing final polish (30 October 2026): the lead states the finding (53 neighbourhoods broke the pattern; more subsidized renters went with less pressure). Card 03 reads "A two-neighbourhood contrast, then a check across all 140." Sources sit in the downloads row; no separate grey footer.

- Housing film (30 October 2026): the housing header and the home-page housing card play housing/media/housing-film.mp4 (15 s, 1920x1080 rendered from lossless frames at CRF 17, silent, loops; poster housing-film.jpg). Updated the same day at Justin's request: modern, clean look that does not need to match the site brand (charcoal #0D0E11, white Geist bold, coral #FF5A3C accent, no serif). Opens with the Toronto neighbourhood outline drawing in and the wordmark "Toronto" with "Where is renting hardest to afford?" (the data is neighbourhood-level, so it answers where, not who; no official City logo); then map fill with "138 of 140"; dot chart with "53 broke the pattern"; Regent Park vs South Parkdale bars; end line "Rent alone is the wrong yardstick." with "wrong yardstick." in coral and the sign-off "Toronto housing · 2011 data". Do not put Justin's name in the film. Keep text inside the centre 864px so phone crops do not cut it. Pauses for reduced motion; the header keeps its Pause/Play button.

- Carry-on conveyor (31 October 2026): on the boarding pass, Carry-on spans the full width and is a slowly sliding belt of tool tiles (rounded tile, small icon, name): Python, SQL, JavaScript, HTML/CSS, Power BI, Excel, Tableau, Figma, GitHub, SAP, Power Automate, SharePoint, Dynamics 365, Claude, Codex. Icons are simple original line icons, not official brand logos. Pauses on hover; with reduced motion it shows as a still, wrapped list. This replaces the earlier three-line Carry-on text.

- Carry-on icons (31 October 2026, supersedes the earlier line-icon rule): use current official product marks and established language logos in their original colours, with no visible name labels. Keep accessible names, a seamless conveyor, hover pause and a still wrapped list for reduced motion. HTML and CSS use separate marks. SQL uses a neutral database glyph because there is no single official SQL logo. Assets are stored locally in about/tools/.

- Boarding pass update (31 October 2026): Home base and Next stop are removed; fields are Carry-on and Off duty. Carry-on is a split-flap board (airport departures style) of Justin's own icon files in about/tools/. Eight tiles flip in a wave every 2.8 seconds between two sets, ordered by importance for PM, design and analyst roles: SQL, Python, Excel, Power BI, Tableau, Figma, GitHub, JavaScript, then HTML, CSS, Claude, Codex, Power Automate, SharePoint, Dynamics 365, SAP. Four per row on phones; reduced motion shows all sixteen still. This replaces the conveyor belt.

- Off duty (31 October 2026): removed at Justin's request. The boarding pass shows Carry-on only. The unused files in about/hobbies/ and about/theo-tile.jpg stay in the folder.
- Logo (1 November 2026): Justin picked option 05, the take-off J: a white J whose top turns into an upward arrow, on a brand-red (#DC4A36) rounded tile. Geist-style geometry, no serif. It is the favicon on every page (inline SVG in the icon link), icon-180.png (square, for phones) and icon.svg (master file).

## SkillSwap — 1 November 2026
- Case study `skillswap.html` (CSC318 group project, Jan to Apr 2026, team of six: "Me + 5 designers") follows the TStar format. Facts come only from the A1 to A3 reports: 42 surveys, 7 interviews (5 students, 1 small business owner, 1 campus sustainability lead), 5 heuristic reviews and 4 think-alouds on paper, 12 hi-fi testers, SUS 71.7, about 4.5 minutes average (2 to 8).
- Course feedback is applied as Justin's own iteration, never described as feedback from a class or TA: findings grouped by who we heard from, real quotes, requirements and journey backed by numbers.
- The redesign (skillswap/app) is an untested plan: test results stay in "Next step" until a real test happens. Ratings, reviews, notifications and chat messages in the prototype are sample content, never results.
- The original Figma screens (file YUwAwgfbNEGoPWNnlw3Nrg) live in skillswap/media/figma-*.jpg. The hi-fi section shows them, and every decision card is a before/after: "Tested in Figma" next to "My redesign".
- App look (set 1 November 2026): mostly black and white on a warm cream background (#FAF7F2), dark green-black #17302A for main buttons, terracotta #C4532F used sparingly (Offer a swap, swap icons, logo, unread dots), plus soft pastels (peach, sky, butter, rose, lavender, sage) for tags, cards and stat tiles. Serif (Fraunces) only for titles. No verified ticks, no "Reply needed" tags.
- Patterns follow familiar marketplaces (eBay, Kijiji, Amazon, Facebook Marketplace): name then price ("$10 or swap"), plain back arrows with no circle, one header style, bottom bar with Message, Buy and Offer a swap, a Facebook-style location sheet with a 1 to 100 km slider, hobby tags plus an "All categories" sheet, filters (All / Swap / Buy, category, condition, "Wants what I have"), a chat with the swap pinned on top and a message box, and a notifications page.
- Wording Justin chose: "Make an offer", "Review offer", "Offer sent", "Renegotiate", "Decline" (pale red), "SkillSwapped!" with "You and Maya swapped. Enjoy the new hobby." Meet-up offers suggested public spots plus "Somewhere else", and quick days plus a date and time picker.
- Real free photos from Unsplash in skillswap/media/photos (yarn-hd.jpg is the sharp welcome photo).
- Home card and case-study hero use skillswap/card.html (offer sent, accepted, items trade places, SkillSwapped) in the new colours on a peach tint. Final design clips are the live app in demo mode (?demo=browse, request, accept, post).
- Kept short for recruiters (about 15,000 px at 1440 wide): no journey map, no product-thinking section, four decision cards, four clips in a two-column grid, four extra screens. Persona is Sam, drawn by Justin (skillswap/media/sam.jpg), who is also the app user.
- Justin's own tasks on the original team are not yet stated on the page; ask him before adding them.

## Recruiter feedback update — 2 November 2026
- Based on advice from a UX hiring manager: lead with outcomes, not a step-by-step story; tell one clear story; show AI skills and user-centred work.
- **Positioning (final, 2 November 2026):** Justin keeps his original line unchanged: "An analyst who designs, and a designer who checks *the numbers.*" Do not add an e-commerce ending; he wants it general so it works for any application. "I design shopping and marketplace products…" and "…the numbers behind what people buy." were both rejected.
- **Goal / Result / My part:** every case study has a three-column brief right under the lead, before the meta row. Each column has a small mono label, a short serif headline and one muted sentence. The Result uses only real, measured results. If nothing has been measured, write the goal as a target and put the measurement in "Next step". Done for all four case studies. Since 2 November 2026 the brief is visual cards, not text: Goal shows the old way crossed out above the new way; Result shows a big red number with a small chart (bars, score bar, dot grid); My part shows numbered steps or "Team of N" / "On my own" pills; one short bold line closes each card. Cards sit three across above 1200px and stack below.
- **AI story:** where Justin built with AI and asks to show it, add a "How I built it" section with three columns: what AI did, what Justin decided, and what he pushed back on. Use only real examples. SkillSwap has one (sidebar link "built with ai"), placed between the decisions and "Try it". This follows Non-negotiable 8: never imply he built it alone, and never hide his own decisions.
- Resume: the SkillSwap entry lists Claude and has a third bullet about building the redesign as a working web prototype with Claude. Skills reads "AI Prototyping (Claude, Codex)".
- **Say each fact once (2 November 2026):** the brief carries the headline result. Later sections give the evidence and should not repeat the same sentence or number. The lead under the title is one line saying what the project is, not a summary of the process. Cut duplicate "limits" lists, number rows already shown in a chart, and "bar to beat" charts in Next step (the target sits in the goals row instead).
- Home page (2 November 2026): Justin wants it left as it is. Do not add result lines to the cards or change the "Next" status line unless he asks.
- Resume projects: at most two one-line bullets per project. SkillSwap bullet 2: "Redesigned the app solo around tester issues, then built it as a working web prototype with Claude in HTML/JS."

## Homepage intro refresh — 4 November 2026
- Supersedes the earlier keep-original-tagline rule: headline is "I design with precision, build with AI, and use data to guide decisions." Newsreader 370, about 40px on phones to 72px on desktop; precision in brand red.
- Small Justin Dao identity above; Currently and Previously columns below, stacked on phones. Preserve the Vale, Apple and TMA experience copy and the June 2027/open-to-work line beneath Currently. No intro row dividers. Keep sidebar, themes and existing project layout/content.

- Homepage refinement (4 November 2026): remove the small Justin Dao identity above the headline and the U of T graduation/open-to-work line from the intro. Rotate precision, care and intent every three seconds with a Carry-on-style flip, brand red and stable width; pause offscreen/hidden and keep precision for reduced motion. Navigation identity stays.

- Homepage refinement: align desktop headline and sidebar work link around 28vh from the top. Use Carry-on split top/bottom paper flaps for the rotating adjective. Word width follows its actual text; do not reserve precision-width blank space for care or intent.

- Homepage final wording behavior (4 November 2026): precision stays static in brand red. Remove adjective rotation and flap animation. Preserve the lowered intro/sidebar alignment and natural headline wrapping; do not force three phrase lines. Supersedes the rotating-adjective instructions above.

- Latest homepage behavior: restore precision/care/intent paper-flap rotation, left-aligned. First phrase occupies its own line so build with AI stays stationary. Keep comma attached to the displayed adjective; reduced motion stays precision. Supersedes static-only rule.

- Latest correction: headline stays inline with natural wrapping. Only the left-aligned adjective flips in a fixed precision-width slot. Comma remains outside the animated slot next to build with AI; do not force a break before build.

- Instacart opening (4 November 2026): product headline, benefit and about 24% offline recall, prototype link and full interface first; oversized personalized-versus-popularity comparison next, with held-out evaluation context and simpler-rule decision. Goal/Result/My part cards replaced for this page. Development overview and animation follow. No claims of measured revenue or time savings.

- Instacart opening correction: retain the existing animated hero/video at the very top, above the product headline; product-first copy and evidence follow.

- Instacart opening refinement: place quantitative results before the embedded prototype. Remove model-choice explanation from the opening; keep technical reasoning in the later story. Early task times must retain two-person repeated-task/assistance limitations; never claim causal time savings or convert recall into accuracy.

- Instacart user testing update: Justin confirmed two additional participants, Search first then recommendations on the same items: Person 3 15s/4s, Person 4 14s/3s. Four total. Assistance for new participants unknown; do not invent. Show glanceable paired time bars and preserve repeated-task/order caveat.

- Instacart opening hierarchy refinement: video, title and one-line product benefit, Role/Skills/Duration immediately below, action links, one prominent recommendation comparison, then interactive prototype. Detailed four-person task chart belongs in User testing rather than crowding the intro. Preserve branding.

- Instacart opening also includes a compact four-participant task-time summary: search first 14-22 seconds, recommendations second 3-5 seconds, same items. Retain practice/assistance limitations and a link to the full testing section. Do not present ranges as causal savings.

- Instacart recruiter flow: video, brief introduction and ownership, Results at a glance (user testing first, recommendation performance second), interactive prototype and action links, then process. Show participant timing ranges once at the top; later testing section explains method/limits/next test without repeating the numbers or chart.

- Instacart intro polish: remove independent-project label at user request; concise product benefit and visual results. Remove redundant Try the prototype CTA; retain View code and full-screen fallback, and show Try me / Switch shoppers. Add a product. inside the embedded prototype stage. Keep short method limitations linked to deeper evidence.
