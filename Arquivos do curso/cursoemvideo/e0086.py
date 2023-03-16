'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''
Razao = float(input('Digite a razão da PA: '))
PrimeiroTermo = float(input('Digite o primeiro termo da PA: '))
for ProgressãoAritmética in range(1,11):
    Resultado = PrimeiroTermo + (ProgressãoAritmética - 1)* Razao
    print(f'O {ProgressãoAritmética}º é {Resultado}')
