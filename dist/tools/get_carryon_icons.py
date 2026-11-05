from pathlib import Path
import urllib.request,concurrent.futures,zipfile,io,json
folder=Path('about/tools');folder.mkdir(exist_ok=True)
urls={
'python.svg':'https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/files/python-logo-only.svg',
'excel.svg':'https://www.microsoft.com/content/dam/microsoft/bade/images/icons/en-us/m365-app-icons-fy26/Excel-Icon-FY26.svg',
'sharepoint.svg':'https://www.microsoft.com/content/dam/microsoft/bade/images/icons/en-us/m365-app-icons-fy26/SharePoint-Icon-FY26.svg',
'power-bi.svg':'https://raw.githubusercontent.com/microsoft/PowerBI-Icons/main/SVG/Power-BI.svg',
'figma.svg':'https://static.figma.com/app/icon/2/favicon.svg',
'claude.svg':'https://claude.com/icon.svg',
'html.svg':'https://www.w3.org/html/logo/downloads/HTML5_Badge.svg',
'javascript.svg':'https://raw.githubusercontent.com/voodootikigod/logo.js/master/js.svg',
'css.svg':'https://raw.githubusercontent.com/CSS-Next/logo.css/main/css.svg',
'sap.svg':'https://www.sap.com/dam/application/shared/logos/sap-logo-svg.svg.adapt.svg/1493030643828.svg',
 'tableau.svg':'https://www.tableau.com/themes/custom/tableau_www/logo.v2.svg'
}
def get(item):
 name,url=item
 try:
  data=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=20).read()
  assert b'<svg' in data
  (folder/name).write_bytes(data);print(name,len(data),flush=True);return name,url
 except Exception as e:print(name,e,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:results=list(pool.map(get,urls.items()))
z=zipfile.ZipFile('tools/verification/powerplatform.zip');(folder/'power-automate.svg').write_bytes(z.read('Power Platform/PowerAutomate_scalable.svg'))
z=zipfile.ZipFile('tools/verification/github.zip');(folder/'github.svg').write_bytes(z.read('GitHub Logos/SVG/GitHub_Invertocat_Black.svg'))
u='https://download.microsoft.com/download/498606aa-6d27-4f13-aa5c-1401078c153b/Dynamics-365-icons-scalable.zip'
z=zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(u).read()));print('dynamics files',z.namelist(),flush=True)
Path('tools/verification/icon-download-sources.json').write_text(json.dumps([r for r in results if r],indent=2))
