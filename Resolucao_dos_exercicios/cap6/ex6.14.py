#O que acontece quando a lista já está ordenada? Rastreie o
#Programa 6.20, mas com a lista L = [1, 2, 3, 4 , 5].

l = [1, 2, 3, 4 , 5]
fim = 5
while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if l[x] > l[x + 1]:
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

# como nenhum elemento é maior que o elemento seguinte
# O código para no primeiro break