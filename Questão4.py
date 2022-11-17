matriz = []

for altura in range(5):
    matriz.append(5*[0])

for i in range(5):
    matriz[i][i] = 1

for a in range(5):
    print(matriz[a])