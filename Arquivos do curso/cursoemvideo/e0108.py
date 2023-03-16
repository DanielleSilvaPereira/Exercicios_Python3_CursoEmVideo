'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
de zero até vinte.
 Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

number = ('zero', 'um','dois','três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze'
          , 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numberuser = int(input('Digite um numero de 0 a 20 para vê-lo em extenso: '))

print(f'{numberuser} em extenso é {number[numberuser]}')