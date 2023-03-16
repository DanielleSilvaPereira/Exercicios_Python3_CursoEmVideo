'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
 na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

table = ('Palmeiras', 'Internacional', 'Fluminense', 'Flamengo', 'Corinthians', 'Athletico-MG', 'America-MG', 'Goias', 'São Paulo', 'Chapecoense', 'Bota-fogo', 'Santos', 'Bragantino',
         'Fortaleza', 'Ceara SC', 'Coritiba', 'Avai', 'Cuiaba', 'Juventude')
print(table[0:5])
print(table[15:])
print(f'Chapecoense está na posição {table.index("Chapecoense")+1}º')
print(sorted(table))