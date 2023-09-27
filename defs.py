from db_connection  import *
from utils import *

def menu():
    print()
    print('-' * 20)
    print('Menu Principal')
    print('-' * 20)
    print()
    print('[1] - Cliente')
    print('[2] - Ordem')
    print('[3] - Realizar Análise da Carteira')
    print('[4] - Imprimir Relatório da Carteira')
    print('[5] - Sair')
    print()

    resp = int(input('Informe a opção desejada:'))
    if resp == 1:
        limpaTerminal()
        menu_cliente()
    elif resp == 5:
        pass
    else:
        limpaTerminal()
        menu()
    
def menu_cliente():
    print()
    print('-' * 20)
    print('Menu Cliente')
    print('-' * 20)
    print()
    print('[1] - Cadastrar Cliente')
    print('[2] - Alterar Cliente')
    print('[3] - Buscar Cliente')
    print('[4] - Excluir Cliente')
    print('[5] - Listar Clientes')
    print('[6] - Voltar ao Menu Principal')
    print()

    resp = int(input('Informe a opção desejada:'))
    if resp == 1:
        limpaTerminal()
        cadastro_cliente()
    elif resp == 2:
        limpaTerminal()
        altera_cliente()
    elif resp == 3:
        limpaTerminal()
        busca_cliente()
    elif resp == 4:
        limpaTerminal()
        exclui_cliente()
    elif resp == 5:
        limpaTerminal()
        lista_cliente()
    elif resp == 6:
        limpaTerminal()
        menu()
    else:
        limpaTerminal()
        print("Opção Inválida!")
        menu_cliente()

#Opção 1 - Cadastrar Cliente
def cadastro_cliente():
    cliente_dicionario = { 
    "nome": input("Informe o Nome do Cliente: "),
    "cpf": valida_cpf(input("Informe o CPF do Cliente: ")),
    "rg": valida_rg(input("Informe o RG do Cliente: ")),
    "nascimento": valida_nascimento(),
    "cep": valida_cep(input("Informe o CEP do Cliente: ")),
    "complemento" : input("Informe o Complemento do Endereço: "),
    "numero" : input("Informe o Número da Residência: ")
    }
    insert_cliente_bd(cliente_dicionario)

#Opção 2 - Alterar Cliente
def altera_cliente():
    cliente_dicionario = {
    "cpf": valida_padrao_cpf(input("Informe o CPF do Cliente: ")),
    "nome": input("Informe o Novo Nome: "),
    "rg": valida_rg(input("Informe o novo RG do cliente: ")),
    "nascimento": valida_nascimento(),
    "cep": valida_cep(input("Informe o novo CEP do cliente: ")),
    "complemento" : input("Informe o novo complemento do endereco: "),
    "numero" : input("Informe o novo numero da residência do cliente: ")
    }
    update_cliente_bd(cliente_dicionario)

#Opção 3 - Buscar Cliente
def busca_cliente():
    cliente_dicionario = {
    "cpf": valida_padrao_cpf(input("Informe o CPF do cliente a ser buscado: "))
    }
    busca_cliente_bd(cliente_dicionario)

#Opção 4 - Excluir Cliente
def exclui_cliente():
    cliente_dicionario = {
    "cpf": valida_padrao_cpf(input("Informe o CPF do cliente a ser buscado: "))
    }
    delete_cliente_bd(cliente_dicionario)

#Opção 5 - Listar Clientes
def lista_cliente():
    select_cliente_bd()