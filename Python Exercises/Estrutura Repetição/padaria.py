preco_pao = float(input("Informe o preço do pão: "))
i = 1

while(i<=50):
    print(i, "- R$ %.2f" %(preco_pao*i))
    i += 1