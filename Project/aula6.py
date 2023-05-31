'''
#essa tá ok (tem que instalar o pip install requests)
import requests as req
# req.packages.urllib3.disable_warnings()
import json
url = 'https://viacep.com.br/ws/52121370/json/'
res = req.get(url=url, verify=False) 
res = json.loads(res.text) 
print(res)
'''
import requests as req
req.packages.urllib3.disable_warnings()
import json
url = 'https://pokeapi.co/api/v2/pokemon/dragonite'
res = req.get(url=url, verify=False) 
res = json.loads(res.text) 
print(res['stats'][0]['stat']['name'], ' - ', res['stats'][0]['base_stat'])
#print(res) - funci