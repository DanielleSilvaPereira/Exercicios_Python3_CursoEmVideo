'''Jogo de adivinhar'''
import random
print('Vamos brincar de adivinha!')
n = int(input('Digite um numero de 1 a 5: '))
if n == random.randint(1, 5):
    print('Parabéns você ganhou o jogo de adivinha!')
else:
    print('Tente novamente!')