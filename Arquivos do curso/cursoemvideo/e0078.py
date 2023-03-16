'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''
Peso = float(input('Digite o seu peso (em quilos): '))
Altura = float(input('Digite a sua altura (em metros): '))
IMC = Peso/(Altura*Altura)
if IMC < 18.5:
    print('Abaixo do peso')
elif IMC < 25:
    print('Peso ideal')
elif IMC < 30:
    print('Sobrepeso')
elif IMC < 40:
    print('Obesidade')
elif IMC > 40:
    print('Obesidade morbida')
