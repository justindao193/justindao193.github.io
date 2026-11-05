import urllib.request,json
url='https://api.github.com/repos/justindao193/justindao193.github.io/actions/runs?per_page=3'
r=json.load(urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'portfolio-publish-check'})))
print(json.dumps([{'name':x['name'],'sha':x['head_sha'],'status':x['status'],'conclusion':x['conclusion'],'url':x['html_url']} for x in r['workflow_runs']]))
