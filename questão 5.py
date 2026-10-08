#5. Calculando a idade Crie um script que leia o nome, o ano de nascimento e o ano atual. 
# Depois, mostre uma mensagem informando a idade aproximada da pessoa. #

#aqui o usuario digita seus dados#
nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

# cálculamos a idade usando as variaveis#
idade = ano_atual - ano_nascimento

#resultado é impreso na tela#
print(f"{nome} tem aproximadamente {idade} anos.")
