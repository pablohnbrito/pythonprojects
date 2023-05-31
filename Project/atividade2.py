#atividade2

i = 0
user = []
password = []

while(True):
    userName = (input('Inclua seu usuário: '))
    if (userName in user):
        print('Usuário já existe!')
    else:
        user.append(userName)
        password.append(input('Digite a sua senha:'))
        i += 1
    
    close = input('Deseja incluir outro usuário? (Digite "n" para sair ou qualquer tecla para continuar)')
    if close == 'n':
        print(user)
        break