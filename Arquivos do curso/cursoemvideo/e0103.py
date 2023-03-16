'''Faça um programa que jogue par ou ímpar com o computador.
 O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
import random
print("AAAAAAAEEEE BRINCADEIRAAAAAA PAR OU IMPAAAAAARRRR")
while True:
    user = int(input('Digite um numero: '))
    computer = random.randint(1, 10)
    opcoes = ["par", "impar"]
    result = random.choice(opcoes)
    print(f" o seu numero foi {user} e o do computador foi {computer}")
    print(f"O resultado foi {result}")
    if result == "par":
        if computer % 2 == 0 and user % 2 == 0:
            print("EMPATOU N VALE")
        if computer % 2 == 0 and user % 2 != 0:
            print("PERDEU :/")
            break
        if computer % 2 != 0 and user % 2 == 0:
            print("GANHOU EBA")
    if result == "impar":
        if computer % 2 != 0 and user % 2 != 0:
            print('EMPATOU N VALE')
        if computer % 2 != 0 and user % 2 == 0:
            print('PERDEU :/')
            break
        if computer % 2 == 0 and user != 0:
            print("GANHOU EBA")

