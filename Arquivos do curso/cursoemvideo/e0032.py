'''calcular 0.50 a cada km de uma viagem até 200km. Depois o valor muda para 0.45'''
v = int(input('Digite o numero de km que serão percorridos durante a viagem: '))
if v < 200:
    print('O valor pago na viagem é equivalente a R${:.2f}'.format(v*0.50))
else:
    print('O valor pago na viagem é equivalente a R${:.2f}'.format(v*0.45))
