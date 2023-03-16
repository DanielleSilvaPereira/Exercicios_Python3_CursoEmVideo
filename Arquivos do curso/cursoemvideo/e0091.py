'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres
 têm menos de 20 anos.'''
Menoridade = 0
Maioridade = 0
Soma = 0
Nomehomemvelho = str
for laco in range(1,5):
      Nome = str(input('Qual o seu nome: '))
      Idade = int(input('Qual é a sua idade: '))
      Sexo = int(input('Qual é o seu gênero? (1 - fem/ 2 - masc): '))
      Soma += Idade
      if Sexo == 1 and Idade < 20:
            Menoridade = Menoridade + 1
      elif Sexo == 2:
            Homemvelho = Idade
            Nomehomemvelho = Nome
            if Idade > Homemvelho:
                Homemvelho = Idade
                Nomehomemvelho = Nome

print(f'O número de mulheres menores de 20 anos é {Menoridade}')
Media = Soma / laco
print(f'A média de idade do grupo é {Media}')
print(f'O nome do homem mais velho é {Nomehomemvelho}')
