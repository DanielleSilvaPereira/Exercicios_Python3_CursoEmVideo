'''Ver quais são as casas numericas de um numero de 0 a 9999'''
n = str(input('Digite um numero de 0 a 9999: '))
u = n[0]
d = n[1]
c = n[2]
m = n[3]
print('o numero em questão pode ser dividido da seguinte forma:\n{} unidades\n{} dezenas\n{} centenas\n{} milhares'.format(u, d, c, m))