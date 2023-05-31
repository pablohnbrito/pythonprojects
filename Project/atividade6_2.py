import requests as req
req.packages.urllib3.disable_warnings()
import json

def lutar(pkmn1, pkmn2, nome1, nome2):
    HP1 = pkmn1[0]
    HP2 = pkmn2[0]
    atk = 5
    while(True):
        HP2 = HP2 - atk*(pkmn1[1]/pkmn2[2])
        print(f'HP {nome2}: {HP2}')
        if HP2 <= 0: 
            print(f'{nome2} desmaiou.')
            break
        HP1 = HP1 - atk*(pkmn2[1]/pkmn1[2])
        print(f'HP {nome1}: {HP1}')
        if HP1 <= 0: 
            print(f'{nome1} desmaiou.')
            break

def achar_pokemon(nome):
    num = 0
    try:
        url = f'https://pokeapi.co/api/v2/pokemon/{nome}'
        res = req.get(url=url, verify=False)
        res = json.loads(res.text) 
        return True
    except:
        print('O pokemon não existe!')
        return False
         
pkmn1 = []
pkmn2 = []
find1 = False
find2 = False

while(find1==False):
    nome1 = input('Digite o nome do pokemon 1: ')
    achar_pokemon(nome1)
    find1 = achar_pokemon(nome1)

while(find2==False):
    nome2 = input('Digite o nome do pokemon 2: ')
    achar_pokemon(nome1)
    find2 = achar_pokemon(nome2)


url1 = f'https://pokeapi.co/api/v2/pokemon/{nome1}'
url2 = f'https://pokeapi.co/api/v2/pokemon/{nome2}'
res1 = req.get(url=url1, verify=False) 
res2 = req.get(url=url2, verify=False) 
res1 = json.loads(res1.text)
res2 = json.loads(res2.text) 
# res['stats'][i]['stat']['name'] - pegar o nome do status

for i in range (6):
    pkmn1.append(res1['stats'][i]['base_stat'])
    pkmn2.append(res2['stats'][i]['base_stat'])

if pkmn1[5] >= pkmn2[5]: lutar(pkmn1, pkmn2, nome1, nome2)
else: lutar(pkmn2, pkmn1, nome2, nome1)
