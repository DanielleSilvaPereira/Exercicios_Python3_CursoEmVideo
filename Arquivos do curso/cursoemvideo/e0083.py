'''Faça um programa que calcule a soma entre todos os números
que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''
soma = 0
for numerosimpares in range(0,501):
    if numerosimpares % 2 != 0:
        soma = numerosimpares + soma
print(soma)