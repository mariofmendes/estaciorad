import sqlite3 as conector


def criar_tabela():
    conexao = conector.connect('exemplo.db')
    cursor = conexao.cursor()
    sql = ("create table if not exists usuarios (id integer primary key, "
           "nome text not null, "
           "idade integer,"
           "dn date,"
           "endereco varchar,"
           "tel char,"
           "sexo text,"
           "profissao text,"
           "objetivo text,"
           "dias_semana text,"
           "horario text,"
           "qntd_dia varchar,"
           "historico text,"
           "fuma text,"
           "alcool text,"
           "medicamentos text,"
           "anabolizantes text,"
           "suplementos text,"
           "limitacao text,"
           "atividade_fisica text,"
           "sono text,"
           "alimenta text,"
           "rotina text)")
    cursor.execute(sql)

    conexao.commit()
    conexao.close()


def adicionar_usuario():
    conexao = conector.connect('exemplo.db')
    cursor = conexao.cursor()
    sql = ("insert into usuarios (nome, idade, dn, "
           "endereco, tel, sexo, profissao, objetivo, "
           "dias_semana, horario, qntd_dia, historico, "
           "fuma, alcool, medicamentos, anabolizantes, "
           "suplementos, limitacao, atividade_fisica, "
           "sono, alimenta, rotina) "
           "values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, "
           "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")
    cursor.execute(sql, (nome, idade, dn, endereco,
                         tel, sexo, profissao, objetivo, dias_semana,
                         horario, qntd_dia, historico, fuma, alcool,
                         medicamentos, anabolizantes, suplementos,
                         limitacao, atividade_fisica, sono, alimenta, rotina))
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
    sql = ("UPDATE usuarios SET nome = ?, idade = ?, dn = ?, endereco = ?, tel = ?, sexo = ?, profissao = ?, objetivo = ?, dias_semana = ?, horario = ?, qntd_dia = ?, historico = ?, fuma = ?, alcool = ?, medicamentos = ?, anabolizantes = ?, suplementos = ?, limitacao = ?, atividade_fisica = ?, sono = ?, alimenta = ?, rotina = ? WHERE id = ?")
    cursor.execute(sql, (nome, idade, dn, endereco, tel, sexo, profissao, objetivo, dias_semana, horario, qntd_dia, historico, fuma, alcool, medicamentos, anabolizantes, suplementos, limitacao, atividade_fisica, sono, alimenta, rotina, id))

    conexao.commit()
    conexao.close()


def deletar_usuario():
    conexao = conector.connect('exemplo.db')
    cursor = conexao.cursor()
    sql = "DELETE FROM usuarios WHERE id = ?"
    cursor.execute(sql, (id,))

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
        nome = input("Nome completo: ")
        idade = int(input("Idade: "))
        dn = input("Data de nascimento: ")
        endereco = input("Endereço: ")
        tel = int(input("Telefone: "))
        sexo = input("Sexo: ")
        profissao = input("Profissão: ")
        objetivo = input("Objetivos com a atividade física: ")
        dias_semana = input("Dias da semana disponíveis para treino: ")
        horario = input("Horários disponíveis para treino: ")
        qntd_dia = input("Pode treinar mais de uma vez por dia? ")
        historico = input("Histórico patológico e cirúrgico (Ex.: Hipertensão, diabetes, tendinite, cirurgias em "
                          "geral etc.): ")
        fuma = input("Você fuma? Com que frequência? ")
        alcool = input("Você consome álcool? Com que frequência? ")
        medicamentos = input("Faz uso de medicamentos? Quais? ")
        anabolizantes = input("Faz uso de anabolizantes e/ou estimulantes? Quais? ")
        suplementos = input("Faz uso de suplementos alimentares? Quais? ")
        limitacao = input("Tem alguma limitação motora? Quais? ")
        atividade_fisica = input("Pratica atividades físicas? Quais? ")
        sono = input("Possui sono regular? Quantas horas diárias de sono (média)? ")
        alimenta = input("Se alimenta regularmente? ")
        rotina = input("Descreva brevemente sua rotina diária (Ex.: horário de trabalho, horários livres, trabalha "
                       "de pé ou sentado o dia todo etc.): ")
        adicionar_usuario()
        print("Usuário adicionado com sucesso!")
    elif escolha == '2':
        print("\nTodos os usuários:")
        listar_usuarios()
    elif escolha == '3':
        id = int(input("Digite o ID do usuário a ser atualizado: "))
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        dn = input("Data de nascimento: ")
        endereco = input("Endereço: ")
        tel = int(input("Telefone: "))
        sexo = input("Sexo: ")
        profissao = input("Profissão: ")
        objetivo = input("Objetivos com a atividade física: ")
        dias_semana = input("Dias da semana disponíveis para treino: ")
        horario = input("Horários disponíveis para treino: ")
        qntd_dia = input("Pode treinar mais de uma vez por dia? ")
        historico = input("Histórico patológico e cirúrgico (Ex.: Hipertensão, diabetes, tendinite, cirurgias em "
                          "geral etc.): ")
        fuma = input("Você fuma? Com que frequência? ")
        alcool = input("Você consome álcool? Com que frequência? ")
        medicamentos = input("Faz uso de medicamentos? Quais? ")
        anabolizantes = input("Faz uso de anabolizantes e/ou estimulantes? Quais? ")
        suplementos = input("Faz uso de suplementos alimentares? Quais? ")
        limitacao = input("Tem alguma limitação motora? Quais? ")
        atividade_fisica = input("Pratica atividades físicas? Quais? ")
        sono = input("Possui sono regular? Quantas horas diárias de sono (média)? ")
        alimenta = input("Se alimenta regularmente? ")
        rotina = input("Descreva brevemente sua rotina diária (Ex.: horário de trabalho, horários livres, trabalha "
                       "de pé ou sentado o dia todo etc.): ")
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

