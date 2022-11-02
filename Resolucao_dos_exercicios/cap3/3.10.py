#Faça um programa que calcule o aumento de um salário. Ele deve
#solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento
#e do novo salário.

valor_salario = float(input('Digite o salário do funcionário: '))
porcentagem_aumento = float(input('Digite a porcentagem de aumento: '))
aumento = valor_salario + ((porcentagem_aumento/100)*valor_salario)

print(f'Com um aumento de {porcentagem_aumento:.2f} %, o salário que era de {valor_salario:.2f} R$ passa a ser de {aumento:.2f} R$')