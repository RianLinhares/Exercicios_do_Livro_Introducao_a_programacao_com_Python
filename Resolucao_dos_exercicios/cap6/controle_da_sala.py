lugares_vagos = [10, 2, 1, 3, 0] # cada item da lista representa uma sala
while True:
    sala = int(input('Sala: (0 sai) '))
    if sala == 0:
        print('FIM!!')
        break
    if sala > len(lugares_vagos) or sala < 1:
        print('Sala Inválida!!')
    elif lugares_vagos[sala - 1] == 0:
        print('Desculpe, sala lotada!!!')
    else:
        lugares = int(input(f'Quantos Lugares você deseja ({lugares_vagos[sala - 1]} Vagos): '))
    if lugares > lugares_vagos[sala - 1]:
        print(f'Este número de lugares não está disponível!!')
    elif lugares < 0:
        print('Número Ínvalido')
    else:
        lugares_vagos[sala - 1] -= lugares
        print(f'{lugares} lugares vendidos!!')
print('Utilização das salas')
for i, v in enumerate(lugares_vagos):
    print(f'Sala {i + 1} - Lugares {v}')
