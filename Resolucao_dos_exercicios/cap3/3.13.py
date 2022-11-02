#Escreva um programa que pergunte a quantidade de km percorridos
#por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais
#o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por
#dia e R$ 0,15 por km rodado.

km_percorridos = float(input('Digite a quantidade de km percorridos: '))
dias = float(input('Digite a quantidadde de dias em que o carro foi alugado: '))
preco = (60 * dias) + (0.15 * km_percorridos)
print(f'O preço final do aluguel do carro será {preco} R$')