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

