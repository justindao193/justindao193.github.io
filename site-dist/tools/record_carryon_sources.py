import json
from pathlib import Path
sources=json.loads(Path('tools/verification/icon-download-sources.json').read_text())
sources += [
 ['excel.svg','https://www.microsoft.com/content/dam/microsoft/bade/images/icons/en-us/m365-app-icons-fy26/Excel-Icon-FY26.svg'],
 ['sharepoint.svg','https://www.microsoft.com/content/dam/microsoft/bade/images/icons/en-us/m365-app-icons-fy26/SharePoint-Icon-FY26.svg'],
 ['github.svg','https://brand.github.com/GitHub_Logos.zip — GitHub_Invertocat_Black.svg'],
 ['power-automate.svg','https://download.microsoft.com/download/498606aa-6d27-4f13-aa5c-1401078c153b/Power-Platform-icons-scalable.zip — PowerAutomate_scalable.svg'],
 ['dynamics-365.svg','https://download.microsoft.com/download/498606aa-6d27-4f13-aa5c-1401078c153b/Dynamics-365-icons-scalable.zip — Dynamics365_scalable.svg'],
 ['tableau.ico','https://public.tableau.com/favicon.ico'],
 ['sap.png','https://ui5.sap.com/resources/sap/ui/core/mimes/logo/icotxt_white_220x72_blue.png'],
 ['codex.svg','Official installed OpenAI.Codex_26.1023.6621.0 package, app.asar/webview/assets/codex-d905da579253.svg; unchanged'],
 ['sql.svg','Original neutral database glyph. SQL has no universal official logo; no database vendor implied.']]
Path('references/Carryon-Icon-Sources-2026-10-31.json').write_text(json.dumps({'checked':'2026-10-31','notes':'Original colours retained; no wordmarks cropped or logos redrawn. JavaScript and CSS use established community language marks rather than a claimed corporate logo. Local only; not published.','sources':dict(sources)},indent=2),encoding='utf-8')
