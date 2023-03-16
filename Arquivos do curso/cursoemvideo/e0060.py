'''Crie um programa que leia dois valores e mostre um menu na tela:'''
from time import sleep
info = int(input('Digite um numero: '))
info2 = int(input('Digite outro numero: '))
menu = int(input('\nEscolha entre as opções abaixo:\n[1]Soma\n[2]Multiplicar\n[3]Maior opção\n[4]Novos numeros\n[5]Sair do programa\nDigite sua opção: '))
while menu != 5:
    if menu == 1:
        print('A soma entre os numeros é {}'.format(info+info2))
        menu = int(input('\nEscolha entre as opções abaixo:\n[1]Soma\n[2]Multiplicar\n[3]Maior opção\n[4]Novos numeros\n[5]Sair do programa\nDigite sua opção: '))
    elif menu == 2:
        print('A multiplicação entre os numeros é {}'.format(info*info2))
        menu = int(input('\nEscolha entre as opções abaixo:\n[1]Soma\n[2]Multiplicar\n[3]Maior opção\n[4]Novos numeros\n[5]Sair do programa\nDigite sua opção: '))
    elif menu == 3:
        if info > info2:
            print('O maior numero é {}'.format(info))
            menu = int(input('\nEscolha entre as opções abaixo:\n[1]Soma\n[2]Multiplicar\n[3]Maior opção\n[4]Novos numeros\n[5]Sair do programa\nDigite sua opção: '))
        else:
            print('o maior numero é {}'.format(info2))
            menu = int(input('\nEscolha entre as opções abaixo:\n[1]Soma\n[2]Multiplicar\n[3]Maior opção\n[4]Novos numeros\n[5]Sair do programa\nDigite sua opção: '))
    elif menu == 4:
        info = int(input('Digite um numero: '))
        info2 = int(input('Digite outro numero: '))
        menu = int(input('\nEscolha entre as opções abaixo:\n[1]Soma\n[2]Multiplicar\n[3]Maior opção\n[4]Novos numeros\n[5]Sair do programa\nDigite sua opção: '))
    else:
        print('Valor invalido')
        menu = int(input('\nEscolha entre as opções abaixo:\n[1]Soma\n[2]Multiplicar\n[3]Maior opção\n[4]Novos numeros\n[5]Sair do programa\nDigite sua opção: '))
sleep(1)