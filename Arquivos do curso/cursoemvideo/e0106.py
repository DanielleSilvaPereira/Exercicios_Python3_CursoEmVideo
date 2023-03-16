'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''
from math import inf
summ = 0
contprice = 0
smallvalue = inf
nameofsmallproduct = ''

while True:
    cont =+ 1
    product = str(input(f'Digite o nome do {cont} produto: '))
    price = float(input(f'Digite o preço do {cont} produto: R$'))
    ask = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    summ += price

    if price >= 1000:
        contprice += 1

    if price < smallvalue:
        smallvalue = price
        nameofsmallproduct = product

    if ask not in 'Ss':
        break

print(f'o total dos produtos é {summ}')
print(f'o total de produtos que custam mais de R$ 1000 é {contprice}')
print(f'O produto mais barato é {nameofsmallproduct} que custa R${smallvalue}')