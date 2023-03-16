'''Mostre o primeiro e o ultimo nome de alguem'''
n = input(str('Digite seu nome completo: ')).strip().split()
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu ultimo sobrenome é {}'.format(n[len(n)-1]))