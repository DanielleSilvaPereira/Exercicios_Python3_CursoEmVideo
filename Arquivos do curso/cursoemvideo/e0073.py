'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais'''
Primeirovalor = int(input('Digite um numero: '))
Segundovalor = int(input('Digite outro numero: '))
if Primeirovalor == Segundovalor:
    print('Os dois valores são iguais')
elif Primeirovalor > Segundovalor:
    print('O primeiro valor é maior')
elif Segundovalor > Primeirovalor:
    print('O segundo valor é maior')