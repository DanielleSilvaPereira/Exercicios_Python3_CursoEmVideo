'''Leia o peso de 5 pessoas e diga qual foi o maior e qual foi o menor'''
'''ist = []
for c in range(1,6):
    f = float(input('Digite o peso da pessoa em KG: '))
    ist += [f]
print('O maior peso foi {}\nO menor peso foi {}'.format(max(ist), min(ist)))'''
maior = 0
menor = 0
for c in range (1,6):
    p = float(input('Qual é o peso da {} pessoa: '.format(c)))
    if c == 1:
        maior = c
        menor = c
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('O maior peso foi {} e o menor foi {}'.format(maior, menor))