soma_notas = 0
for i in range(4):
    print("Informe o valor da nota", i+1)
    numero = int(input())
    soma_notas += numero

print("A média é: ", soma_notas/4)