#Faça um programa que percorra duas listas e gere uma terceira sem
#elementos repetidos.

lista1 = []
lista2 = []
lista3 = []
lista4 = []
print(f'{"LISTA 1":^30}')
while True:
    n = float(input(f'Digite um número: [0] para sair '))
    if n == 0:
        break
    lista1.append(n)
print(f'{"LISTA 2":^30}')
while True:
    n = float(input(f'Digite um número: [0] para sair '))
    if n == 0:
        break
    lista2.append(n)
lista3.extend(lista1)
lista3.extend(lista2)
count = 0
while count < len(lista3):
    if lista3[count] not in lista4:
        lista4.append(lista3[count])
    count += 1
print(lista4)
