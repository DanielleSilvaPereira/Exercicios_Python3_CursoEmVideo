'''Ler o valor da casa, salário e a quantidade de anos que será pago, dizendo se poderá pagar ou não sabendo que não pode exercer
30% do salário as parcelas'''
casa = float(input('Digite o valor da casa/apartamento: '))
salario = float(input('Digite o valor do seu salario mensal: '))
tempo = int(input('Digite em quantos anos voce deseja parcelar a casa: '))
valor = casa / (tempo*12)
if valor > salario-(salario*30/100):
    print('Me desculpe, mas voce não tem condições financeiras para financiar a casa')
else:
    print('O valor das parcelas do financiamento sairão por R$:{:.2f}'.format(valor))