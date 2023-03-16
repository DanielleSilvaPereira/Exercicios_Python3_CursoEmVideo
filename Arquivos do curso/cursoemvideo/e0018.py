import math
print('Vamos calcular a hipotenusa de um triangulo retangulo agora!')
ca = float(input('Digite o valor do cateto adjacente do triangulo: '))
co = float(input('Digite o valor do cateto oposto do triangulo: '))
'''ca2 = math.pow(ca, 2)
co2 = math.pow(co, 2)
print('A hipotenusa é {:.1f}'.format(math.sqrt(ca2 + co2)))'''
print('A hipotenusa é {:.2f}'.format(math.hypot(ca, co)))

