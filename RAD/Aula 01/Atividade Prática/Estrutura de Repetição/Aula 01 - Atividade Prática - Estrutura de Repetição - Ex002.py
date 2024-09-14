"""2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome
 do usuário, mostrando uma mensagem de erro e voltando a pedir as informações."""


while True:
    nome = input("Informe o seu nome: ")
    senha = input("Informe a sua senha: ")

    if senha == nome:
        print("Senha não pode ser igual ao nome, informe outra senha: ")
        continue

    else:
        break