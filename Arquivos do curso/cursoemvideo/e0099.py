'''Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
 O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
 No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

number = int(input('input a number here, if you want to stop input 999: '))
soma = 0
cont = 0
while number != 999:
    soma += number
    cont += 1
    number = int(input('input a number here, if you want to stop input 999: '))

print(f"{soma} is the sum of the numbers that you input")
print(f"{cont} is the count of the number that you input")
