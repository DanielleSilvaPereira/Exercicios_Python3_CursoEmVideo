'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

values = []
min = 0
maxi = 0
for l in range(0,5):
    v = int(input(f'Input the {l+1} number: '))
    if l == 0 or v > values[-1]:
        values.append(v)
    else:
        pos = 0
        while pos < len(values):
            if v <= values[pos]:
                values.insert(pos, v)
            break
            pos += 1



print(values)
