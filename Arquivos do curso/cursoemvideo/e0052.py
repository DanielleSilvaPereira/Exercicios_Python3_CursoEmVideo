'''LER A RAZÃO E O PRIMEIRO TERMO DE UMA P.A E DIZER OS 10 SEGUINTES'''
c = 0
razao = int(input('Digite a razão da P.A: '))
termo = int(input('Digite o primeiro termo da P.A'))
x = termo + (10-1) * razao

for c in range(termo, x + razao, razao ):
 print(c, end =' >> ')
