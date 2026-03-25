import mysql.connector

try:
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'g9'
    )

    if conexao.is_connected():
        cursor = conexao.cursor()

        print("CADASTRO DE NOVOS USUÁRIOS G9 ARENA")

        nome = input("Nome Completo: ").capitalize()
        cpf = input("CPF (EX:000.000.000-00): ")
        telefone = input("Telefone (EX: (00)00000-0000): ")
        email = input("E-mail: ")
        data_nasc = input("Data de Nascimento (EX: AAAA-MM-DD): ")
        endereco = input("Endereço: ")

        comando_sql = """INSERT INTO tbl_cliente 
        (cpf_cliente, nome_cliente, telefone_cliente, email_cliente, data_nasc_cliente, endereco_cliente, data_cadastro, status_cliente)
        VALUES (%s, %s, %s, %s, %s, %s, CURDATE(), 'Ativo')"""

        valores = (cpf, nome, telefone, email, data_nasc, endereco)

        cursor.execute(comando_sql, valores)

        conexao.commit()

        print(f"\n Cliente {nome}, cadastrado com sucesso no Banco de Dados!")
        print(f"\n Segue para confirmação dos dados:\n {nome}\n {cpf}\n {telefone}\n {email}\n {data_nasc}\n {endereco}")

except mysql.connector.Error as erro:
    print(f"Erro ao inserir dados: {erro}")

finally:
    if 'conexao' in locals() and conexao.is_connected():
        cursor.close()
        conexao.close()
        print("Conexão encerrada.")

#DICIONARIO:

#%S: UTILIZADO COMO FORMA DE SEGURANÇA PARA QUE O PROGRAMA NÃO REALIZE O COMANDO DE FORMA ERRADA, PARA CONSIDERAR QUE O QUE O USUÁRIO
# DIGITA, SEJA CONSIDERADO COMO APENAS UM TEXTO DE ENTRADA E NÃO UM COMANDO, IMPEDINDO COM QUE O ARMAZENAMENTO DO DADO, ALTERAÇÃO OU
#  EXCLUSÃO, NÃO SEJA REALIZADA PARA UMA MASSA OU TODOS OS USUÁRIOS, APENAS PARA O QUE ELE ENCONTRA COM AQUELE "TEXTO" DIGITADO;
#CURDATE: COMANDO DO MYSQL PARA QUE SEJA CONSIDERADA A DATA ATUAL PARA O CADASTRAMENTO DO USUÁRIO;
#CONEXAO.COMMIT: COMANDO QUE FAZ COM QUE AS INFORMAÇÕES DIGITADAS PELO USUÁRIO NO PYTHON, SEJA SALVO DENTRO DO BANCO DE DADOS.
