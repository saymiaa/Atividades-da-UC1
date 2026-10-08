#6. Conversor de metros Crie um script que leia uma medida em metros 
# e mostre o valor correspondente em centímetros. 

# digite a médida em metros

medida = float(input("Digite a a medida em metros: "))

#Conversor de metros para centimetros#
medidacm = ((medida)*100)

# RESULTADO #
print(f"a medida em cetimetros é {medidacm:.2f} cm")