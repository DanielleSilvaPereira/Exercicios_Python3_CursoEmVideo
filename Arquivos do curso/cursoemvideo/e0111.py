'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''
count = 0
numberuser = (int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')))
print(f'Você digitou os números {numberuser}')
print(f'O número 9 aparece {numberuser.count(9)} vezes')
if 3 in numberuser:
    print(f'O primeiro número 3 aparece em {numberuser.index(3)+1}º')
else:
    print('Não há número 3')
for n in numberuser:
    if n % 2 == 0:
        print(f'o número "{n}" digitado é par.')


