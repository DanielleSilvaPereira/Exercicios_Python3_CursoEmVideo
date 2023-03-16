'''Computador que joga par ou impar e mostra as vitorias consecutivas quando o jogador perder'''
import random
computador = random.randint(1,11)
soma = 0
cont = 0
print('Vamos jogar par ou impar!')
while True:
    Numero = int(input('Escolha um numero: '))
    Opcao = str(input('Escolha entre Par ou Impar [P/I]: ')).strip().upper()
    soma = computador + Numero
    soma % 2
    if Opcao == 'P':
        if soma == 1:
            break
    cont += 1
    if Opcao == 'I':
        if soma == 0:
            break
    cont += 1
print('--'*20)
print('Voce perdeu')
print(f'Voce ganhou {cont} vezes')

