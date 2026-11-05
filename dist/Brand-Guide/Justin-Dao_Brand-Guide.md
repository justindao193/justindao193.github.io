# Justin Dao

Personal brand for Justin Dao: product and data person in Toronto. Clean, warm and quietly confident, with one red accent doing all the talking. Used on the portfolio first, and on resumes, cover letters, slides and LinkedIn graphics after.

## The idea in one line

**Lots of calm, one red dot.** Cream paper, near-black ink, a clean sans for almost everything, a light serif only as an accent, and red used sparingly so it always means "look here". Keep it simple: if a page feels busy, take something away.

## Voice

Write the way Justin talks to a friend over coffee: plain words, short sentences mixed with longer ones, no contractions ("I am", "I have", "do not").

- **Not wordy.** One short heading plus one or two sentences per section. If a line does not help someone understand the work, cut it.

- Say what happened, with real numbers from the resume. Never invent impact.
- Name the decision, not just the work: "I picked weighted recency because I can explain it in one sentence."
- Say where AI helped and what Justin decided.
- Skip fluff: no "passionate", "leverage", "delve", "in today's world", "excited to".

| Instead of | Write |
| --- | --- |
| I am passionate about leveraging data to drive impact. | I like making the boring parts of work easier, with dashboards, automation and AI. |
| Spearheaded a cutting-edge AI initiative. | I am building an agent so people can ask a question and get the right file. |
| Results-driven analyst. | Product and data person in Toronto. |

## Colour

Two themes, same personality. **Cream** is the default; **Charcoal** is dark mode.

- `paper` is the ground for every page. `surface` and `surface-strong` alternate behind project thumbnails so neighbours never match.
- `ink` for headings and body. `muted` for dates, subtitles and labels.
- `red` is the signature: the dot after the name, a thumbnail fill, the live dot by the clock, the arrow in a "→ fix" line. Use it in one or two places per screen, never more.
- At small sizes use `red-deep` (links, small labels, buttons with `on-red` text). `red` fails contrast for small text on paper.
- `charcoal` is for one dark thumbnail per grid, or full dark mode.
- `red-soft` sits behind the lead skill chip on a project card.

Rough mix on any page: 80% paper and surface, 15% ink, 5% red.

## Type

Three Google Fonts, free everywhere:

- **Geist** (sans) is the main voice: body text, intros, labels, notes, captions, lists, numbers and stats, buttons. When in doubt, use Geist.
- **Newsreader** (serif), light weight (300), is an **accent only**: the name on the home page, the page title of a case study, and section headings. Keep it at moderate sizes (about 28 to 46px on case studies). Never use it for body text, notes, quotes, captions or lists, and avoid italic red words inside headings.
- **Geist Mono** for small metadata: years, company tags, the clock.

Scale: name 168px (home only) → case study title 46px → section heading 36px → body 17px → small 14px → meta 12.5px. On phones the name drops to about 64px.

## Layout

- Max width 1120px, 16px side gutter on phones. Desktop first: use the space, never a narrow mobile-looking column of boxes.
- A tiny nav (name, Work, About, plus a live Toronto clock) instead of a big header.
- Home hero: huge name on the left, a short status list on the right. Nothing else.
- Work: one column of big image-led project cards with a title, one line, a year and up to four skill chips.
- **Case studies are their own pages**, modelled on ducngo.xyz/airbnb and rachelchen.tech/projects/1password:
  1. Breadcrumb nav ("← Work / Project").
  2. A wide hero film or image (16:9, radius 16px).
  3. A centred text column (max 720px): serif title, one lead paragraph, then Team / Skills / Duration in three small columns.
  4. Each section: a small grey label, a serif heading, one or two sentences of sans text, then a wide media panel (max 1120px).
  5. End with a short reflection and a "Next project" link.
- Generous space between sections. Hairline `line` dividers between big chapters. **No boxes inside boxes**: a media panel is one flat `surface` block; content sits straight on it.

## Components to reuse

- **Project card**: thumbnail (`surface`, `surface-strong`, `red` or `charcoal`) with a floating mock UI on `card`, then title, subtitle, year in mono, and skill chips. The first chip is the main skill and sits on `red-soft`.
- **Skill chip**: pill, `chip` text style, `line` border. Examples: Machine learning, UX/UI design, Product analytics, AI agents, User research.
- **Badge**: small pill on a thumbnail ("In progress", with a green dot).
- **Link**: ink text with a `line` underline that turns `red-deep` on hover.
- **Primary button**: `red-deep` fill, `on-red` text, pill radius.
- **Media panel**: one flat `surface` block, radius 16px, generous padding, content placed straight on it. A short centred caption underneath in `muted`.
- **Stat row**: big number in Geist 600, one short line under it in `muted`. No serif numbers.

## Imagery

- **Screens:** show app screens as clean cutouts (rounded corners, soft shadow), with **no phone frames or device bezels**.
- **Process artifacts** (personas, journey maps, affinity maps, priority grids): redraw them as clean, on-brand graphics built from the real data, in the tokens and fonts above. Link to the original board for anyone who wants it. Hand-drawn sketches can stay as photos; they are the work.
- **Video:** product films should feel like a launch ad. Let the product do the talking: camera zooms into the feature, smooth easing, one small label per feature (for example "02 Shoot a Star"), a short logo open and close. No big blocks of text on screen.
- No stock photos, mascots, emoji, stickers, or gradients on the portfolio itself (a project's own brand may use its colours inside its media).

## Project brands

A project can carry its own look inside its media, while the page around it stays in Justin's brand.

- **TStar:** night indigo `#1C1F5E`, star yellow `#FFC43D`, Inter in the app. The logo is the plain four-point star in star yellow next to the "TStar" wordmark, vertically centred on the letters. No box or tile behind the star.

## Logo

There is no logo mark yet. The wordmark is the name set in Newsreader 300 followed by a red full stop: **Justin Dao.** Use the full stop in `red`. For small spaces (favicon, profile image) use "JD." on `paper` or `charcoal`.

## Using this on other things

- **Resume and cover letter:** Geist for body, Newsreader for the name only, `red-deep` for one rule or the section labels. Keep everything else ink on white or `paper`.
- **Slides:** `paper` background, Newsreader titles, one red word per slide at most, charts in ink with the key bar in `red`.
- **LinkedIn banner:** `charcoal` or `paper` ground, "Justin Dao." in Newsreader with the red dot, one line in Geist: "Product and data · Toronto".
