numero=int(input("Bom dia Magnata! Digite um número entre 0 e 10.: "))

while numero < 0 or numero > 10:
    print("Número inválido Magnata. Por favor, digite corretamente.")
    numero=int(input("Digite um número entre 0 e 10: "))

print("Numero aceito Magnata. Obrigado!:", numero)