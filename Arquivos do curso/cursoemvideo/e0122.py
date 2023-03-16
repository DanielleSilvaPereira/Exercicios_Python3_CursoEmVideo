'''Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''

matrix = [[], [], []]

for primeiralinha in range(0,3):
    numero = int(input(f'Digite o número {primeiralinha+1}x1: '))
    matrix[0].append(numero)

for segundalinha in range(0,3):
    numero2 = int(input(f'Digite o número {segundalinha+1}x2: '))
    matrix[1].append(numero2)

for terceiralinha in range(0, 3):
    numero3 = int(input(f'Digite o número {terceiralinha+1}x3: '))
    matrix[2].append(numero3)

print(matrix[0])
print(matrix[1])
print(matrix[2])
