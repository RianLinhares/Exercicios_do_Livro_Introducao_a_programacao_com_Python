#Escreva um programa que pergunte o salário do funcionário e calcule
#o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de
#10%. Para os inferiores ou iguais, de 15%.

salario = float(input('Digite o salário do funcionário: '))
if salario >= 1250.00:
    aumento = salario
    novo_salario = salario + (salario * 0.1)
    print(f'Com um salário de {salario} o aumento do funcionário será {aumento}, e o novo salário será {novo_salario}')
if salario < 1250.00:
        aumento = salario
        novo_salario = salario + (salario * 0.15)
        print(
            f'Com um salário de {salario} o aumento do funcionário será {aumento}, e o novo salário será {novo_salario}')
