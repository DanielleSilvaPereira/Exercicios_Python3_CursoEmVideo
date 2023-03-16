''' Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
NumeroEscolhido = int(input('Digite um numero: '))
'''for NumeroPrimo in range (1):
    Condicao1 = NumeroEscolhido % 2
    Condicao2 = NumeroEscolhido % 3
    Condicao3 = NumeroEscolhido % 5
    if Condicao3 and Condicao2 and Condicao1 != 0:
        print('O numero é primo')
    else:
        print('O numero não é primo')'''
soma = 0

for x in range (1,NumeroEscolhido + 1):
    Divisao = NumeroEscolhido % x
    if Divisao == 0:
        soma = soma + 1
soma = soma
if NumeroEscolhido == 1:
    print('O numero é primo')
elif soma == 2:
    print('o numero é primo')
else:
    print('o numero não é primo')
