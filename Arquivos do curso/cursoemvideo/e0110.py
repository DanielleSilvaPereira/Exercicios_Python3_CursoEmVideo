'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''
from random import randint

number = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(number)
number = sorted(number)
print(number)
print(f'O menor numero é {number[0]}')
print(f'O maior numero é {number[4]}')