'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''
Primeirolado = float(input('Digite o primeiro lado do triangulo: '))
Segundolado = float(input('Digite o segundo lado do triangulo: '))
Terceirolado = float(input('Digite o terceiro lado do triangulo: '))
if Primeirolado == Segundolado == Terceirolado:
    print('O seu triangulo é equilátero')
elif Primeirolado == Segundolado != Terceirolado or Terceirolado == Primeirolado != Segundolado or Segundolado == Terceirolado != Primeirolado:
    print('o seu triangulo é isosceles')
elif Primeirolado != Segundolado != Terceirolado:
    print('O seu triangulo é escaleno')

