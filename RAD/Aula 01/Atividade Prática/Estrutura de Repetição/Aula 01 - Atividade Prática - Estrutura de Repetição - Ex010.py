"""10 - Faça um programa que receba dois números inteiros e gere os números inteiros que
estão no intervalo compreendido por eles."""

"""
lista_numeros = [int(input("Numero:")) for x in range(2)]
#faz iteracao para obter a sequencia dos numeros.
intervalo = [x for x in range(min(lista_numeros),max(lista_numeros))]

#imprimir na tela o intervalo.
print (intervalo)
"""
"""
num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))

while num2 < num1:

    num1 = int(input("Informe um número: "))
    num2 = int(input("Informe outro número: "))

else:
    for x in range(num1+1,num2):
        print(x)
"""

n1 = int(input('Infome um número: '))
n2 = int(input('Infome outro número: '))

if n1 > n2:
    for a in range(n2+1,n1):
        print(a)

elif n1 < n2:
    for a in range(n1+1,n2):
        print(a)
else:
    print('Os numeros são iguais.')

