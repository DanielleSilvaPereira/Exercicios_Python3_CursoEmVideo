''': Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
import random
print('Eba jogo de adivinha :)')
palpites = 1
num = int(input('Chute um numero de 1 a 10: '))
certo = random.randint(1, 10)
while num != certo:
    num = int(input('Tente de novo: '))
    palpites += 1
print('Eba você adivinhou')
print('Você tentou {} vezes'.format(palpites))