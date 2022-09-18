nota1 = float(input("Informa a nota 1 do aluno:"))
nota2 = float(input("Informa a nota 2 do aluno:"))
media = (nota2+nota1)/2

if (media==10):
    print("Aprovado com distinção")
elif (media>=7):
    print("Aprovado")
else:
    print("Reprovado")