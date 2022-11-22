# Altere o Programa 6.11 (Verificação do Maior valor)
# de forma a imprimir o menor elemento da lista.

l = [1, 7, 2, 4]
minimo = l[0]
for e in l:
    if e < minimo:
        minimo = e
print(minimo)