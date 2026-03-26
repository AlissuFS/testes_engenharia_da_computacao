import mysql.connector

try:
    conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'g9'
    )

    if conexao.is_connected():
        cursor = conexao.cursor(buffered=True)

        print("1 - Acessar Arena")
        print("2 - Novo Cadastro")
        opcao = input("Escolha uma opção (1 ou 2): ")

        if opcao == "1":
            cursor.execute("SELECT nome_cliente, status_cliente from tbl_cliente")
            resultado = cursor.fetchall()
            encontrado = False
            nome_digitado = input("Digite seu nome: ").capitalize()
            for (nome, status) in resultado:
                if nome == nome_digitado:
                    encontrado = True
                    if status == 'Ativo':
                        print(f"\nBem-vindo {nome}! Acesso Liberado.")
                    else:
                        print(f"\nSinto muito {nome}, seu cadastro está Inativo, por gentileza procurar a recepção.")
                    break
            if not encontrado:
                print("perfil não cadastrado!")
        elif opcao == "2":
            nome = input("Nome Completo: ").capitalize()
            cpf = input("CPF (EX:000.000.000-00): ")
            telefone = input("Telefone (EX: (00)00000-0000): ")
            email = input("E-mail: ")
            data_nasc = input("Data de Nascimento (EX: AAAA-MM-DD): ")
            endereco = input("Endereço: ")

            comando_sql = """INSERT INTO tbl_cliente
            (cpf_cliente, nome_cliente, telefone_cliente, email_cliente, data_nasc_cliente, endereco_cliente, data_cadastro, status_cliente)
            values (%s, %s, %s, %s, %s, %s, CURDATE(), 'Ativo')"""

            valores = (cpf, nome, telefone, email, data_nasc, endereco)

            cursor.execute(comando_sql, valores)

            conexao.commit()

            print(f"{nome}, seu cadastro foi finalizado com sucesso!")
        else:
            print("Opção Invalida, reinicie o programa")

except mysql.connector.Error as erro:
    print(f"Erro ao inserir dados: {erro}")

finally:
    if 'conexao' in locals() and conexao.is_connected():
        cursor.close()
        conexao.close()
        print("\nConexão encerrada.\n")

