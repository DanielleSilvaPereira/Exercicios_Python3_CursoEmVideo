'''Conversor de base numérica'''
print('Conversão de numeros inteiros')
n = int(input('Digite um numero inteiro: '))
b = int(input('\n1 - Para binário\n2 - Para octal\n3 - hexadecimal:'))
if b == 1:
    print('A conversão de {} é igual a {}'.format(n, bin(n)[:2]))
elif b == 2:
    print('A conversão de {} é igual a {}'.format(n, oct(n)[:2]))
elif b == 3:
    print('A conversão de {} é igual a {}'.format(n, hex(n)[:2]))