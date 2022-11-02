'''Escreva um programa que pergunte o depósito inicial e a taxa de
juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses.
Escreva o total ganho com juros no período.'''

dep_inicial = float(input('Digite o valor do depósito inicial: '))
taxa_juros = float(input('Digite a taxa de juros: '))
somador = dep_inicial
count = 0
while count < 24:
    somador += (dep_inicial * (taxa_juros / 100))
    count += 1
    print(f'Valor no mês {count}: {somador:.2f} R$')
print(f'Ao todo você teve um lucro de {somador - dep_inicial:.2f} R$')
