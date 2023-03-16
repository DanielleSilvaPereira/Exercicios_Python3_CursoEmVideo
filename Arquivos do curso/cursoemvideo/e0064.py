'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.'''
num = int(input('Digite um numero: '))
cont = 3
t1 = 0
t2 = 1
print(' {} {}'.format(t1, t2), end = ' ')
while cont <= num:
    t3 = t1 + t2
    cont += 1
    t1 = t2
    t2 = t3
    print (' {}'.format(t3), end = ' ')

