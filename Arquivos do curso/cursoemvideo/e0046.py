'''Jokenpo'''
import random
from time import sleep
print('Brinca comigo de jokenpo????')
opçoes = ('Pedra', 'Papel', 'Tesoura')
eu = int(input('0 - Pedra\n1 - Papel\n2 - Tesoura\nEscolha uma das opções: '))
vc = (opçoes[eu])
pc = random.randint(0, 2)
cpu = (opçoes[pc])
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-'*20)
if pc == 0:
    if eu == 0:
        print('EMPATE')
    elif eu == 1:
        print('VITORIA')
    elif eu == 2:
        print('DERROTA')
elif pc == 1:
    if eu == 0:
        print('DERROTA')
    elif eu == 1:
        print('EMPATE')
    elif eu == 2:
        print('VITORIA')
elif pc == 2:
    if eu == 0:
        print('VITORIA')
    if eu == 1:
        print('DERROTA')
    if eu == 2:
        print('EMPATE')
print('-'*20)
print('Voce jogou {}'.format(vc))
print('O computador jogou {}'.format(cpu))

