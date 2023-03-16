'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

values = []

for link in range(0,5):
    values.append(int(input('Input a number here: ')))

print(values)

print(f'The bigger value in the list is >{max(values)}< in the position {values.index(max(values))+1}')

print(f'The smallest value in the list is >{min(values)}< in the position {values.index(min(values))+1}')
