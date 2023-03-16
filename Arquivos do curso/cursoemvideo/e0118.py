'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras
que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

num = []

while True:
    number = int(input('Digite um número: '))
    ask = str(input('Deseja continuar? [S/N]: '))
    num.append(number)
    if ask in 'Nn':
        break

print(f'A lista dos valores digitados é {num}')

numpar = []
numimpar = []

for numpars, num in enumerate(num):
    if num % 2 == 0:
        numpar.append(num)
    else:
        numimpar.append(num)


print(f'A lista de números pares é {numpar}')
print(f'A lista de números impares é {numimpar}')
