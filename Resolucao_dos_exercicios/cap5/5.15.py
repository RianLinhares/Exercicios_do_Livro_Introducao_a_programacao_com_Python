'''Escreva um programa para controlar uma pequena máquina registra-
dora. Você deve solicitar ao usuário que digite o código do produto e a quantidade
comprada. Utilize a tabela de códigos a seguir para obter o preço de cada produto:
Seu programa deve exibir o total das compras depois que o usuário digitar O.
Qualquer outro código deve gerar a mensagem de erro "Código inválido''.'''
total = 0
while True:
    codigo = int(input("Código da mercadoria (0 para sair): "))
    preco = 0
    if codigo == 0:
        break
    elif codigo == 1:
        preco = 0.50
    elif codigo == 2:
        preco = 1.00
    elif codigo == 3:
        preco = 4.00
    elif codigo == 5:
        preco = 7.00
    elif codigo == 9:
        preco = 8.00
    else:
        print("Código inválido!")
    if preco != 0:
        quantidade = int(input('Digite a quantidade: '))
        total += (quantidade*preco)
print(f'Total a pagar {total} R$')
