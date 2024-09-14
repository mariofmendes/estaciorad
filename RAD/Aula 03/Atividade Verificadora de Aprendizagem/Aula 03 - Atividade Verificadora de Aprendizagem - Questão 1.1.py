"""1.1 - Desenvolva um programa em Python que escreva em disco um arquivo com números ordenados
crescentemente de 1 a 100. Cada número deve ser separado por “;”. O arquivo deve se chamar
“crescente.txt”."""
"""
arquivo= open("Crescente.txt","w")
for numeros in range(1,101):
   arquivo.write(str(numeros) + "; ")
   print(numeros)
arquivo.close()
"""
with open('Crescente.txt', 'w') as arquivo:
   arquivo.write('; '.join(str(n) for n in range(1, 101)))