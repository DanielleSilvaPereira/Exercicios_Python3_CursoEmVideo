'''Crie um programa que leia números inteiros pelo teclado.
 O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''

number = int(input('Input a number(999 for stop): '))
cont = 0
summ = number
while number != 999:
    number = int(input('Input a number(999 for stop): '))
    cont += 1
    if number == 999:
        break
    summ += number
print(f'Voce digitou {cont} numeros')
print(f'A soma dos numeros que voce digitou é {summ}')
