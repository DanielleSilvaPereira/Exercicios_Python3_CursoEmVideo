'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
sexo = input(str('Digite o seu genero: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = input(str('Digite o seu genero: ')).upper().strip()
print('Sexo {} validado com sucesso'.format(sexo))
