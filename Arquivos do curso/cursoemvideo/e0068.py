'''Leia um numero e mostre sua tabuada até que o valor seja negativo'''
cont = 0
while True:
    numero = int(input('Digite um numero: '))
    if numero in '-':
        break
    for cont in range (1,11):
        print(f'{numero} * {cont} = {numero*cont}')