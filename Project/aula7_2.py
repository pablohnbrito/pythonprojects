import sqlite3

cep = 52121370
conn = sqlite3.connect('curso.sqlite3') #Criar arquivo do banco de dados
cursor = conn.cursor() # Iniciando a transição de informação~
cursor.execute(f'''INSERT INTO cep (

                cep,logradouro,complemento,bairro,localidade,uf,ddd

                ) VALUES ("52121370", "Avenida Retiro dos Ananás", " - ", "São Mateus", "Morada de Ribeirão", "ES", 27)''') # Executar comandos SQL
conn.commit() # Salva as informaçãos no Banco de Dados
conn.close()