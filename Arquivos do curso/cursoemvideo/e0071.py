" Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado."
print('Configurações para aprovar o seu emprestimo bancário: ')
casa = int(input('Digite o valor da casa: '))
salario = int(input('Digite o valor do salario: '))
tempo = int(input('Digite em quantos anos a casa deverá ser paga: '))
if casa/(tempo*12) < salario*30/100:
    print("Voce pode efetuar o emprestimo")
else:
    print("Voce não pode efetuar o emprestimo")