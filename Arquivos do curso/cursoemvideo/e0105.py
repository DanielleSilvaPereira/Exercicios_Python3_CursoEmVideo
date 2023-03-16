''' Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

age = 0
cont = 0
man = 0
agecont = 0
genre = ''
ask = ''
youngwoman = 0

while True:
    cont += 1
    age = int(input(f'Digite a idade da {cont} pessoa: '))
    genre = str(input(f'Digite o gênero [M/F] da {cont} pessoa: ')).upper().strip()[0]
    ask = str(input('Deseja continuar analisando pessoas? [S/N]: ')).upper().strip()[0]
    if age > 18:
        agecont += 1
    if genre not in 'fF':
        man += 1
    if genre not in 'Mm' and age < 20:
        youngwoman += 1
    if ask not in 'Ss':
        break

print(f'Há {man} homens nos resultados')
print(f"Há {agecont} pessoas maiores de 18 nos resultados")
print(f'Há {youngwoman} mulheres com menos de 20 anos')















































































