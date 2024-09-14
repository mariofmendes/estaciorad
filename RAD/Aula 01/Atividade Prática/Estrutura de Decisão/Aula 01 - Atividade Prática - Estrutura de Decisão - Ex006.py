"""
6 - Faça um programa que leia três números e mostre o maior deles.
"""

lista_numeros = []
for x in range(1, 4):
    lista_numeros.append(int(input("Informe um número:")))

print("O maior número é " + str(max(lista_numeros)) + ".")