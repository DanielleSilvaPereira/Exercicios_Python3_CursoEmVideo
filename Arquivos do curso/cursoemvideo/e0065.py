'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''
cont = 0
som = 0
num = 0
num = int(input('Digite um numero: '))
while num != 999:
    num = int(input('Digite um numero: '))
    cont += 1
    som += num
print('Foram digitados {} numeros'.format(cont))
print('A soma entre os valores digitados é {}'.format(som-999))