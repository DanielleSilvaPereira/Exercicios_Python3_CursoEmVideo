import math
a = float(input('Digite o valor do angulo: '))
r = math.radians(a)
print('O cosseno do angulo é {:.2f}\nO seno do angulo é {:.2f}\nA tangente do angulo é {:.2f}'.format(math.cos(r), math.sin(r), math.tan(r)))
