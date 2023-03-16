'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120'''

'''number = int(input('Input a number here:  '))
fatorial = 1

while number != 0:
    print(number, if number != 0 end = '! ')
    number -= 1
    number *= fatorial'''


import math
number = int(input('Input a number here: '))
fatorial = math.factorial(number)
print(f'The fatorial of {number} is {fatorial}')