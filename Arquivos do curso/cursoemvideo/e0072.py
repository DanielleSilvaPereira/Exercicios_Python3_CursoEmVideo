''' Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''
Numero = int(input("Digite um numero: "))
Seleçao = int(input('Digite para conversão: \n[1] binário [2] octal [3] hexa:  '))
if Seleçao == 1:
    print(f'{bin(Numero)} é a conversão para binário de {Numero}')
elif Seleçao == 2:
    print(f'{oct(Numero)} é a conversão para octal de {Numero}')
elif Seleçao == 3:
    print(f'{hex(Numero)} é a conversão para hexa de {Numero}')
