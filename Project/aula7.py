import sqlite3

conn = sqlite3.connect('curso.sqlite3') #Criar arquivo do banco de dados
cursor = conn.cursor() # Iniciando a transição de informação~
cursor.execute('DROP TABLE IF EXISTS cep')
cursor.execute('''CREATE TABLE cep (
                cep varchar(40),
                logradouro varchar(40),
                complemento varchar(40),
                bairro varchar(40),
                localidade varchar(40),
                uf varchar(2),
                ddd int
                )''') # Executar comandos SQL
conn.commit() # Salva as informaçãos no Banco de Dados
conn.close()

variavel = cursor.fetchone() # busca uma linha ou;
variavel = cursor.fetchall()