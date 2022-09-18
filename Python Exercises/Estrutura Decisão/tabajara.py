salario = float(input("Informe o salário do colaborador:"))
reajuste = 0

if salario <= 280:
    reajuste = salario*1.2
elif salario <=700:
    reajuste = salario*1.15
elif salario <=1500:
    reajuste = salario*1.1
else:
    reajuste = salario*1.05

print("O salário anterior era de R$ %.2f" %salario, "e com o reajuste, o salario foi alterado para R$ %.2f" %reajuste)