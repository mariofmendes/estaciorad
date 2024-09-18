import sqlite3 as conector


def criar_tabela():
    conexao = conector.connect('exemplo.db')
    cursor = conexao.cursor()
    sql = "create table if not exists usuarios (id integer primary key, nome text not null, idade integer)"
    cursor.execute(sql)

    conexao.commit()
    conexao.close()


def adicionar_usuario():
    conexao = conector.connect('exemplo.db')
    cursor = conexao.cursor()
    sql = "insert into usuarios (nome, idade) values (?, ?)"
    cursor.execute(sql, (nome, idade))
    conexao.commit()
    conexao.close()


def listar_usuarios():
    conexao = conector.connect('exemplo.db')
    cursor = conexao.cursor()
    sql = "SELECT * FROM usuarios"

    cursor.execute(sql)

    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)

    conexao.close()


def atualizar_usuario():
    conexao = conector.connect('exemplo.db')
    cursor = conexao.cursor()
    sql = "UPDATE usuarios SET nome = ?, idade = ? WHERE id = ?"
    cursor.execute(sql, (nome, idade, id))

    conexao.commit()
    conexao.close()


def deletar_usuario():
    conexao = conector.connect('exemplo.db')
    cursor = conexao.cursor()
    sql = "DELETE FROM usuarios WHERE id = ?"
    cursor.execute(sql)

    conexao.commit()
    conexao.close()


def menu():
    print("\n1. Adicionar usuário")
    print("2. Listar usuário")
    print("3. Atualizar usuário")
    print("4. Deletar usuário")
    print("5. Sair")


criar_tabela()

while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        nome = input("Digite o nome do usuário: ")
        idade = int(input("Digite a idade do usuário: "))
        adicionar_usuario()
        print("Usuário adicionado com sucesso!")
    elif escolha == '2':
        print("\nTodos os usuários:")
        listar_usuarios()
    elif escolha == '3':
        id = int(input("Digite o ID do usuário a ser atualizado: "))
        nome = input("Digite o novo nome do usuário: ")
        idade = int(input("Digite a nova idade do usuário: "))
        atualizar_usuario()
        print("Usuário atualizado com sucesso!")
    elif escolha == '4':
        id = int(input("Digite o ID do usuário a ser deletado: "))
        deletar_usuario()
        print("Usuário deletado com sucesso!")
    elif escolha == '5':
        print("Sair do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

