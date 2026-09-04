N= int(input("Digite um número: "))

x = 1

soma = 0
while x <= N:
    #print(x)
    print(f"Antes de somar\nX = {x} - Soma = {soma}")
    x+= 1 # -> x = x + 1
    soma += x
    print(f"Antes de somar\nX = {x} - Soma = {soma}")

print(f"Soma total = {soma}")
