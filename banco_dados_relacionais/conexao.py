import sqlite3

conexao = sqlite3.connect("clientes.db")
print(conexao)
cursor = conexao.cursor()

###CRIANDO TABLEA###
#cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(50))" )


###INSERINDO DADOS NA TABELA###
#cursor.execute('INSERT INTO clientes (nome, email) VALUES ("Talita" ,"talita@gmail.com")')
#conexao.commit()


###ATUALIZANDO OU MODIFICANDO A TABELA###
#cursor.execute ("UPDATE clientes SET nome= 'Talita', email= 'talita@gmail.com' WHERE id=2;")
#conexao.commit()


###INSERINDO MAIS REGISTRO NA TABELA###
#cursor.execute ("UPDATE clientes SET nome= 'Lorena', email= 'lorena@gmail.com' WHERE id=3;")
#conexao.commit()

                
###DELETANDO REGISTRO DA TABELA### 
#cursor.execute("DELETE FROM clientes WHERE id=3;")
#conexao.commit()

###INSERINDO MUITOS REGISTROS NA TABELA DE UMA VEZ SÓ###
#def inserir_muitos(conexao, cursor, dados):
   #cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?)", dados)
    #conexao.commit()

#dados = [
    #("Joao", "joao@gmail.com"), 
    #("Isadora", "isa@gmail.com"), 
    #("Léo Natel", "natel@gmail.com"),


#inserir_muitos(conexao, cursor, dados)  

###CONSULTANDO DADOS DA TABELA###
def recurperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

cliente = recurperar_cliente(cursor, 2)
print(cliente)


def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes;") ### USAR OEDER BY PARA MUDAR A ORDEM DO CURSOR###

    

clientes = listar_clientes(cursor)
for cliente in clientes:
    print(cliente)