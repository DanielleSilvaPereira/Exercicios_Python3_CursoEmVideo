''' Dizer se o numero é par ou não '''
n = int(input('Digite um numero inteiro: '))
r = n % 2
if r == 0:
    print('O numero que voce digitou é par')
else:
    print('O numero que voce digitou é impar')