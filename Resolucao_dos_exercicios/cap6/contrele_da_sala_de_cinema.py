lugares_vagos = [10, 2, 1, 3, 0]
while True:
    sala = int(input("Sala (0 sai): "))
    if sala == 0:
        print("FiM")
        break
    if sala > len(lugares_vagos) or sala < 1:
        print(" Sala inválida")
    elif lugares_vagos[sala - 1] == 0:
        print("Desculpe, sala lotada! ")
    else:
        lugares = int(input(f"Quantos lugares você deseja ({lugares_vagos[sala - 1]}vagos): "))
    if lugares > lugares_vagos[sala - 1]:
        print("Esse núMero de lugares não estã dlsponlvel.")
    elif lugares < 0:
        print("NúMero lnvãlldo")
    else:
        lugares_vagos[sala - 1] -= lugares
        print(f"{lugares} lugares vendidos")
print("Utlllzação das salas")
for x, l in enumerate(lugares_vagos):
    print(f"Sala {x + 1} - {l} lugar(es) vazlo(s)")