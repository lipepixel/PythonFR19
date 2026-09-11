soma = 0

while True:
    numero = float(input("Digite um número ou 0 para parar de somar: "))
    
    if numero == 0:
        break
    
    soma = soma + numero
    
print("Somatória", soma)