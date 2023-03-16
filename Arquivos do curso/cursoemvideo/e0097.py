'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
 O programa encerrará quando ele disser que quer mostrar 0 termos.'''

primeiro_termo = int(input("Digite o primeiro termo da P.A: "))
razao = int(input("Digite a Razao da P.A: "))
cont = 1
while cont <= 10:
    primeiro_termo += razao
    cont += 1
    print(primeiro_termo)

continua = int(input("Digite a quantidade de termos que voce deseja ver mais:   "))
if continua != 0:
    for x in range (cont, cont <= (cont + continua)):
        primeiro_termo += razao
        cont += 1
        print(primeiro_termo)
        break
else:
    print('Ok')