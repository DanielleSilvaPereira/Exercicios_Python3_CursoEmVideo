'''Um programa que leia a data do computador e diga se ele deve se alistar ou não, e se estiver atrasado quanto tempo'''
import datetime
hoje = datetime.date.today().year
sexo = int(input('Digite:\n 1 - se for mulher\n 2 - se for homem: '))
ano = int(input('Em que ano voce nasceu?: '))
idade = hoje - ano
if sexo == 1:
    print('Mulheres não são obrigadas a se alistarem!')
elif idade < 18:
    resto = 18 - idade
    print('Voce não precisa se alistar ainda! Ainda restam {} anos'.format(resto))
elif idade == 18:
    print('Esta na hora de se alistar!')
elif idade > 18:
    resto2 = idade - 18
    print('Voce já deveria ter se alistado há {} anos'.format(resto2))