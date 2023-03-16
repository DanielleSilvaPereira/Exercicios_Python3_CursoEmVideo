'''Faça um programa que mostre a tabuada de vários números, um de cada vez,
 para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''

while True:
    number = int(input('Digite um numero para efetivar a tabuada: '))
    if number < 0:
        print('não é possivel executar uma tabuada negativa')
        break
    for loop in range(1,11):
        print(f'{number} * {loop} = {number * loop}')

