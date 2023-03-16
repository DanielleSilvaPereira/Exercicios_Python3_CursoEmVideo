'''Um programa que compare 2 numeros inteiros e diga se o primeiro ou o segundo valor são maiores, ou se são iguais'''
print('Descubra qual numero é maior!')
primeiro = float(input('Digite o primeiro numero: '))
segundo = float(input('Digite o segundo numero: '))
if primeiro > segundo:
    print('O numero {} é o maior'.format(primeiro))
elif segundo > primeiro:
    print('O numero {} é o maior'.format(segundo))
elif primeiro == segundo:
    print('Os dois valores são iguais')
