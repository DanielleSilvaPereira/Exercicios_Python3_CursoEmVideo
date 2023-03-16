'''Calcular a média do aluno e dizer se ele passou ou não'''
primeira = float(input('Digite a primeira nota do aluno: '))
segunda = float(input('Digite a segunda nota do aluno: '))
terceira = float(input('Digite a terceira nota do aluno: '))
media = (primeira+segunda+terceira)/3
if media == 7 or media > 7:
    print('Parabéns você passou de ano!')
elif 5 < media < 7:
    print('Você está de recuperação, estude mais na proxima vez.')
elif media < 5:
    print('Que pena! Você repetiu de ano.')
