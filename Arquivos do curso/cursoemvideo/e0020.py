import math
import random
print('SORTEIO DE CELULAR!!')
a = input('Digite o nome do primeiro participante: ')
b = input('Digite o nome do segundo participante: ')
c = input('Digite o nome do terceiro participante: ')
d = input('Digite o nome do quarto participante: ')
lista = [a, b, c, d]
print('SORTEIO REALIZADO! NÃO FIQUE TRISTE SE NÃO FOI PREMIADO, AGRADECEMOS SUA PARTICIPAÇÃO E TE DESEJAMOS BOA SORTE NOS PRÓXIMOS SORTEIOS')
print('O GANHADOR FOI {}. PARABENS PARA ELE!!!!'.format(random.choice(lista)))
