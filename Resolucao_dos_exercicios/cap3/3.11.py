#Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
#Exiba o valor do desconto e o preço a pagar.

preco_mercadoria = float(input('Digite o preço da mercadoria: '))
percentual_desconto = float(input('Digite a porcentagem de desconto: '))
desconto = preco_mercadoria - ((percentual_desconto/100)*preco_mercadoria)

print(f'Com um desconto de {percentual_desconto:.2f} %, o valor da mercadoria que era de {preco_mercadoria:.2f} R$ passa a ser de {desconto:.2f} R$')