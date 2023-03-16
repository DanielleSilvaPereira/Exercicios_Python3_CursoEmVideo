'''Um programa que leia o IMC de uma pessoa e diga se ela esta abaixo, ideal, obeso ou muito obeso'''
print('Vamos analisar o seu IMC e contar sua situação')
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura*altura)
if imc < 18.5:
    print('Voce esta abaixo do peso')
elif 18.5 < imc < 25:
    print('Seu peso é o ideal')
elif 25 < imc < 30:
    print('Voce esta acima do peso')
elif 30 < imc < 40:
    print('Voce esta obeso')
elif 40 < imc:
    print('Voce esta com obesidade morbida')