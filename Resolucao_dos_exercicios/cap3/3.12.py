#Escreva um programa que calcule o tempo de uma viagem de carro.
#Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = float(input('Digite a distância a percorrer: Km '))
velocia_media = float(input('Digite a velocidade média esperada para a viagem:Km/h  '))
tempo = distancia/velocia_media
print(f'Para percorrer uma distância de {distancia:.2f} á uma velocidade média de {velocia_media:.2f} será necessário {tempo:.2f} horas')