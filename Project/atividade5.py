notas = []
menor_nota = 10
maior_nota = 0
media = 0
print('Obs: notas maiores que 10 serão consideradas 10 e menores que 0 serão 0, assim como qualquer caracter diferente de números.')

for i in range(4):
    nota = input('Digite a nota: ')
    try:
        nota = int(nota)
        if nota > 10: nota = 10
        elif nota < 0: nota = 0
        elif nota < menor_nota: menor_nota = nota
        elif nota > maior_nota: maior_nota = nota
        media += nota
        notas.append(nota)        
    except:
        print('Não é um número. Sera considerado como zero.')
        notas.append(0)


print(f'A média é: {media/4} a nota mais baixa foi {menor_nota} e a mais alta foi {maior_nota}. A lista está abaixo: \n {notas}')