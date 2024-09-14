"""5 - Altere o programa anterior permitindo ao usuário informar as populações e as taxas
 de crescimento iniciais. Valide a entrada e permita repetir a operação."""

a = float(input("Informe a quantidade de habitantes da cidade A: "))
b = float(input("Informe a quantidade de habitantes da cidade B: "))
ano = 0

while a <= b:

    a += a * 0.03
    b += b * 0.015
    ano += 1

print ( "A ultrapassa ou iguala a B em ", ano, " anos.")