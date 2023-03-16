'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoa,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
lista = []
listagem = []
maiorpeso = menorpeso = 0
while True:
    lista.append(str(input('Digite o nome da pessoa: ')))
    lista.append(float(input('Digite o peso da pessoa: ')))
    continua = str(input('Deseja continuar? [S/N]: '))
    if len(lista) == 0:
        maiorpeso = menorpeso = lista[1]
    if lista[1] > maiorpeso:
        maiorpeso = lista[1]
    if lista[1] < menorpeso:
        menorpeso = lista[1]
    listagem.append(lista[:])
    lista.clear()
    if continua in 'Nn':
        break

print(f'Foram {len(listagem)} pessoas cadastradas. ')
print(f'O maior peso foi {maiorpeso}, de: ', end='')
for p in listagem:
    if p[1] == maiorpeso:
        print(f'{p[0]}')

print(f'O menor peso foi {maiorpeso}, de: ', end='')
for p in listagem:
    if p[1] == menorpeso:
        print(f'{p[0]}')

