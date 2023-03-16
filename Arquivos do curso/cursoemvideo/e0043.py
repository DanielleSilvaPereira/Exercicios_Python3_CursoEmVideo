'''Um programa que veja se as retas conseguem formar um triangulo e se a resposta for sim, ver qual triangulo forma'''
print('Vamos brincar de formatar triangulos!')
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digiite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 + r2 > r3 and r3 + r2 > r1 and r3 + r1 > r2:
    print('Parabens é possivel formar um triangulo!')
    if r1 == r2 or r2 == r3 or r3 == r1:
        print('O triangulo formado é isosceles')
    elif r2 != r1 != r3 and r1 != r3:
        print('O triangulo formado é escaleno')
    elif r1 == r2 == r3:
        print('O triangulo formado é equilátero')
else:
    print('Que pessimo! não formou um triangulo')
