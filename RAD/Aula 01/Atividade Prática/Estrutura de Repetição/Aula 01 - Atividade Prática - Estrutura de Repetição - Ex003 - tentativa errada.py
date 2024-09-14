"""3 - Faça um programa que leia e valide as seguintes informações:
a) Nome: maior que 3 caracteres;
b) Idade: entre 0 e 150;
c) Salário: maior que zero;
d) Sexo: 'f' ou 'm';
e) Estado Civil: 's', 'c', 'v', 'd';
"""
"""
while True:
    nome = input("Informe o seu nome: ")
    if len(nome) > 3:
        break
    else:
        print("Nome inválido!")
        continue

while True:
    idade = int(input("Informe a sua idade: "))
    if idade >= 0 and idade <= 150:
        break
    else:
        print("Idade inválida!")
        continue

while True:
    salario = float(input("Informe o seu salário: "))
    if salario < 0:
        print("Salário inválido!")
        break
    else:
        continue

while True:
    sexo = input(("Informe o seu sexo: "))
    if sexo == 'f' or 'm':
        print("Sexo inválido!")
        break
    else:
        continue

while True:
    ecivil = input("Informe seu estado civil: ")
    if ecivil == 's' or 'c' or 'v' or 'd':
        print("Estado civil inválido!")
        break
    else:
        continue
"""

