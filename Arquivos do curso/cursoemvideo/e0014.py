n = int(input('Digite o preço do produto: '))
a = n*10/100
b = n*15/100
print('O valor do produto á vista, fica com 10% de desconto, equivalente a {}.\nO valor parcelado recebe 15% de acrescimo somando em {}.'.format(n-a, n+b))
