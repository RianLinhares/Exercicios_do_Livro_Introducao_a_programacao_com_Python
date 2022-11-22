compras = []
while True:
    produto = input('Digite o Produto: ').lower()
    if produto == 'fim':
        break
    quantidade = int(input('Quantidade: '))
    preco = float(input('Preço: '))
    compras.append([produto, quantidade, preco])
soma = 0
for e in compras:
    print(f'{e[0]} X {e[1]} X {e[2]} X {e[1] * e[2]}')
    soma += e[1] * e[2]
print(f'Total: {soma:7.2f}')
