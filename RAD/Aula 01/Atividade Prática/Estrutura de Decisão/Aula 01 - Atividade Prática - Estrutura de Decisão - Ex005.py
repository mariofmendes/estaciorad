"""Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por
aluno e apresentar:
    - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    - A mensagem "Reprovado", se a média alcançada for menor do que sete;
    - A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

media = (nota1 + nota2)/2

print("A média do aluno foi: ", media)

if 10 > media >=7:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
else:
    print("Aprovado com Distinção")
