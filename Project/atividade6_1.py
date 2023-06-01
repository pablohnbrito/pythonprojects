import requests as req
req.packages.urllib3.disable_warnings()
import json
cep = input('Digite o seu cep: ')

try:
    url = f'https://viacep.com.br/ws/{cep}/json/'
    res = req.get(url=url, verify=False) 
    res = json.loads(res.text) 
    print(res)
except:
    print('CEP não é válido')    