salario = float(input("Digite o salário do funcionário: R$ "))

if salario > 1250:
    aumento = salario * 0.10
    novo_salario = salario + aumento
else:
    aumento = salario * 0.15
    novo_salario = salario + aumento

print(f"Novo salário: R$ {novo_salario:.2f}")
