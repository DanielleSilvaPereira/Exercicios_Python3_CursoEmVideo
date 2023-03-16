'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
para cada palavra, quais são as suas vogais.'''

words = ('costumer', 'ATM machine', 'cashier', 'currency', 'coin', 'banknote', 'wallet', 'money')

print(words)

for lace in words:
    print(f'\n Em {lace.upper()} existem as vogais', end= ' ')
    for letter in lace:
        if letter.lower() in 'aeou':
            print(letter, end= ' ')
