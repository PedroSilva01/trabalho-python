# Agenda de Contatos
import sqlite3

"""APAGAR ID DEPOIS DAR UM CLEAR NA AGENDA.DB"""


def getConnection():
    #conectando
    connection = sqlite3.connect('agenda.db')
    #definindo um cursor
    cursor = connection.cursor()
    #criando a tabela(se não existir)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contatos(
             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
             nome TEXT NOT NULL,
             fone TEXT
    );
    """)
    #retorna a conexão
    return connection

def adiciona(nome, tel):
    connection = sqlite3.connect('agenda.db')    
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO contatos(nome, fone)
    VALUES (?, ?)
    """,(nome, tel))
    print("Contato Adicionado!")
    connection.commit()
    connection.close()



def mostraContato(id: str) -> str:
    connection = sqlite3.connect('agenda.db')
    cursor = connection.cursor()
    contato = cursor.execute("""SELECT * FROM contatos WHERE id=?""", (id,)).fetchall()
    print(f"nome: {contato[0][1].capitalize()} \ntelefone: {contato[0][2]}")
    connection.close()
    
    



def mostraLista():
    connection = sqlite3.connect('agenda.db')
    cursor = connection.cursor()
    linhas = cursor.execute("""SELECT * FROM contatos""").fetchall()
    print('\n'.join(map(lambda x: str(x[0]) + ' ' + str(x[1]) + ' ' + str(x[2]), linhas))) 
    connection.close()

def apagaContato(id: str) -> str:
    connection = sqlite3.connect('agenda.db')
    cursor = connection.cursor()
    contato = cursor.execute("""SELECT * FROM contatos WHERE id=?""", (id,)).fetchall()
    cursor.execute("DELETE FROM contatos WHERE id=?", (id,))
    print(f'O contato {contato[0][1].capitalize()} foi deletado com sucesso')
    connection.commit()
    connection.close()

def apagaTodosContatos():
    connection = sqlite3.connect('agenda.db')
    cursor = connection.cursor()
    cursor.execute("""DELETE FROM contatos""")
    print('Todos os contatos foram deletados com sucesso')
    connection.commit()
    connection.close()

# def getConnection():
#     connection = sqlite3.connect('agenda.db')
#     cursor = connection.cursor()
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS contatos(
#         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#         nome TEXT NOT NULL,
#         fone TEXT
#     );
#     """)
#     return connection
