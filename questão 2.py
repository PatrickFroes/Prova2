import random
import time

dado = [1,2,3,4,5,6]
jogador1 = []
jogador2 = []

print("Digite 1 para jogar")
print("Digite 2 para sair")

escolha = int(input("Qual sua escolha?"))

while escolha == 1:
    escolhido = random.choice(dado)
    print("Jogador um tirou o numero:", escolhido)
    jogador1.append(escolhido)
    time.sleep(3)
    escolhido2 = random.choice(dado)
    print("Jogador dois tirou o numero:", escolhido2)
    jogador2.append(escolhido2)

    print("Digite 1 para continuar")
    print("Digite 2 para ver o resultado e sair")
    escolha = int(input("Qual sua escolha?"))

print(jogador1)
print("A soma do jogador 1 é:", sum(jogador1))
time.sleep(3)
print(jogador2)
print("A soma do jogador 2 é:", sum(jogador2))

j1 = sum(jogador1)
j2 = sum(jogador2)

if j1>j2:
    print("O jogador 1 venceu!!!")
else:
    print("O jogador 2 venceu!!!")

