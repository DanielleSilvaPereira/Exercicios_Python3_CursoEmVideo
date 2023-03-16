'''Exercício Python 081: Crie um programa que vai ler vários números e colocar numa lista.

Depois disso, mostre:
                                                                                                                                                
A) Quantos números foram digitados.

B) A lista de valores, ordenada de forma decrescente.

C) Se o valor 5 foi digitado e está ou não na lista.
'''

lista = []
numberfiveyes = 0

while True:
    n = int(input('Digite um número: '))
    c = str(input('Deseja continuar ? [S/N]: '))
    if n == 5:
        lista.append(n)
        numberfiveyes = 1
    if n == int:
        lista.append(n)
    if c in 'Nn':
        break



print(f'A ordem da lista decrescente dos números digitados é {lista.sort(reverse=True)}')
print(f'A quantidade de valores digitados foram {len(lista)+1}')
if numberfiveyes == 1:
    print('O número 5 está nessa lista')
else:
    print('O número 5 não está nessa lista')