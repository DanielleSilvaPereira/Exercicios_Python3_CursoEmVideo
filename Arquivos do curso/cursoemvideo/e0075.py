'''Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''
PrimeiraNota = float(input('Digite a primeira nota do aluno: '))
SegundaNota = float(input('Digite a segunda nota do aluno: '))
TerceiraNota = float (input('Digite a terceira nota do aluno: '))
Media = (PrimeiraNota + SegundaNota + TerceiraNota)/3
if 7 > Media >= 5:
    print('O aluno esta de recuperação')
elif Media >= 7:
    print('O aluno esta aprovado')
elif Media < 5:
    print('O aluno esta reprovado')