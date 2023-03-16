"""Um programa que leia o comprimento de 3 retas e diga se elas podem formar um triangulo ou não"""
print('Vamos tentar fazer um triangulo!')
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r2 - r3 < r1 < r2 + r3 and r1 - r3 < r2 < r1 + r3 and r1 + r2 < r3 < r1 + r2:
    print('Parabens voce formou um triangulo!')
else:
    print('Voce não conseguiu formar um triangulo, tente novamente!')