quantidade = 0
soma = 0

while True:
    numero = float(input("Digite um número ou 0 para sair: "))
    
    if numero == 0:
        break
    
    quantidade = quantidade + 1
    soma = soma + numero
    
    if quantidade > 0:
        media = soma / quantidade
    else:
        media = 0
        
    print("Quantidade", quantidade)
    print("Soma", soma)
    print("Média", media)
    