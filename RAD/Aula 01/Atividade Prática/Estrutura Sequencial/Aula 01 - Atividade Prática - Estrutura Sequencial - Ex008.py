"""8 - Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre
o total do seu salário no referido mês"""

sal = float(input("Informe quanto ganha por hora: "))
hora = float(input("Informe quantas horas trabalhou por mês: "))

total = sal * hora

print("O salário para o referido mês será de: R$", total)