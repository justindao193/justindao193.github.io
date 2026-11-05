import urllib.request,json
u='https://api.github.com/repos/microsoft/PowerBI-Icons/git/trees/main?recursive=1'
try:
 d=json.load(urllib.request.urlopen(u));print([x['path'] for x in d.get('tree',[]) if 'svg' in x['path'] and 'Power-BI' in x['path']][:20])
except Exception as e:print(e)
