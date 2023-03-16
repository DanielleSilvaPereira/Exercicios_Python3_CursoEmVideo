'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''
import datetime
Hoje = datetime.date.today().year
Nascimento = int(input('Digite o ano de nascimento do atleta: '))
Idade = Hoje - Nascimento
if Idade <= 9:
    print('Categoria mirim')
elif Idade <= 14:
    print('Categoria infantil')
elif Idade <= 19:
    print('Categoria junior')
elif Idade <= 25:
    print('Categoria senior')
elif Idade > 25:
    print('Categoria master')