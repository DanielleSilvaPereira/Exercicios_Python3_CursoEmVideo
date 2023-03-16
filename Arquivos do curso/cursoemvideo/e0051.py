'''LEIA 6 NUMEROS INTEIROS E MOSTRE APENAS OS PARES'''
x = 0
y = 0
for c in range(1,7):
    b = int(input('Digite um numero: '))
    if b % 2 == 0:
     x = x + b
print('A soma entre os numeros pares é equivalente a {}'.format(x))
