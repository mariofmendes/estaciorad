"""3 - Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
F - Feminino, M - Masculino, sexo inválido."""

sexo = input("Informe o sexo 'F' para feminino ou 'M' para Masculino: ")

if sexo == 'F':
    print("Sexo feminino")
elif sexo == 'M':
    print("Sexo masculino")
else:
    print("Sexo inválido")