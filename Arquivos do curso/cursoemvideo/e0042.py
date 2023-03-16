'''Um programa que leia a idade da pessoa e diga se ela esta em mirim, infantil, junior, senior ou master'''
import datetime
print('Bem-vinde a natação do CEU Vila Rubi')
ano = datetime.date.today().year
idade = int(input('Digite o ano do seu nascimento: '))
id = ano - idade
if id <= 9:
    print('Voce esta classificado na categoria MIRIM')
elif 9 <= id < 14:
    print('Voce esta classificado na categoria INFANTIL')
elif 14<= id < 19:
    print('Voce esta classificado na categoria JUNIOR')
elif 19 <= id < 25:
    print('Voce esta classificado na categoria SENIOR')
else:
    print('Voce esta classificado na categoria MASTER')