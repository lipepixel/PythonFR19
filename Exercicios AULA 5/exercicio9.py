n = int(input("Digite um número inteiro positivo: "))

soma = 0

for x in range(1, n + 1):
    soma = soma + (1 / x)
    
print("Soma", soma)