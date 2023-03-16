'''Ler a velocidade de um carro, e se ele passar de 80km, ele será multado com 7 por cada km acima do limite'''
v = float(input('Digite a velocidade do carro em km: '))
if v > 80:
    print('Voce foi multado >:(')
    print('O valor da multa é o equivalente a {:.2f} reais'.format((v-80)*7))
print('Tenha um bom dia!')

