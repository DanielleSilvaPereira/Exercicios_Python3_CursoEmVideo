'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
termo = int(input('Digite o primeiro termo da p.a: '))
razao = int(input('Digite a razão da p.a: '))
termo2 = termo
c = 1
while c <= 10:
    termo2 += razao
    c += 1
    print('{}'.format(termo2), end=' ')
