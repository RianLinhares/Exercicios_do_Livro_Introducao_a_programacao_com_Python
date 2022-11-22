#Escreva um programa que leia uma string e imprima quantas vezes
#cada caractere aparece nessa string.
#String: TTAAC
#Resultado:
#T: 2x
#A: 2x
#C: 1x

frase = input("Digite uma frase para contar as letras: ").upper()
d = {}
for letra in frase:
    # Se letra não existir no dicionário, retorna 0
    # se existir, retorna o valor anterior
    d[letra] = d.get(letra, 0) + 1
for k, v in d.items():
    print(f'{k}: {v}x')