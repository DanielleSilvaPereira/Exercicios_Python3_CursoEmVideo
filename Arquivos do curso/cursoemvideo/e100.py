'''Crie um programa que leia vários números inteiros pelo teclado.
 No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
import statistics

number = int(input('Input a number here: '))
continu = str(input('Do you want to continue? [Y/N]: ')).upper()
sum = number
cont = 1
bigvalue = number
smallvalue = number
average = 0

while continu not in 'Nn':
    number = int(input('Input a number here: '))
    continu = str(input('Do you want to continue? [Y/N]: '))
    sum += number
    cont += 1
    if number > bigvalue:
       bigvalue = number
    if number < smallvalue:
        smallvalue = number

average = sum / cont

print(f'{average} is the mean of the number that you input')
print(f'{bigvalue} is the biggest number here')
print(f'{smallvalue} is the smallest number here')
