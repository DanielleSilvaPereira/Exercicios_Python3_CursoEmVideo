'''Numeros impares e multiplos de 3 de 1 a 500'''
soma = 0
for c in range(1, 501, 2):
    if  c % 3 == 0:
          soma = soma + c
print('{} valor da soma entre multiplos de 3 impares entre 1 e 500'.format(soma))
#soma=0
#for k in range(1,501,2):
#	if k%3 == 0:
#		soma = soma + k

#print(f'A soma dos múltiplos de 3 entre 1 e 500 é = {soma}')