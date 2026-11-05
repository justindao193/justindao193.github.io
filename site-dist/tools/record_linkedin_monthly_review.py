from pathlib import Path
import json
folder=Path(r'C:\Users\justi\OneDrive\Documents\Career\LinkedIn')
review='''# LinkedIn monthly review — 1 November 2026

Read-only review of the live profile at https://www.linkedin.com/in/justin-dao1903/ against the approved resume brief, local LinkedIn baseline and the published portfolio.

- Headline unchanged; preserve it.
- About now uses the newer single-paragraph draft Justin requested in chat. Treat this as a user-applied change, not an error to revert. No unsupported results or SharePoint assistant claims in About.
- Vale, Apple and TMA descriptions match the verified baseline. The Vale assistant remains described as being built.
- Apple and TMA skill associations remain present; profile reports 26 skills.
- BISA and MTA Experience copies and three Organization records remain. Cleanup was already raised and awaits confirmation; do not repeat the question without new evidence.
- No confirmed new role, role end date or graduation event.

## Newly actionable suggestion

The Toronto housing case study was published on 30 October, after the 28 October LinkedIn baseline. No Featured or Projects section was displayed on the fully loaded profile. Suggest featuring this verified public work to support data/BI applications.

Title: Toronto housing — what rental prices leave out
Description: An Excel and Tableau analysis of renter housing pressure across 140 Toronto neighbourhoods using 2011 data, presented through maps, charts and a visual case study.
Link: https://justindao193.github.io/housing.html

No profile edits, posts or messages were published. This suggestion has now been raised; do not repeat it on later reviews unless something material changes.
'''
(folder/'Profile-Review-2026-11-01.md').write_bytes(review.replace('\n','\r\n').encode('utf-8'))
p=Path('references/LinkedIn_Review.md')
with p.open('ab') as f:f.write(('\r\n## Monthly review — 1 November 2026\r\n\r\nLive headline and experience unchanged. About now uses Justin\u2019s newer one-paragraph draft from chat; preserve it rather than restoring the old five-paragraph draft. Apple/TMA skills remain present (26 total skills shown). Existing extracurricular cleanup remains pending; no repeat question. New recommendation raised: feature the Toronto housing case study published 30 October, using the exact title/description in Career/LinkedIn/Profile-Review-2026-11-01.md. Do not repeat this recommendation without a material change. Review only; no LinkedIn edits made.\r\n').encode('utf-8'))
print('Saved read-only monthly review and recommendation baseline.')
