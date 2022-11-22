#A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista
#T = [ -10, -8, 0, 1, 2, 5, -2, -4] . Faça um programa que imprima a menor e a
#maior temperatura, assim como a temperatura média.

t = [-10, -8, 0, 1, 2, 5, -2, -4]
menor = t[0]
maior = t[0]
soma = 0
count = 0
for e in t:
    soma += e
    if e > maior:
        maior = e
    if e < menor:
        menor = e
    count += 1
media = soma/count
print(f'Menor: {menor}')
print(f'Maior: {maior}')
print(f'Média: {media}')