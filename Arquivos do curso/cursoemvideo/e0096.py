'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
 mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
primeiro_termo = int(input('Digite o primeiro termo da sua progressão aritmética: '))
razao = int(input('Agora digite sua razâo: '))
cont = 1
while cont <= 10:
    primeiro_termo += razao
    cont += 1
    print(primeiro_termo)