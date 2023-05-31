#operadores matemáticos
print(3%2) #divisão do resto
print(3**2) #potencia
print(3/2) #divisão
print(2+3) #soma
print(3-2) #subtração
print(3//2) #divisão inteira

# A extensão ".ipynb" é a do júpyter e dá pra codar linha a linha. Para debugar aqui, basta usar a função "debug".

string = 'Hello'
string += ' world!'
string += ' Bem Vindo.'
print(string)

number = 1
number += 2
print(number)

my_list = ['item']
my_list *= 3
print(my_list)

def foo():
    '''
    Esta é uma função. 
    obs: com  3 aspas, faz comentários como uma caixa de texto
    '''
    print('Este número é:', 1)

print(foo())

phrase = ['numero', 'boca', '09']
for word in phrase:
    print(word, end = '-')