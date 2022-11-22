#O que acontece quando dois valores são iguais? Rastreie o Programa
#6.20, mas com a lista L = [3, 3, 1, 5, 4].

l = [3, 3, 1, 5, 4]
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

# Como utilizamos o método de bolhas, na primeira verificação, 3, 3 são considerados como na ordem correta.
# Quanto verificamos o segundo 3 com 1, ocorre uma troca.
# O mesmo vai ocorrer com o primeiro 3, mas apenas na próxima repetição. Veja que o 1 subiu para a primeira posição
# como uma bolha de ar dentro d'água.