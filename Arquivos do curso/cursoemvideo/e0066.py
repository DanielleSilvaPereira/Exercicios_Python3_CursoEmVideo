''' Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
cont = 0
soma = 0
lista = []
duvida = 'S'
while duvida != 'N':
    numero = int(input('Digite um numero: '))
    duvida = str(input('Deseja continuar? [S/N]: ').upper().strip())
    lista += [numero]
    cont += 1
    soma += numero
    media = soma / cont
lista += [numero]
print('A média dos numeros digitados é {}'.format(media))
print('O maior numero da lista é {}'.format(max(lista)))
print('O menor numero da lista é {}'.format(min(lista)))
