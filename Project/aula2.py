
#printar na tela
print('Qual o seu nome? ')
my_name = input()
print('Oi, {nome}'.format(nome = my_name))
print('Oi, ', my_name)



name = 'carlos'
if name != 'carlos':
    print('Você não é Carlos')
else:
    print('Você é Carlos')

numero = 0
if numero > 1:
    print('Número maior que ', numero)
elif numero == 1:
    print('Número igual que ', numero)
else:
    print('Número menor que ', numero)

