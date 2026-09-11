soma_idades = 0
total_pessoas = 0
soma_salarios_homens = 0
total_homens = 0
mulheres_baixo_salario = 0

while True:
    entrada_idade = input("Digite a idade (valor negativo para encerrar): ")
    idade = int(entrada_idade)
    
    if idade < 0:
        break
    
    sexo = input("Digite o sexo (M/F): ").upper()
    salario = float(input("Digite o salário: R$ "))

    soma_idades = soma_idades + idade
    total_pessoas = total_pessoas + 1

    if sexo == 'M':
        soma_salarios_homens = soma_salarios_homens + salario
        total_homens = total_homens + 1

    if sexo == 'F':
        if salario < 600.00:
            mulheres_baixo_salario = mulheres_baixo_salario + 1

print("\nResultados da Pesquisa")

if total_pessoas > 0:
    media_idade = soma_idades / total_pessoas
    print("a) Média de idade do grupo:", media_idade)
else:
    print("a) Nenhum dado válido foi cadastrado.")

if total_homens > 0:
    media_salarios_homens = soma_salarios_homens / total_homens
    print("b) Média de salários dos homens:", media_salarios_homens)
else:
    print("b) Nenhum homem foi cadastrado.")

print("c) Quantidade de mulheres com salário abaixo de R$ 600,00:", mulheres_baixo_salario)
