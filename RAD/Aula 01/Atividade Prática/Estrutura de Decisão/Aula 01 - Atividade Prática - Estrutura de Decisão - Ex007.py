"""7 - Faça um Programa que leia três números e mostre o maior e o menor deles."""

lista_num=[]

for x in range(1,4):
    lista_num.append(int(input("Informe um número: ")))
print("O maior número é: ", max(lista_num), " e o menor é: ", min(lista_num))