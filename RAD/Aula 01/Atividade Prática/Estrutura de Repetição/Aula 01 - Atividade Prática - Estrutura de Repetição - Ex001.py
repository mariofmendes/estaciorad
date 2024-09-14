"""1 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
 pedindo até que o usuário informe um valor válido."""

while True:
    numero = int(input("Informe número:"))

    if numero <= 10 and numero >= 0:
        break

    else:
        print("Valor inválido!")
        continue