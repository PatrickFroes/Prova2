def criarmartriz(altura,largura):
    matriz = []
    for i in range(altura):
        matriz.append(largura*[0])
    return matriz


par = 0
maior = 0
altura1 = int(input("Digite a altura desejada para a matriz:"))
largura1 = int(input("Digite a largura desejada para a matriz:"))

matriz = criarmartriz(altura1,largura1)

for a in range(altura1):
    print(matriz[a])

for cont in range(altura1):
    for conta in range(largura1):
        num = int(input("Digite o numero que seja colocar na matriz:"))
        matriz[cont][conta] = num

for a in range(altura1):
    print(matriz[a])

for i in range(altura1):
    for j in range(largura1):
        nume = matriz[i][j]
        if nume%2 == 0:
            par = par + 1

print("A quantidade de numeros pares é:", par)

for i in range(altura1):
    for j in range(largura1):
        numero = matriz[i][j]
        if maior < numero:
            maior = numero

print("O maior valor da matriz é:", maior)

