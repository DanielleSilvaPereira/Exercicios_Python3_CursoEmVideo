'''Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo'''
import random
from random import randint

print('JOGO DO IMPAR E DO PAR')

result = 0
cont = 0

while True:
    user = int(input('Digite um numero: '))
    computer = random.randint(1,10)
    choice = int(input('1 para impar 2 para par: '))
    result = user + computer
    if choice == 1:
        if result % 2 == 0:
            print('perdeu')
            break
        if result % 2 != 0:
            print('ganhou')
            cont += 1
    if choice == 2:
        if result % 2 == 0:
            print('ganhou')
            cont += 1
        if result % 2 != 0:
            print('perdeu')
            break

print(f'Você ganhou {cont} vezes')
