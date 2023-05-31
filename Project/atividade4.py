#atividade4
def incluir(incluir):
    with open('newuser.txt', 'a') as new_user:
        new_user = new_user.write(incluir)

i = 0

with open('bacon.txt') as user:
    user = user.read()

user = filter(None, str.split(''))
print(user)


incluir('[')

while(True):
    userName = (input('Inclua seu usuário: '))
    if (userName in user):
        print('Usuário já existe!')
    else:
        incluir(userName)
        
        close = input('Deseja incluir outro usuário? (Digite "n" para sair ou qualquer tecla para continuar)')
        if close == 'n': break
        else:
            i += 1
            incluir(',')
    
    if close == 'n':
        break

incluir(']')

'''
with open('bacon.txt', 'w') as bacon_file:
    bacon_file = bacon_file.write('Olá, mundo \n')


with open('bacon.txt', 'a') as bacon_file:
    bacon_file = bacon_file.write('Hi, there! \n')
    
with open('bacon.txt') as bacon_file:
    bacon_file = bacon_file.read()

print(bacon_file)

'''