'''Crie um programa que leia dois valores e mostre um menu na tela:'''
'''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

NumberChoice1 = int(input('Digite o primeiro número: '))
NumberChoice2 = int(input('Digite o segundo numero: '))
Option = 0
while Option != 5:
    Option = int(input('Escolha a operação: \n[1] soma \n[2]multiplicar \n[3]maior \n[4]novos números \n[5] sair do programa: '))
    if Option == 1:
        print(f'A soma entre os numeros é {NumberChoice2 + NumberChoice1}')
    elif Option == 2:
        print(f'O produto dos numeros é {NumberChoice2 * NumberChoice1}')
    elif Option == 3:
        if NumberChoice1 > NumberChoice2:
            print(f'O maior número é {NumberChoice1}')
        else:
            print(f'O maior numero é {NumberChoice2}')
    elif Option == 4:
        NumberChoice1 = int(input('Digite o primeiro número: '))
        NumberChoice2 = int(input('Digite o segundo numero: '))
    elif Option == 5:
        break

