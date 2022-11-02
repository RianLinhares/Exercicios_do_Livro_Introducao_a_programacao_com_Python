#Escreva um programa que pergunte a distância que um passageiro
#deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km
#para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.

distancia = float(input('Qual a distância que o passageiro deja percorrer em km: km '))
if distancia <= 200.0:
    preco = distancia * 0.5
    print(f'Para uma distância de {distancia} será cobrado o valor de 0.5 R$ por km')
    print(f'Logo o preço da passagem será {preco} R$')
else:
    preco = distancia * 0.45
    print(f'Para uma distância de {distancia} será cobrado o valor de 0.45 R$ por km')
    print(f'Logo o preço da passagem será {preco} R$')
