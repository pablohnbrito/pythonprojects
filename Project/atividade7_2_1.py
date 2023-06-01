'''
import sqlite3

conn = sqlite3.connect('curso.sqlite3') #Criar arquivo do banco de dados
cursor = conn.cursor() # Iniciando a transição de informação~
cursor.execute('DROP TABLE IF EXISTS pokemon')
cursor.execute(CREATE TABLE pokemon ( - colocar depois os 3 traços ('''  ''') para abrir e fechar
                hp varchar(3),
                ataque varchar(3),
                defesa varchar(3),
                sp_atk varchar(3),
                sp_def varchar(3),
                spped varchar(3)
                )) # Executar comandos SQL
conn.commit() # Salva as informaçãos no Banco de Dados
conn.close()
'''

'''
cursor.execute('SELECT * FROM cep')
variavel = cursor.fetchone() # busca uma linha ou;
variavel = cursor.fetchall() # busca 
'''
