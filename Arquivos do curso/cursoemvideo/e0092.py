'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
 Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
Gender = input(str('Digite o seu gênero [M/F]: '))
while Gender not in 'MmfF':
    Gender = input(str('Digite o seu gênero [M/F]: '))


