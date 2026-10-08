matriz = [  
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print("O elemento da linha 0 e da coluna 1 é:", matriz[0][1])  #linha0 posição 1
print("O elemento da linha 1 e da coluna 2 é:", matriz[1][2])  #linha1 posição 2
print("O elemento da linha 2 e da coluna 0 é:", matriz[2][0])  #linha2 posição 0

matriz = [  
    [5, 8, 3],
    [2, 7, 9],
    [4, 6, 1]
]

for linha in matriz:
         print(linha)                   #imprime todos os números da matriz
    
for linha in matriz:
    for numero in linha:
         print("Os elementos da matriz são:", numero)   
         
         
for linha in matriz:
    for numero in linha:
        if numero % 2 == 0:
            print("Os números pares da matriz são:", numero)    #imprime todos os números pares dentro da matriz
            
for linha in matriz:
    for numero in linha:
        if numero > 5:
            print("Os números maiores que 5 da matriz são:", numero)  #imprime todos os números maiores que 5 dentro da matriz
            
            

matriz = [  
    [7, 8, 9],
    [5, 6, 7],
    [8, 9, 10]
]   

soma = 0

for linha in matriz:
    for numero in linha:
        soma += numero

print("A soma dos elementos da matriz é:", soma)  #imprime a soma de todos os números dentro da matriz  

média = soma / (len(matriz) * len(matriz[0]))
print("A média dos elementos da matriz é:", média) #imprime a média de todos os números dentro da matriz


maior = matriz[0][0]
            
for linha in matriz:
    for numero in linha:
        if numero > maior:
            maior = numero

print("O maior número da matriz é:", maior)  #imprime o maior número dentro da matriz     


menor = matriz[0][0]
            
for linha in matriz:
    for numero in linha:
        if numero < menor:
            menor = numero

print("O menor número da matriz é:", menor)  #imprime o menor número dentro da matriz    


matriz = []

for i in range(2):
    linha = []
    
    for j in range(3):
        numero = int(input("Digite um número: "))
        linha.append(numero)        
    matriz.append(linha)    

for linha in matriz:
    print(linha)   #cria uma matriz 2x3 com os números digitados pelo usuário e imprime a matriz na tela.


soma = 0

for i in range(3):
    linha = []
    
    for j in range(3):
        nota = int(input("Digite a nota do aluno:"))
        linha.append(nota)
    
    matriz.append(linha)
    
for linha in matriz:
    print(linha)

média = soma / (len(matriz) * len(matriz[0]))
print("A média dos elementos da matriz é:", média)


soma = 0
    
for j in range(3):
        numero = float(input("Digite a nota do aluno: "))
   
        soma += numero
        media = soma / 3
print("A média das notas dos alunos é:", media)


    
matriz = []

for i in range(4):
    linha = []
    
    for j in range(3):
        numero = int(input("Digite um número: "))
        linha.append(numero)        
    matriz.append(linha)    

for linha in matriz:
    print(linha) 

else:
    if numero: 0 
    print("Os assentos disponíveis são os de número:", 0)
    if numero: 1
    print("Os assentos ocupados são os de número:", 1)
  
for numero in matriz[0]:
      sum += 
print(sum, "assentos disponíveis")

for numero in matriz[1]:
    sum += 
print(sum, "assentos ocupados")


