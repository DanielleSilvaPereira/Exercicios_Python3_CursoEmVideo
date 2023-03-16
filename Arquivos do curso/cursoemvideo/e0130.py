'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
import datetime

#adicionando o input dos dados do usuário
dicionario = dict()
dicionario['nome'] = str(input('Digite o seu nome: '))
dicionario['nascimento'] = int(input('Digite o ano de seu nascimento: '))
dicionario['trabalho'] = int(input('Digite o número da sua carteira de trabalho, se não houver digite 0: '))

#calculando a idade
dicionario['idade'] = datetime.date.today().year - dicionario['nascimento']

#checando se a carteira de trabalho existe para prosseguir e calculando a aposentadoria
if dicionario['trabalho'] != 0:
    dicionario['contratacao'] = int(input('Digite o ano da contratação: '))
    dicionario['salario'] = int(input('Digite o valor do seu salário: '))
    dicionario['aposentadoria'] = dicionario['idade'] + (25 - (datetime.date.today().year - dicionario['contratacao']))

#resultado
print(f"{dicionario['nome']} não tem carteira de trabalho para apresentar os dados da aposentadoria")
if dicionario['trabalho'] != 0:
    print(f"{dicionario['nome']} com a carteira de trabalho {dicionario['trabalho']} se aposentará com {dicionario['aposentadoria']}")