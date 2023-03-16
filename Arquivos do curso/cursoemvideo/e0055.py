'''Leia a idade de 7 pessoas e diga qual alcançou a maioridade'''
import datetime
hoje = datetime.date.today().year
tot = 0
tota = 0
for c in range(1,8):
    ano = int(input('Digite o ano de nascimento do individuo {}: '.format(c)))
    idade = hoje - ano
    if idade >= 18:
        tot = tot + 1
    else:
        tota = tota + 1
print('{} Chegaram a maioridade e {} ainda não chegaram lá'.format(tot, tota))