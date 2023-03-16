'''Descobrir se a frase é um palindromo'''
f = str(input('Digite uma frase: ')).strip().upper()
j = f.strip()
g = ''.join(j)
s = g[::-1]
if s == j:
    print('A frase é um palindromo')
else:
    print('A frase não é um palindromo')