#Modifique o Programa 6.6 usando for. Explique por que nem todos
#os while podem ser transformados em for .
# Adição de elementos à lista
l = []
while True:
    n = int(input("Digite um número (0 sai): "))
    if n == 0:
        break
    l.append(n)
for n in l:
    print(n)
    
# O primeiro while não pode ser transformado em for, pois
# não se sabe o números de indices que se o usuário irá digitar
