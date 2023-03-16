'''Um programa que calcule o preço do produto de acordo com a condição de pagamento'''
print('Bom dia, bem vindo ao Magalu!')
preço = float(input('Digite o valor da mercadoria: '))
condiçao = int(input('Digite a condição de pagamento ( a vista em dinheiro = 1, a vista no cartão = 2, até 2x no cartão = 3 e 3x ou mais no cartão = 4: '))
if condiçao == 1:
    p = preço - (preço*10/100)
    print(' O valor a ser pago é R${}'.format(p))
elif condiçao == 2:
    po = preço - (preço*5/100)
    print('O valor a ser pago é R${}'.format(po))
elif condição == 3:
    print('O valor a ser pago é R${}'.format(preço))
elif condição == 4:
    por = preço + (preço*20/100)
    print('O valor a ser pago é R$:{}'.format(por))