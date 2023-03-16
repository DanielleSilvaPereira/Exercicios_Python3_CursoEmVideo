'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
 Depois vai ler a quantidade de gols feitos em cada partida. No final,
 tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
aproveitamento = 0
dicionario = {}
lista = list()
#nome do jogador e a quantidade de partidas
print('==================ÁNALISE DO JOGADORE==================')
dicionario['jogadore'] = str(input('Digite o nome do jogadore: '))
dicionario['partidas'] = int(input('Digite a quantidade de partidas que elu jogou: '))

for numerodegols in range(0, dicionario['partidas']):
    lista.append(int(input(f"Digite a quantidade de gols que elu fez na {numerodegols+1}º partida: ")))


for lista in lista:
    aproveitamento += lista

dicionario['gols'] = aproveitamento


print(f"O jogadore {dicionario['jogadore']} participou de {dicionario['partidas']} partidas")
print(f"Seu número total de gols na temporada foi {dicionario['gols']}")