'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''

dados = {}

for laço in range(0,1):
    dados['nome'] = str(input("Digite o nome do alune: "))
    dados['media'] = float(input("Digite a média do alune: "))
    if dados['media'] < 5:
        dados['situação escolar'] = 'reprovado'
    else:
        dados['situação escolar'] = 'aprovado'

print(dados)