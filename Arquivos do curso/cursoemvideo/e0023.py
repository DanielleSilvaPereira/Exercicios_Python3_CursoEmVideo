'''Formatando o nome de alguem e indicando a quantidade de letras'''
n = str(input('Digite seu nome completo: ')).strip()
upper = n.upper()
lower = n.lower()
print('Formatando o seu nome!\n{} \n{} \n{} letras\n'.format(upper, lower, len(n) - n.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(n.find(' ')))
n = n.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(n[0], len(n[0])))
