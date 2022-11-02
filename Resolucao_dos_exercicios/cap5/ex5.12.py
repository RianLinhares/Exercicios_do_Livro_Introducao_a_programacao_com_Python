'''Altere o programa anterior de forma a perguntar também o valor
depositado mensalmente. Esse valor será depositado no início de cada mês, e você
deve considerá-lo para o cálculo de juros do mês seguinte.'''

dep_inicial = float(input('Digite o valor do depósito inicial: '))
taxa_juros = float(input('Digite a taxa de juros: '))
dep_mensal = float(input('Valor depositado mensalmente: '))
somador = dep_inicial
count = 0
while count < 24:
    somador += (somador * (taxa_juros / 100)) + dep_mensal
    count += 1
    print(f'Valor no mês {count}: {somador:.2f} R$')
print(f'Ao todo você teve um lucro de {somador - dep_inicial:.2f} R$')

