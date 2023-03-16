'''Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''
Numero = int(input('Digite um numero para mostrar sua tabuada: '))
for tabuada in range(1,11):
    ResultadoTabuada = Numero * tabuada
    print(f'{Numero} X {tabuada} = {ResultadoTabuada}')

