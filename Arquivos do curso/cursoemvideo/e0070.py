'''Programa que a idade e o sexo de varias pessoas e diga 1 - maiores de 18 2 - homens 3 - mulheres - 20 anos'''
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o genero da pessoa [M/F] : ')).strip().upper()
    parada = str(input('Digite se deseja parar [S/N] : ')).strip().upper()
        if parada == 'S':
          break
print('sexo')