'''Programa que leia varios valores e tenha como flag 999, no final mostre a soma e quantos numeros foram digitados'''
cont = 0
soma = 0
while True:
    numero = int(input('Digite um numero: '))
    if numero == 999:
        break
    cont += 1
    soma += numero
print(f'A quantidade de valores somados é {cont} e a soma entre eles é {soma}')

