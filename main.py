#questão 1


def criarlista(numero):
    lista = []
    for i in range(numero):
        lista.append(0)
    return lista

tamanho=int(input("digite o tamanho da sua lista:"))
lista2 = criarlista(tamanho)
print(lista2)

for i in range(tamanho):
    numdesejado = int(input("digite qual numeroquer colocar na lista:" ))
    lista2[i] = numdesejado


print("Lista")
print(lista2)
print("Lista ordenada")
print(sorted(lista2))
print("Soma da lista")
print(sum(lista2))
print("Maior valor da lista")
print(max(lista2))