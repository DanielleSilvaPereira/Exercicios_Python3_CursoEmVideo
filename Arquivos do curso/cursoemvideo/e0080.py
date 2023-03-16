'''Crie um programa que faça o computador jogar Jokenpô com você.'''
import random
Jogador = int(input('Escolha:\n[1] Tesoura\n[2] Pedra\n[3] Papel\n'))
Computador = random.randint(1,3)
if Computador == 1:
    if Jogador == 1:
        print('Empate')
    elif Jogador == 2:
        print('Ganhou')
    elif Jogador == 3:
        print('Perdeu')
elif Computador == 2:
    if Jogador == 1:
        print('Perdeu')
    elif Jogador == 2:
        print('Empate')
    elif Jogador == 3:
        print('Ganhou')
elif Computador == 3:
    if Jogador == 1:
        print('Ganhou')
    elif Jogador == 2:
        print('Perdeu')
    elif Jogador == 3:
        print('Empate')
