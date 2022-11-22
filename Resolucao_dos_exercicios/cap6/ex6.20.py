#Escreva um programa que compare duas listas. Considere a primeira
#lista como a versão inicial e a segunda como a versão após alterações. Utilizando
#operações com conjuntos, seu programa deverá imprimir a lista de modificações
#entre essas duas versões, listando:
#• os elementos que não mudaram
#• os novos elementos
#• os elementos que foram removidos
lista1 = [2, 3, 1, 4, 5]
lista2 = [2, 3, 5, 6]
a = set(lista1)
b = set(lista2)
nao_mudaram = a & b
novos = b - a
removidos = a - b
print(f'Elementos que não mudaram: {nao_mudaram}')
print(f'Novos elementos: {novos}')
print(f'Elementos removidos: {removidos}')

