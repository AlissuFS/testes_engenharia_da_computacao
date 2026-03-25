#CONECTOR PYTHON COM O MYSQL
import mysql.connector

# Estabelecer conexão com o banco de dados
try:
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='g9'
    )
    if conexao.is_connected():
        cursor = conexao.cursor(buffered = True)
        cursor.execute("SELECT nome_cliente, status_cliente FROM tbl_cliente")

        resultados = cursor.fetchall()

        nome_digitado = input("Digite seu nome para acessar: ").capitalize()

        encontrado = False
        for (nome, status) in resultados:
            if nome == nome_digitado:
                encontrado = True
                if status == 'Ativo':
                    print(f"\n Bem-vindo, {nome}! Acesso liberado.")
                else:
                    print(f"\n Sinto muito, {nome}. Seu acesso foi negado. Por favor, procure a recepção da Arena")
                break
        if not encontrado:
            print("\n Cliente não encontrado em sistema, por favor, realizar o cadastro caso ainda não tenha, caso já possua, procurar a recepção.")

except mysql.connector.Error as erro:
    print(f"Erro ao conectar ao banco de dados: {erro}")

finally:
    if 'conexao' in locals() and conexao.is_connected():
        cursor.close()
        conexao.close()
        print("\n Conexão com o banco de dados encerrada com segurança.")

#DICIONARIO:

#TRY: UTILIZADO PARA QUE O CÓDIGO TENTE ALGO, NESSE CASO, ELE VAI TENTAR A CONEXÃO COM O BANCO DE DADOS;
#EXCEPT: UTILIZADO PARA EVITAR QUE O PROGRAMA TRAVE E BUSQUE UMA OUTRA SAÍDA, QUE SERIA INDICAR QUAL O ERRO COM A CONEXÃO;
#FINALLY: COMANDO UTILIZADO PARA ENCERRAR A CONEXÃO COM O BANCO DE DADOS;
#MYSQL.CONNECTOR.CONNECT: UTILIZADO PARA QUE O PROGRAMADOR INDIQUE DA ONDE ELE VAI PUXAR AS INFORMAÇÕES, INDICANDO QUEM É O HOST, USUÁRIO E SENHA, QUAL BANCO DE DADOS
# DAQUELE HOST QUE SERÁ UTILIZADO PARA RETIRAR AS INFORMAÇÕES;
#CONEXAO.IS.CONNECTED: VERIFICAÇÃO DE SEGURANÇA PARA GARANTIR QUE A CONSULTA NÃO TENHA CAÍDO ANTES DE COMEÇAR A TRABALHAR;
#CURSOR = CONEXAO.CURSOR: SERÁ O RESPONSÁVEL POR "PEGAR" AS INFORMAÇÕES E TRAZER PARA A SUA CONSULTA;
#BUFFERED=TRUE: TUDO QUE O CONEXAO.CURSOR TROUXER COMO INFORMAÇÕES, FARÁ COM QUE FIQUE ARMAZENADO NA MEMÓRIA TEMPORÁRIA;

#MANIPULAÇÃO DE DADOS: 
#CURSOR.EXECUTE(SELECT...): É O INDICADOR DE QUAIS COLUNAS DO BANCO DE DADOS QUE VOCÊ PRECISA DA INFORMAÇÃO;
#RESULTADOS = CURSOR.FETCHALL: FAZ COM QUE TODOS OS RESULTADOS LISTADOS ESTEJAM DENTRO DA VARIÁVEL RESULTADOS;
#INPUT: COMANDO QUE INDICA QUE O USUÁRIO DIGITE O SEU NOME PARA A VALIDAÇÃO
#CAPITALIZE: COMANDO QUE GARANTE QUE INDEPENDENTE DA FORMA QUE O USUARIO DIGITE O SEU NOME, SEJA COM A PRIMEIRA LETRA MAIUSCULA OU TODOS OS CARACTERES MINUSCULOS
# ELE CONTINUE A CONSULTA E ENTENDENDO QUE ESSA VARIAÇÃO NÃO TORNE O USUÁRIO INVALIDO
#FOR (NOME, STATUS) IN RESULTADOS: LAÇO DE REPETIÇÃO, ONDE FAZ COM QUE O PROGRAMA ACESSE A LISTA NA VARIAVEL RESULTADOS
#IF NOME == NOME_DIGITADO: FAZ A COMPARAÇÃO COM O QUE O USUARIO DIGITOU, COM O QUE HÁ NO BANCO DE DADOS E ASSIM, POSSA VER QUAL O STATUS (ATIVO OU INATIVO)
#BREAK: COMANDO QUE FAZ COM QUE ASSIM QUE O PROGRAMA ACHE O USUARIO DIGITADO, ELE PARE DE FAZER A PROCURA E ENCERRE O COMANDO FOR, PARA QUE NÃO FAÇA A LEITURA COMPLETA DA LISTA;
