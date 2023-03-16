'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
 e o programa vai informar quantas cédulas de cada valor serão entregues.
  OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('Caixa Eletrônico')
print('-' * 30)
moneyneed = int(input('Digite o valor que deseja sacar (inteiro): R$:'))

fifty = moneyneed // 50
twelve = moneyneed // 20
ten = moneyneed // 10
one = moneyneed // 1

if fifty >= 1:
    print(f'{fifty} notas de R$50.00')
    fifty *= 50
    moneyneed -= fifty

twelve = moneyneed // 20
ten = moneyneed // 10
one = moneyneed // 1

if twelve >= 1:
    print(f'{twelve} notas de R$20.00')
    twelve *= 20
    moneyneed -= twelve

ten = moneyneed // 10
one = moneyneed // 1

if ten >= 1:
    print(f'{ten} notas de R$10.00')
    ten *= 10
    moneyneed -= ten

one = moneyneed // 1

if one >= 1:
    print(f'{one} notas de R$1.00')
    one *= 1
