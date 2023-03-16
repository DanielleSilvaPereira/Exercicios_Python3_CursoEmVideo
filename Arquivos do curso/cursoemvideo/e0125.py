'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
import random
print('Tele tele tele-sena! eu vou... ganhar!!! tele-senaaaa B)')
jogador = int(input('Quantos palpites você deseja criar para a tele-sena? '))

telesena = []
rodada = list()
tot = 1
cont = 0
while tot <= jogador:
    cont = 0
    while True:
        numero = random.randint(0,60)
        if numero not in rodada:
            rodada.append(numero)
            cont += 1
        if cont >= 6:
            break
    telesena.append(rodada[:])
    rodada.clear()
    tot += 1

for indice, lista in enumerate(telesena):
    print(f'{indice+1} Jogo: {lista}')

