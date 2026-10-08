#7. Compra no mercado Crie um script que leia o nome de um produto, 
# #seu preço e a quantidade comprada. Depois, 
# #mostre o nome do produto e o valor total da compra. 

nome_do_produto = input("Digite o nome do produto: ")
preco = float(input("Digite o Preço: "))
quantidade = int(input("Digite a Quantidade Comprada: "))
valor_total = (preco*quantidade)
#resultado impreso na tela:

print("\n--- Detalhes do produto ---")
print(f"Nome do produto: {nome_do_produto}")
print(f"Preço do Produto: R$ {preco} ")
print(f"Valor total da compra: R$ {valor_total:.2f} ")