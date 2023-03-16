''' Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python.
 No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
import random
c = 1
jogadores = dict()
jogadores['jogador1'] = random.randint(0,6)
jogadores['jogador2'] = random.randint(0,6)
jogadores['jogador3'] = random.randint(0,6)
jogadores['jogador4'] = random.randint(0,6)
jogo = {jogadores}
for dicionario in sorted(jogadores, key=jogadores.get):
 print(f'{c}º lugar vai para {dicionario} com o número {jogadores[dicionario]}')
 c += 1

