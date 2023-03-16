'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
 Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

expressao = []

expressao = input('Digite sua expressão numérica: ')
colchetesesquerda = expressao.count('(')
colchetesdireita = expressao.count(')')
print(f'Sua expressão numérica é {expressao}')
print(f'A quantidade de colchetes ( é {colchetesesquerda} e a quantidade de colchetes ) é {colchetesdireita}')
if colchetesdireita == colchetesesquerda:
    print('A expressão numérica está certa')
else:
    print('A expressão númerica está errada')
