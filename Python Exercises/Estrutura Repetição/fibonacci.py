n_termo = int(input("Informe o enésimo termo: "))

def fibo(num):
    if num < 2:
        return num
    else:
        return fibo(num-1) + fibo (num-2)

for i in range(n_termo+1):
    print(fibo(i))
