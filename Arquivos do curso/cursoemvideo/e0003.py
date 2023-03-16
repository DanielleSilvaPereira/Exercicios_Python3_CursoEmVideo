
#n = input ('Digite algo')
#print = (n.isnumeric
#print = (type float(n))
#print = (type bool(n))
#print = (type str(n))

#n = input('Digite algo: ')
#print (type (n) )
#print('É numerico?', n.isnumeric())
#print('É minusculo(a)?',n.islower())
#print ('maiusculo(a)?',n.isupper())
#print('É alfanumérico?',n.isalnum())
#print('É compostos por maiusculas e minusculas?', n.istitle())
#print('É só espaços?', n.isspace())
#print('É apenas letras?', n.isalpha())

#x = input('Digite algo')
#n1 = ('São só letras?', x.isalpha())
#n2 = ('São numeros e letras?', x.isalnum())
#n3 = ('São apenas espaços?', x.isspace())
#n5 = ('Tem letras minusculas e maisuculas?', x.istitle())
#n6 = ('Está em maiúsculo?', x.isupper())
#n7 = ('Está em minusculo?', x.islower())
#print .format{n1,
#            n2,
#           n3,
#             n5,
#            n6,
#           n7}

y = input('Digite algo: ')
print('{} É do tipo {}'.format(y, type(y)))
print('{} Só tem espaço?{}'.format(y, y.isspace()))
print('{} Só tem número?{}'.format(y, y.isnumeric()))
print('{} Só tem letra?{}'.format(y, y.isalpha()))
print('{} Tem números e letras?{}'.format(y, y.isalnum()))
print('{} Só tem minúscula?{}'.format(y, y.islower()))
print('{} Só tem maiúscula?{}'.format(y, y.isupper()))