'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''
primeiro = int(input('Digite o primeiro termo da p.a: '))
razao = int(input('Digite a razão da p.a: '))
cont = 1
tot = 0
duvida = 10
termo = primeiro
while duvida != 0:
    tot = tot + duvida
    while cont <= tot:
        print('{}'.format(termo), end=' ')
        termo += razao
        cont += 1
    duvida = int(input('Deseja adicionar mais termos? Se sim quantos: '))

