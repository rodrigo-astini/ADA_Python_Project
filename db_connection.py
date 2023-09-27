import pyodbc

#Criando Conexão com BD
def retorna_cursor_bd():
    connection = pyodbc.connect(retorna_string_conexao_bd())
    cursor = connection.cursor()
    return cursor, connection

def retorna_string_conexao_bd():
    return(
        "DRIVER={SQL Server};"
        "SERVER=hoesql633.na.xom.com;"
        "DATABASE=SkillUp_RMASTIN;"
        "UID=rmastin;"
        "Trusted_Connection=yes"
    )

#Função Cadastrar
def insert_cliente_bd(cliente):
    print (cliente)
    cursor, connection = retorna_cursor_bd()
    insert_query = """
    INSERT INTO cliente (nome, cpf, rg, data_nascimento, cep, logradouro, bairro, cidade, estado, complemento, numero_residencia)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """
    values = (cliente['nome'], cliente['cpf'], cliente['rg'], cliente['nascimento'], cliente['cep']['CEP'], cliente['cep']['Logradouro'], cliente['cep']['Bairro'], cliente['cep']['Cidade'], cliente['cep']['Estado'], cliente['complemento'], cliente['numero'])
    cursor.execute(insert_query, values)
    connection.commit()
    print ("Cliente inserido na base de dados com sucesso!")
    
#Função Alterar
def update_cliente_bd(cliente):
    cursor, connection = retorna_cursor_bd()
    update_query = "UPDATE cliente SET nome = '" +cliente['nome']+ "', rg = '" +cliente['rg']+ "', data_nascimento = '" +cliente['nascimento']+ "', cep = '"+cliente['cep']['CEP']+ "', logradouro = '" +cliente['cep']['Logradouro']+ "', bairro = '" +cliente['cep']['Bairro']+ "', cidade = '" +cliente['cep']['Cidade']+ "', estado = '"+cliente['cep']['Estado']+ "', complemento = '" +cliente['complemento']+ "', numero_residencia = '"+cliente['numero']+ "' WHERE cpf = '" + cliente['cpf'] + "';"
    cursor.execute(update_query)
    connection.commit()
    print ("Registro Alterado na Base de Dados!")

#Função Buscar
def busca_cliente_bd(cliente):
    cursor, connection = retorna_cursor_bd()
    buscar_query = "SELECT * FROM cliente where cpf = '" + cliente['cpf'] + "';"
    cursor.execute(buscar_query)
    cliente = cursor.fetchall()
    print(cliente)
    connection.commit()

#Função Excluir  
def delete_cliente_bd(cliente):
    cursor, connection = retorna_cursor_bd()
    delete_query = "DELETE FROM cliente WHERE cpf = '" + cliente['cpf'] + "';"
    cursor.execute(delete_query)
    connection.commit()
    print ("Registro excluído da Base de Dados!")

#Função Listar
def select_cliente_bd():
    cursor, connection = retorna_cursor_bd()
    cursor.execute("select * from cliente;")
    clientes = cursor.fetchall()
    print(clientes)
    connection.commit()