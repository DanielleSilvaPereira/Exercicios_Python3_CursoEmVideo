"""Leia o salario de um funcionario e calcule o seu aumento de 15% e se o salario passar de 1250 são 10%"""
s = float(input('Digite o valor em reais do sálario do colaborador: '))
if s < 1250:
    print('O salário do colaborador acaba de sofrer um aumento de 15%!\nO valor atualizado equivale a R${:.2f}'.format((s*15/100)+s))
else:
    print('O salário do colaborador acaba de receber um aumento de 10%!\nO valor atualizado equivale a R${:.2f}'.format((s*10/100)+s))