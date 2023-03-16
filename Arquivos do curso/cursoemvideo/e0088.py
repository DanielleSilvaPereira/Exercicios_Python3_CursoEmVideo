'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. '''
Frase = str(input('Digite uma frase: ')).strip().upper()
FraseEspaço = Frase.split()
FraseSeparador = ' '.join(FraseEspaço)
FraseContrario = FraseSeparador[::-1]
if FraseContrario == Frase:
    print('A frase é um palindromo')
else:
    print('A frase não é um palindromo')