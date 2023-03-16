''' Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''
lista = []
for laço in range (1,6):
    peso = int(input(f'Digite o peso da {laço}º pessoa:(kg) '))
    lista += [peso]
print(f'A pessoa mais pesada tem {max(lista)}.kg e a mais leve {min(lista)}.kg')
