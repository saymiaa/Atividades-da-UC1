#9. Cadastro de jogador Crie um script que leia o nome de um jogador, o nome do seu time, sua idade e seu número da camisa. 
# Depois, mostre uma frase apresentando o jogador com todas as informações. 

Nome_jogador = input("Digite o nome do jogador: ")
Time = input("Digite o nome do seu time do Coração: ")
idade_jogador = int(input("Digite a idade do jogador :"))
numero_camisa = int(input("Digite o número da camisa do jogador :"))

print("\n--- Detalhes do Jogador ---")
print(f"O nome do jogador é: {Nome_jogador}, o time do seu coração é o {Time}, sua idade é {idade_jogador}, e o numero da sua camisa é a {numero_camisa}.")