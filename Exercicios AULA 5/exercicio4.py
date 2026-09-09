maior = 0

for x in range(6):
    numero = int(input("Digite um número: "))
    if numero > maior:
        maior = numero

print("O maior número digitado foi:", maior)