'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros'''
PreçoDoProduto = float(input('Qual é o preço do produto: '))
CondicaoDePagamento = int(input('Escolha o metodo de pagamento: \n[1] Á vista \n[2] Á vista no cartão \n[3] Em até 2x do cartão \n[4] 3x ou mais vezes no cartão \n '))
if CondicaoDePagamento == 1:
    Real = PreçoDoProduto - (PreçoDoProduto * 10/100)
    print (f'o preço final é {Real}')
elif CondicaoDePagamento == 2:
    Real = PreçoDoProduto - (PreçoDoProduto * 5/100)
    print(f'O preço final é {Real}')
elif CondicaoDePagamento == 3:
    print(f'O preço final é {PreçoDoProduto}')
elif CondicaoDePagamento == 4:
    Real = PreçoDoProduto + (PreçoDoProduto * 20/100)
    print(f'O preço final é {Real}')
