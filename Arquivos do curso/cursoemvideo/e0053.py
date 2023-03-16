'''Digite um numero e veja se ele é primo ou não'''
n = int(input('Digite um numero inteiro: '))
t = 0
for c in range(1, n+1):
    if n % c == 0:
        print(c, end=' ')
        t += 1
if t == 2:
 print('O numero é primo')
