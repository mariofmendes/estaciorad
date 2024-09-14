"""8 - Faça um programa que leia 5 números e informe a soma e a média dos números."""

lista_num = []
for x in range(5):
    lista_num.append(int(input("Informe um número: ")))

soma = sum(lista_num)
media = soma/len(lista_num)

print("A soma é: ", soma, " e a média é: ", media)
