'''Um programa que leia um ano e diga se o ano é bissexto ou não'''
ano = int(input('Digite o ano: '))
if ano % 400 == 0:
    print('É ano bissexto.')
else:
    print('Não é um ano bissexto.')