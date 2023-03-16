'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
 para vencer.'''
import random
NumberComputer = random.randint(0, 10)
print (NumberComputer)
print('=================Jogo  de  adivinhar=================')
NumberUser = int(input('Digite um numero de 0 a 10: '))
while NumberUser is not NumberComputer:
    print('Tente de novo! ')
    NumberUser = int(input('Digite um numero de 0 a 10: '))
print(f'Você adivinhou! era o numero {NumberUser}, parabéns s2')
