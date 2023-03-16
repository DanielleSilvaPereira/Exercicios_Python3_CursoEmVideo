'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
 No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

products = ('Coffe', 8.00, 'Milk', 5.00, 'Cookies', 7.00, 'Salt', 3.00, 'Sugar', 3.00,
            'Rice', 12.00)

print(products)
print(f'{products[0]}        {products[1]}')
print(f'{products[2]}        {products[3]}')
print(f'{products[4]}        {products[5]}')
print(f'{products[6]}        {products[7]}')
print(f'{products[8]}        {products[9]}')
print(f'{products[10]}        {products[11]}')

for pos in range(0, len(products)):
    if pos % 2 == 0:
        print(f'{products[pos]:.<30}', end= ' ')
    else:
        print(f'${products[pos]:<5.2f}')
