import requests as req
import sqlite3
import json
req.packages.urllib3.disable_warnings()


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
         
pkmn = []
find = False

while(find==False):
    nome = input('Digite o nome do pokemon: ')
    nome = nome.lower()
    achar_pokemon(nome)
    find = achar_pokemon(nome)


url1 = f'https://pokeapi.co/api/v2/pokemon/{nome}'
res1 = req.get(url=url1, verify=False) 
res1 = json.loads(res1.text)

# res['stats'][i]['stat']['name'] - pegar o nome do status

for i in range (6):
    pkmn.append(res1['stats'][i]['base_stat'])

conn = sqlite3.connect('curso.sqlite3') #Criar arquivo do banco de dados
cursor = conn.cursor() # Iniciando a transição de informação~
cursor.execute(f'''INSERT INTO pokemon (

                hp,ataque,defesa,sp_atk,sp_def, spped

                ) VALUES ({pkmn[0]}, {pkmn[1]}, {pkmn[2]}, {pkmn[3]}, {pkmn[4]}, {pkmn[5]} )''') # Executar comandos SQL
conn.commit() # Salva as informaçãos no Banco de Dados
conn.close()