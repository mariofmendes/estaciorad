"""2 - Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo."""

num = float(input("Informe um número: "))

if num > 0:
    print("O número informado ", num, " é positivo")
elif num == 0:
    print("O número informado é zero")
else:
    print("O número informado ", num, " é negativo")