'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta. No final, mostre um boletim contendo
a média de cada um e permita que o usuário
possa mostrar as notas de cada aluno individualmente.'''

lista = list()
while True:
    nome = str(input('Digite o nome do alune: '))
    nota1 = float(input('Digite a 1º nota: '))
    nota2 = float(input('Digite a 2º nota: '))
    media = (nota1+nota2)/2
    lista.append([nome, [nota1,nota2], media])
    continuar = str(input('Deseja continuar? [S/N]: '))
    if continuar in 'Nn':
        break

print('-------------BOLETIM-------------')
print(f'{"Número":<7} {"Nome":<12} {"Média":<10}')
for indice, alunos in enumerate(lista):
    print(f'{indice:<7} {alunos[0]:<12} {alunos[2]:<10}')
while True:
    resp = int(input('Deseja ver as notas de quaL aluno? Se a resposta for nenhum, digite 999: '))
    if resp == 999:
        break
    if resp <= len(lista)-1:
         print(f'As notas de {lista[resp][0]} são {lista[resp][1]}')
