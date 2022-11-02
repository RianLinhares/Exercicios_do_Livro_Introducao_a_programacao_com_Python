#Escreva um programa para calcular a redução do tempo de vida de
#um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos
#ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro,
#e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

n_cigarros = int(input('Digite o número de cigarros fumados por dia: '))
n_anos = float(input('Quantos anos de fumante: '))
horas_perdidos_minutos = 10 * n_cigarros * 365 * n_anos
tempo_totalperdido = horas_perdidos_minutos / (24 * 60)
print(f'Ao longo da vida o fumante téra perdido {tempo_totalperdido:.2f} dias de vida')
