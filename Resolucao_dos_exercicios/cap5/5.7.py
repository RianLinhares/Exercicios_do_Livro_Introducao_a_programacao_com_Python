n = int(input('Tabuada de: '))
inicio = int(input('Início: '))
fim = int(input('Fim: '))
count = inicio
while count <= fim:
    print(f'{n} x {count} = {count*n}')
    count += 1