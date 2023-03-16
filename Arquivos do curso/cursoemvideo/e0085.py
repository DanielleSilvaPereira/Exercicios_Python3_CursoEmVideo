'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''
soma = 0
for numeros in range(1,7):
    numerodigitado = int(input('Digite um numero: '))
    if numerodigitado % 2 == 0:
        soma = numerodigitado + soma
print(f'A soma dos numeros pares é {soma}')
