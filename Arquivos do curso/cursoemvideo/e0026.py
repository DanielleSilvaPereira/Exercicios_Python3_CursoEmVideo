""": Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”."""
n = str(input('Digite o nome de sua cidade: ')).strip()
separa = n.split()
print(n[:5].upper() == 'SANTO')

