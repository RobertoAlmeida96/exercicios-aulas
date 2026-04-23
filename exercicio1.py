notaAlunos = float(input("Digite a nota do aluno: "))

if notaAlunos >= 9:
    print("Excelente")
elif notaAlunos >= 7:
    print("Aprovado")
elif notaAlunos >= 5:
    print("Recuperação")
elif notaAlunos < 5:
     print("Reprovado")
else:
    print("Nota inválida ou inesxistente")