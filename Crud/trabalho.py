import sqlite3 as conector
from tkinter import *
from tkinter import messagebox

# Funções de Banco de Dados
def criar_tabela():
    try:

        conexao = conector.connect('exemplo.db')
        cursor = conexao.cursor()


        sql = ("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, "
               "nome TEXT NOT NULL, idade INTEGER, dn DATE, endereco VARCHAR, "
               "tel CHAR, sexo TEXT, profissao TEXT, objetivo TEXT, dias_semana TEXT, "
               "horario TEXT, qntd_dia VARCHAR, historico TEXT, fuma TEXT, alcool TEXT, "
               "medicamentos TEXT, anabolizantes TEXT, suplementos TEXT, limitacao TEXT, "
               "atividade_fisica TEXT, sono TEXT, alimenta TEXT, rotina TEXT)")
        cursor.execute(sql)


        conexao.commit()
        print("Tabela criada com sucesso.")

    except conector.Error as e:
        # Tratamento de erro para problemas de conexão e execução
        messagebox.showerror("Erro", f"Ocorreu um erro ao criar a tabela: {e}")

    finally:
        
        if conexao:
            conexao.close()
            print("Conexão encerrada.")


# Teste rápido da função
criar_tabela()

def adicionar_usuario(dados):
    conexao = conector.connect('exemplo.db')
    cursor = conexao.cursor()
    sql = ("INSERT INTO usuarios (nome, idade, dn, endereco, tel, sexo, profissao, objetivo, "
           "dias_semana, horario, qntd_dia, historico, fuma, alcool, medicamentos, anabolizantes, "
           "suplementos, limitacao, atividade_fisica, sono, alimenta, rotina) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")
    cursor.execute(sql, dados)
    conexao.commit()
    conexao.close()

def listar_usuarios():
    conexao = conector.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios")
    registros = cursor.fetchall()
    conexao.close()
    return registros

def atualizar_usuario(dados, usuario_id):
    conexao = conector.connect('exemplo.db')
    cursor = conexao.cursor()
    sql = ("UPDATE usuarios SET nome = ?, idade = ?, dn = ?, endereco = ?, tel = ?, sexo = ?, "
           "profissao = ?, objetivo = ?, dias_semana = ?, horario = ?, qntd_dia = ?, historico = ?, "
           "fuma = ?, alcool = ?, medicamentos = ?, anabolizantes = ?, suplementos = ?, limitacao = ?, "
           "atividade_fisica = ?, sono = ?, alimenta = ?, rotina = ? WHERE id = ?")
    cursor.execute(sql, dados + (usuario_id,))
    conexao.commit()
    conexao.close()

def deletar_usuario(usuario_id):
    conexao = conector.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (usuario_id,))
    conexao.commit()
    conexao.close()

# Funções de Interface
def adicionar_usuario_interface():
    dados = (
        nome_var.get(), idade_var.get(), dn_var.get(), endereco_var.get(),
        tel_var.get(), sexo_var.get(), profissao_var.get(), objetivo_var.get(),
        dias_semana_var.get(), horario_var.get(), qntd_dia_var.get(), historico_var.get(),
        fuma_var.get(), alcool_var.get(), medicamentos_var.get(), anabolizantes_var.get(),
        suplementos_var.get(), limitacao_var.get(), atividade_fisica_var.get(),
        sono_var.get(), alimenta_var.get(), rotina_var.get()
    )
    adicionar_usuario(dados)
    messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso!")
    limpar_campos()

def listar_usuarios_interface():
    registros = listar_usuarios()
    texto_lista.delete(1.0, END)
    for registro in registros:
        texto_lista.insert(END, f"{registro}\n")

def atualizar_usuario_interface():
    usuario_id = int(id_var.get())
    dados = (
        nome_var.get(), idade_var.get(), dn_var.get(), endereco_var.get(), tel_var.get(),
        sexo_var.get(), profissao_var.get(), objetivo_var.get(), dias_semana_var.get(),
        horario_var.get(), qntd_dia_var.get(), historico_var.get(), fuma_var.get(),
        alcool_var.get(), medicamentos_var.get(), anabolizantes_var.get(), suplementos_var.get(),
        limitacao_var.get(), atividade_fisica_var.get(), sono_var.get(), alimenta_var.get(),
        rotina_var.get()
    )
    atualizar_usuario(dados, usuario_id)
    messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso!")
    limpar_campos()

def deletar_usuario_interface():
    usuario_id = int(id_var.get())
    deletar_usuario(usuario_id)
    messagebox.showinfo("Sucesso", "Usuário deletado com sucesso!")
    limpar_campos()

def limpar_campos():
    for var in [id_var, nome_var, idade_var, dn_var, endereco_var, tel_var, sexo_var,
                profissao_var, objetivo_var, dias_semana_var, horario_var, qntd_dia_var,
                historico_var, fuma_var, alcool_var, medicamentos_var, anabolizantes_var,
                suplementos_var, limitacao_var, atividade_fisica_var, sono_var,
                alimenta_var, rotina_var]:
        var.set("")

# Configuração Inicial da Interface
root = Tk()
root.title("Ficha de Anamnese")
root.geometry("900x700")
root.config(bg="#f5f5f5")

# Variáveis de Entrada
id_var = StringVar()
nome_var = StringVar()
idade_var = StringVar()
dn_var = StringVar()
endereco_var = StringVar()
tel_var = StringVar()
sexo_var = StringVar()
profissao_var = StringVar()
objetivo_var = StringVar()
dias_semana_var = StringVar()
horario_var = StringVar()
qntd_dia_var = StringVar()
historico_var = StringVar()
fuma_var = StringVar()
alcool_var = StringVar()
medicamentos_var = StringVar()
anabolizantes_var = StringVar()
suplementos_var = StringVar()
limitacao_var = StringVar()
atividade_fisica_var = StringVar()
sono_var = StringVar()
alimenta_var = StringVar()
rotina_var = StringVar()

# Dividir interface em frames para organização
frame_esquerda = Frame(root, padx=20, pady=20, bg="#e0e0e0")
frame_esquerda.grid(row=0, column=0, padx=10, pady=10, sticky="n")

frame_direita = Frame(root, padx=20, pady=20, bg="#f5f5f5")
frame_direita.grid(row=0, column=1, padx=10, pady=10, sticky="n")

# Layout de Formulário (Frame da Esquerda)
Label(frame_esquerda, text="Ficha de Anamnese", font=("Arial", 16, "bold"), bg="#e0e0e0").grid(row=0, column=0, columnspan=2, pady=10)

campos = [
    ("ID", id_var), ("Nome", nome_var), ("Idade", idade_var), ("Data de Nascimento", dn_var),
    ("Endereço", endereco_var), ("Telefone", tel_var), ("Sexo", sexo_var), ("Profissão", profissao_var),
    ("Objetivos", objetivo_var), ("Dias da semana", dias_semana_var), ("Horários para treino", horario_var),
    ("Treina mais de uma vez por dia?", qntd_dia_var), ("Histórico médico", historico_var),
    ("Fuma?", fuma_var), ("Consome álcool?", alcool_var), ("Usa medicamentos?", medicamentos_var),
    ("Usa anabolizantes?", anabolizantes_var), ("Usa suplementos?", suplementos_var),
    ("Limitações motoras", limitacao_var), ("Atividades físicas", atividade_fisica_var),
    ("Sono regular?", sono_var), ("Alimenta-se bem?", alimenta_var), ("Rotina", rotina_var)
]

for i, (campo, var) in enumerate(campos, start=1):
    Label(frame_esquerda, text=campo, font=("Arial", 10), anchor="w", bg="#e0e0e0").grid(row=i, column=0, sticky=W, pady=2)
    Entry(frame_esquerda, textvariable=var, width=30).grid(row=i, column=1, padx=5, pady=2)

# Botões no frame esquerdo
Button(frame_esquerda, text="Adicionar", command=adicionar_usuario_interface, width=15).grid(row=30, column=0, pady=10)
Button(frame_esquerda, text="Atualizar", command=atualizar_usuario_interface, width=15).grid(row=30, column=1, pady=10)
Button(frame_esquerda, text="Limpar Campos", command=limpar_campos, width=32).grid(row=31, column=0, columnspan=2, pady=10)

# Área de Exibição e Botões no frame direito
Label(frame_direita, text="Lista de Usuários", font=("Arial", 14, "bold"), bg="#f5f5f5").grid(row=0, column=0, pady=10)
texto_lista = Text(frame_direita, height=25, width=50)
texto_lista.grid(row=1, column=0, pady=10)

Button(frame_direita, text="Listar", command=listar_usuarios_interface, width=20).grid(row=2, column=0, pady=10)
Button(frame_direita, text="Deletar", command=deletar_usuario_interface, width=20).grid(row=3, column=0, pady=5)

# Criação da tabela no banco de dados
criar_tabela()

# Iniciar interface gráfica
root.mainloop()
