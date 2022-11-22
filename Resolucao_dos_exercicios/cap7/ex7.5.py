#Escreva um programa que leia duas strings e gere uma terceira, na
#qual os caracteres da segunda foram retirados da primeira.
#1 string: AATTGGAA
#2 string: TG
#3 string: AAAA

palavra1 = str(input('Digite uma frase: ')).upper()
palavra2 = str(input('Digite uma frase: ')).upper()
palavra3 = ''
for l in palavra1:
    if l not in palavra2:
        palavra3 += l
if palavra3 == "":
    print("Todos os caracteres foram removidos.")
else:
    print(f"Os caracteres {palavra2} foram removidos de {palavra1}, gerando: {palavra3}")
