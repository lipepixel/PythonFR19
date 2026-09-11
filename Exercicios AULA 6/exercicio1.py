totalprimos=0
primos=0
N = int(input("Digite qtd de números: "))
for i in range(N):
    primos=0
    x = int(input("Digite um número: "))
    if x > 1:
        primos = 1
    for j in range(2, x):
        if x % j == 0:
            primos = 0
            break
    totalprimos += primos
    
print(f"Total de números primos: {totalprimos}")