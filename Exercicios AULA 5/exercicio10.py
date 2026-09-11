aprovados = 0
soma = 0

for x in range(80):
    nota = float(input("Digite a nota do aluno: "))
    
    if nota >= 6:
        aprovados = aprovados + 1
        
    soma = soma + nota
    
    media = soma / 80

print("Quantidade de alunos aprovados:", aprovados)
print("Média da turma:", media)