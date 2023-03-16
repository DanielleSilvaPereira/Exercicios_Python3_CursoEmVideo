'''Contar quantos A aparecem na frase e qual foi a primeira e a ultima vez de sua aparição'''
f = input('Digite uma frase qualquer: ').upper().strip()
print('A primeira vez que A aparece é em {} \nA ultima vez que A aparece é em {}\ne tem {} A na frase ao todo'.format(f.find('A')+1, f.rfind('A')+1, f.count("A")))