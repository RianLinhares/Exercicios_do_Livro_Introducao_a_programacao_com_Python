compras = []
while True:
    produto = input('Digite o Produto: ').lower()
    if produto == 'fim':
        break
    compras.append(produto)
for p in compras:
    print(p)