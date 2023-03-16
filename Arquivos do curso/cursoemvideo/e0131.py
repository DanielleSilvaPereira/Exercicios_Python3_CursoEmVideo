''' Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
 A) Quantas pessoas foram cadastradas
 B) A média de idade
 C) Uma lista com as mulheres
 D) Uma lista de pessoas com idade acima da média'''

mulheres = list()
dicionario = dict()
media = list()
lista = list()
matematica = 0
acimamedia =list()
#Lendo os dados das pessoas dentro do dicionário e colocando todos os dicionários em uma lista.
while True:
    dicionario['nome'] = str(input("Digite o nome da pessoa: "))
    dicionario['idade'] = int(input('Digite a idade da pessoa: '))
    dicionario['genero'] = int(input('Digite o genero da pessoa\n[1] feminino\n[2] masculino\n[3] não-binário\n'))
    continuar = str(input('Deseja adicionar outra pessoa?[S] ou [N]: ')).upper()
    media.append(dicionario['idade'])
    lista.append(dicionario.copy())
    if dicionario['genero'] == 1:
        mulheres.append(dicionario['nome'])
    if continuar == 'N':
        break
pessoas_velhas = list
soma_media = sum(media)
resultado_media = soma_media/len(lista)



print(lista)
print(f'O número de pessoas cadastradas foi {len(lista)}')
print(f'As mulheres cadastradas foram: ',end='')
for printe in range(len(mulheres)):
    print(mulheres[printe])
print(f'A média de idade foi {resultado_media}')
for p in dicionario:
    if p['idade'] >= resultado_media:
        for k,v in p.itens():
            print(f'{k} = {v}: ', end='')
            print()