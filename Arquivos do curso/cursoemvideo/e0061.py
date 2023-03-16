'''Faça um programa que leia um número qualquer e mostre o seu fatorial. '''
numero = int(input('Digite um numero para saber seu fatorial: '))
fator = 1
c = numero
while c > 0:
    print('{}'.format(c), end='')
    print(' x' if c > 1 else '=', end=' ')
    fator *= c
    c -= 1
print(fator)