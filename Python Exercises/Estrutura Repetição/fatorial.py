fatorial = int(input("Informe o valor do fatorial a ser verificado"))
total = 1
fatorial2 = fatorial

while (fatorial > 0):
    total = total * fatorial
    fatorial -= 1

print("!", end="")

while (fatorial > 1):
    print(f'{fatorial}*', end="")
    fatorial

print("1 =", total)
