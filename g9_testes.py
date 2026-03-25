#MENSAGEM DE BOAS VINDAS AO SISTEMA G9
print ("Seja bem-vindo ao Sistema de Acesso ao G9 Arena Gamer")
nome_digitado = input("Digite o seu nome: ").capitalize()

#Atribuições (Posteriormente integrará ao banco de dados)
cliente_nome = "Alisson"
cliente_status = "Ativo"

# Lógica de Integração
if nome_digitado == cliente_nome and cliente_status == "Ativo":
    print(f"Bem-vindo, {cliente_nome}! Acesso liberado.")
elif nome_digitado == cliente_nome and cliente_status == "Inativo":
    print("Sinto muito, seu acesso foi negado, por gentileza procurar a recepção!")
else:
    print("Cliente não encontrado no sistema.")

