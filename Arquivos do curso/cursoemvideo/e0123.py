'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
soma2 = 0

for coluna in range(0,3):
    for linha in range(0,3):
        matriz[coluna][linha] = int(input(f'Digite um valor para a matriz [{linha}x{coluna}]: '))
        if matriz[coluna][linha] % 2 == 0:
            soma += matriz[coluna][linha]
        if matriz[2][linha]:
            soma2 += matriz[2][linha]

for printer in range(0,3):
    print(matriz[printer])

print(f'A soma de todos os valores pares digitados é {soma}')
print(f'A soma dos valores da terceira coluna é {soma2}')
print(f'O valor máximo da segunda linha foi {max(matriz[1])}')





