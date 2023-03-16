'''um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
med = 0
men = 0
mai = 0
velh = ''
for cont in range(1,5):
    nome = input('Digite o nome da {} pessoa: '.format(cont))
    idade = int(input('Digite a idade da {} pessoa: '.format(cont)))
    genero = str(input('Digite o gênero da {} pessoa. (M ou F) '.format(cont))).strip()
    med += idade
    if cont == 1 and genero in 'Mm':
     mai = idade
     velh = nome
    if genero in 'Mm' and idade > mai:
        idade = mai
        velh = nome
    if genero in 'Ff' and idade < 20:
        men += 1
med = med/4
print('Há {} meninas com menos de 20 anos'.format(men))
print('A média de idade do grupo é {} anos'.format(med))
print ('O homem mais velho se chama {}'.format(velh))
