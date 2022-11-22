#Modifique o programa do Exercício 6.9 (Pesquisa) de forma a pesquisar p e v
#em toda a lista e informando o usuário a posição onde p e a posição onde v foram
#encontrados.

l = [15, 7, 27, 39]
p = int(input("Digite o primeiro valor a procurar: "))
v = int(input('Digite o segundo valor a procurar: '))
achoup = False
achouv = False
primeiro = 0
x = 0
pos1 = 0
pos2 = 0
while x < len(l):
    if l[x] == p:
        achoup = True
        pos1 = x
        if not achouv:
            primeiro = 1
    if l[x] == v:
        achouv = True
        pos2 = x
        if not achoup:
            primeiro = 2
    x += 1
if achoup:
    print(f"{p} achado na posição {pos1}")
else:
    print(f"{p} não encontrado")
if achouv:
    print(f'{v} achado na posição {pos2}')
else:
    print(f'{v} não encontrado')
if achoup == True and achouv == True:
    if primeiro == 1:
        print(f'p foi achado primeiro!!')
    elif primeiro == 2:
        print(f'v foi achado primeiro!!!')
