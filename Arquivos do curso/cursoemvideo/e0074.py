'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
import datetime
AnoDeNasc = int(input('Digite o ano que voce nasceu: '))
Hoje = datetime.date.today().year
if Hoje - AnoDeNasc < 18:
    print('Ainda não precisa se alistar')
elif Hoje - AnoDeNasc > 18:
    print('Já passou da hora de se alistar')
elif Hoje - AnoDeNasc == 18:
    print('Esta na hora de se alistar')
