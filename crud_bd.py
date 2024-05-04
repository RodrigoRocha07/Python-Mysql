import mysql.connector

def create(nome, idade, numero, email):
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='bd_cadastro')

    cursor = conexao.cursor()

    try:
        comando = f'INSERT INTO pessoas (nome, idade, numero, email) VALUES ("{nome}",{idade},"{numero}","{email}" )'
        cursor.execute(comando)
        conexao.commit()
        print("Registro inserido com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao inserir registro: {erro}")
    finally:
        cursor.close()
        conexao.close()

def read():
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='bd_cadastro')

    cursor = conexao.cursor()

    try:
        comando = f'SELECT * FROM pessoas'
        cursor.execute(comando)
        resultados = list(cursor.fetchall())
        for resultado in resultados:
            print(resultado)
    except mysql.connector.Error as erro:
        print(f"Erro ao ler registros: {erro}")
    finally:
        cursor.close()
        conexao.close()

def updateNome(nome, nomeNovo):
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='bd_cadastro')

    cursor = conexao.cursor()

    try:
        comando = f'UPDATE pessoas SET nome ="{nomeNovo}" WHERE nome = "{nome}" '
        cursor.execute(comando)
        conexao.commit()
        print("Atualizado com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao atualizar registro: {erro}")
    finally:
        cursor.close()
        conexao.close()

def delete(nome):
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='bd_cadastro')

    cursor = conexao.cursor()

    try:
        comando = f'DELETE FROM pessoas WHERE nome = "{nome}"'
        cursor.execute(comando)
        conexao.commit()
        print("Deletado com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao deletar registro: {erro}")
    finally:
        cursor.close()
        conexao.close()

def listar():

    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='bd_cadastro')

    cursor = conexao.cursor()

    comando = 'SELECT * FROM pessoas'
    cursor.execute(comando)
    lista = cursor.fetchall()
    return lista

# Em cada função estão os passos:
#Passo 1 - Fazer conexao com banco de dados
#Passo 2 - Iniciar variavel "Cursor"
#Passo 3 - Colocar o comando SQL dentro de uma variavel "comando"
#Passo 4 - Execultar a variavel "comando" com "cursor.execute(comando)"
#Passo 5 - Fazer o commit caso tenha ocorrido alteração no banco
#Passo 6 - Finalizar interação com o banco