'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
import datetime
somamaioridade = 0
somaminoridade = 0
Hoje = datetime.date.today().year

for laço in range (1,8):
    nascimento = int(input(f'Digite a data de nascimento da {laço}º pessoa:   '))
    idade = Hoje - nascimento
    if idade >= 18:
        somamaioridade = somamaioridade + 1
    else:
        somaminoridade = somaminoridade + 1
print(f'{somaminoridade} são menores de idades\n{somamaioridade} são maiores de idade')
