#8. Temperatura Crie um script que leia uma temperatura em graus Celsius 
# e mostre a temperatura convertida para Fahrenheit. 


temperatura_celsius = float(input("Digite a Temperatura em graus Celsius: "))

# conversão de temperatura de graus celsius para Fahrenheit: 
#simplificarmos a fórmula, temos:
# F = Celsius x 1,8 + 32

temp_Fahrenheit = (temperatura_celsius)*1.8+32

print (f"A temperatura em Fahrenheit é: {temp_Fahrenheit:.2f} F")