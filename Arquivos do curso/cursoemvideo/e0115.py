'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
 Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
  em ordem crescente.'''

values = []


while True:
    v = int(input('Input a number here: '))
    if v  not in values:
        values.append(v)
    else:
        print('Você já inseriu esse número')
    a = str(input('Do you want to continue? [S] ou [N]:' ))
    if a in 'Nn':
        break

print(sorted(values))

