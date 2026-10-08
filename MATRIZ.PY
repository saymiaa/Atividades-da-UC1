matriz = [ 
    [5, 8, 9],
    [7, 3, 9], #linha1 posição 2
    [4, 6, 1]
]


print(matriz[1][2])  #linha1 posição 2




matriz = [
    [10, 20]
    [30, 40]
]

matriz = [0][1] = 99


print(matriz)

#substitui o 20 pelo 99.




matriz = [
    [10, 20, 30],
    [40, 50, 60],
]

for numero in matriz [0]:
    print(numero)                       #imprime os números da primeira linha da matriz
 
for linha in matriz:
         print(linha)                   #imprime todos os números da matriz
    
for linha in matriz:
    for numero in linha:
         print(numero)                   #imprime todos os números da matriz
            
            
            
matriz = [
       [10, 20, 30],
       [40, 50, 60]
    
] 

# o i e a linha
# o j e a coluna
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j])
        
        
       #-----Implementar----   
       
       
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print("Linha:", i)
        print("Coluna:", j)
        print("Valor:", matriz[i][j])
    
          
          
          
matriz = []

for i in range(3):
    linha = []
    
    for j in range(3):
        numero = int(input("Digite um número: "))
        linha.append(numero)        
    matriz.append(linha)      #criou uma matriz 3x3 com os números digitados pelo usuário.

for linha in matriz:
    print(linha)   
     
    
    soma = 0

for linha in matriz:
    for numero in linha:
        soma += numero

print("Soma:", soma)  #imprime a soma de todos os números dentro da matriz

for linha in matriz:
    for numero in linha:
        if numero % 2 == 0:
            print(numero)  #imprime todos os números pares dentro da matriz
          
          
for linha in matriz:
    for numero in linha:
        if numero % 2 != 0:
            print(numero)  #imprime todos os números ímpares dentro da matriz


for linha in matriz:
    for numero in linha:
        if numero < 10:
            print(numero)  #imprime todos os números menores que 10 dentro da matriz
            
for linha in matriz:
    for numero in linha:
        if numero == 10:
            print(numero)  #imprime todos os números iguais a 10 dentro da matriz
            

for linha in matriz:
    for numero in linha:
        if numero != 10:
            print(numero)  #imprime todos os números diferentes de 10 dentro da matriz
 
quantidade = 0
            
for linha in matriz:
    for numero in linha:
        if numero % 2 == 0:
            quantidade += 1
            
print("Quantidade de números pares:", quantidade)  #imprime a quantidade de números pares dentro da matriz

maior = matriz[0][0]
            
for linha in matriz:
    for numero in linha:
        if numero > maior:
            maior = numero

print("Maior número:", maior)  #imprime o maior número dentro da matriz

soma = 0

for numero in matriz[0]:
    soma += numero
    
print("Soma da primeira linha:", soma)  #imprime a soma de todos os números da primeira linha da matriz
           
soma = 0

for numero in matriz[0]:
    soma += numero
    
print("Soma da segunda linha:", soma) #imprime a soma de todos os números da segunda linha da matriz

   
soma = 0
for i in range(len(matriz)):
    soma += matriz[i][0]  

print("Soma da primeira coluna:", soma)  #imprime a soma de todos os números da primeira coluna da matriz


