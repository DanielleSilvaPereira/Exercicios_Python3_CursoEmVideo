'''sorteio da ordem de apresentação '''
from random import shuffle
print('Sorteio da ordem de apresentação do tcc do dricas')
a = input('Digite o primeiro grupo: ')
b = input('Digite o segundo grupo: ')
c = input('Digite o terceiro grupo: ')
d = input('Digite o quarto grupo: ')
l = [a, b, c, d]
r = shuffle(l)
print('A ordem de apresentação será')
print(l)