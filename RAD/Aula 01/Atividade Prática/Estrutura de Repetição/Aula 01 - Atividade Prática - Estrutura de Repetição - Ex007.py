"""7 - Faça um programa que leia 5 números e informe o maior número."""

lista_numeros = []
for x in range(5):
    lista_numeros.append(int(input("Informe um número:")))

print("O maior número é " + str(max(lista_numeros)) + ".")