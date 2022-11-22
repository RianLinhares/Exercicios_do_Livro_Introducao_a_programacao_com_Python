#Escreva um programa que compare duas listas. Utilizando operações com conjuntos, imprima:
#os valores comuns às duas listas
#os valores que só existem na primeira
#os valores que existem apenas na segunda
#uma lista com os elementos não repetidos das duas listas.
#a primeira lista sem os elementos repetidos na segunda

a = {0, 1, 2, 3, -1 }
b = {2, 3, 4, 5}
print(f'Lista a: {a}')
print(f'Lista b: {b}')
conjunto1 = set(a)
conjunto2 = set(b)
comum = conjunto1 & conjunto2
vexa = conjunto1 - conjunto2
vexb = conjunto2 - conjunto1
nao_repetidos = conjunto1 ^ conjunto2
print(f'Valores comuns as duas listas: {comum}')
print(f'Valores que só existem na primeira: {vexa}')
print(f'Valores que só existem na segunda: {vexb}')
print(f'Valores não repetidos das duas listas: {nao_repetidos}')
print(f'Primeira lista sem os elementos repetidos na segunda: {vexa}')