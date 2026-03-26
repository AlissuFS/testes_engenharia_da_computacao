import customtkinter as ctk
import mysql.connector

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AppG9(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema G9 Arena - Acesso")
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="Bem-vindo à Arena G9", font=("Roboto", 20))
        self.label.pack(pady=20)

        self.input_nome = ctk.CTkEntry(self, placeholder_text="Digite seu nome...")
        self.input_nome.pack(pady=10)

        self.btn_acessar = ctk.CTkButton(self, text="Verificar Acesso", command=self.validar_acesso)
        self.btn_acessar.pack(pady=20)

    def validar_acesso(self):
        nome_digitado = self.input_nome.get().capitalize()

        try:
            conexao = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='g9'
            )
            cursor = conexao.cursor(buffered=True)
            cursor.execute("SELECT nome_cliente, status_cliente FROM tbl_cliente")
            resultados = cursor.fetchall()

            encontrado = False
            for (nome, status) in resultados:
                if nome == nome_digitado:
                    encontrado = True
                    if status == 'Ativo':
                        self.label.configure(text=f"✅ Acesso Liberado, {nome}!", text_color="green")
                    else:
                        self.label.configure(text="❌ Cadastro Inativo!", text_color="red")
                    break
            
            if not encontrado:
                self.label.configure(text="⚠️ Não cadastrado!", text_color="yellow")

        except Exception as e:
            print(f"Erro: {e}")
        finally:
            conexao.close()

# Rodar o App
app = AppG9()
app.mainloop()


#DICIONARIO:

#CLASS: DEFINIDO PARA CRIAR A INTERFACE
#CTkLABEL: UTILIZADO PARA DENTRO DA INTERFACE APARECER UM TEXTO, COMO O TÍTULO
#CTkENTRY: UTILIZADO PARA QUE APAREÇA UMA CAIXA DE DIGITAÇÃO
#CTkBUTTON: UTILIZADO PARA CRIAR UM BOTÃO COM UMA AÇÃO AO SER CLICADO
#COMMAND: ONDE DEFINIMOS QUAL A AÇÃO QUE SERÁ REALIZADA AO CLICAR NO BOTÃO
#APP.MAINLOOP: COMANDO PARA QUE A TELA FIQUE ABERTA MESMO APÓS FINALIZAR A VALIDAÇÃO DO ACESSO