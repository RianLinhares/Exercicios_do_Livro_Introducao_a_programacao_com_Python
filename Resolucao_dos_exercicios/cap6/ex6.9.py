#Modifique o exemplo para pesquisar dois valores. Em vez de apenas p,
#leia outro valor v que também será procurado. Na impressão, indique qual dos
#dois valores foi achado primeiro.

l = [15, 7, 27, 39]
p = int(input("Digite o primeiro valor a procurar: "))
v = int(input('Digite o segundo valor a procurar: '))
achoup = False
achouv = False
primeiro = 0
x = 0
while x < len(l):
    if l[x] == p:
        achoup = True
        if not achouv:
            primeiro = 1
        break
    if l[x] == v:
        achouv = True
        if not achoup:
            primeiro = 2
    x += 1
if achoup:
    print(f"{p} achado na posição {x}")
else:
    print(f"{p} não encontrado")
if achouv:
    print(f'{v} achado na posição {x}')
else:
    print(f'{v} não encontrado')
if primeiro == 1:
    print(f'p foi achado primeiro!!')
elif primeiro == 2:
    print(f'v foi achado primeiro!!!')
