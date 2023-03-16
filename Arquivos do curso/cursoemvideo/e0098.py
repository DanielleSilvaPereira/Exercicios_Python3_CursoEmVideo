'''Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer
e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
0 – 1 – 1 – 2 – 3 – 5 – 8'''
fibbo = 0
first = 0
second = 1
third = 0
number = int(input("Input a number here: "))
cont = number
print('{}, {},'.format(first, second), end='')
while cont != 0:
    third = first + second
    print(' {},'.format(third), end='')
    first = second
    second = third
    cont -= 1

