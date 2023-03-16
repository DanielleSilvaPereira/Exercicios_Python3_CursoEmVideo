'''Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.'''
pares = []
impares = []
lista = []

for laso in range(0, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        pares.append(numero)
    if numero % 2 == 1:
        impares.append(numero)

lista.append(pares[:])
lista.append(impares[:])

print(lista)
print(f'Os números pares em ordem crescente: {sorted(lista[0])}')
print(f'Os números impares em ordem crescente: {sorted(lista[1])}')