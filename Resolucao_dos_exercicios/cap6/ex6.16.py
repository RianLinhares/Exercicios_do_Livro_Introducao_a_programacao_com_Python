#Modifique o Programa 6.20 para ordenar a lista em ordem decrescente.
# L = [1, 2, 3, 4, S] deve ser ordenada como L = [S, 4, 3, 2, 1]

l = [1, 2, 3, 4 , 5]
fim = 5
while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if l[x] < l[x + 1]:
            trocou = True
            temp = l[x]
            l[x] = l[x + 1]
            l[x + 1] = temp
        x += 1
    if not trocou:
        break
    fim -= 1
for e in l:
    print(e)
