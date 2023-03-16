'''Um programa que leia 3 numeros e diga qual é o menor e qual é o maior'''
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor numero da sequencia é {} e o maior é {}'.format(menor, maior))
