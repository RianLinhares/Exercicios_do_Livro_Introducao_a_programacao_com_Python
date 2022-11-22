#Modifique o Programa 7.2 de forma a utilizar uma lista de palavras.
#No início, pergunte um número e calcule o índice da palavra a utilizar pela fór-
#mula: tndice = (nú~ero * 776) % len(lista_de_palavras) .
palavras = [
          "casa",
          "bola",
          "mangueira",
          "uva",
          "quiabo",
          "computador",
          "cobra",
          "lentilha",
          "arroz"
     ]

indice = int(input("Digite um numero:"))
palavra = palavras[(indice * 776) % len(palavras)]
print((indice*776) % len(palavras))
for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0
while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else ". "
    print(senha)
    if senha == palavra:
        print("Você acertou! ")
        break
    tentativa = input("\nDigite uma letra: ").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra! ")
        continue
    else:
        digitadas += tentativa
    if tentativa in palavra:
        acertos += tentativa
    else:
        erros += 1
        print("Vocé errou! ")
    print("X== :==\nX : ")
    print("X O " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = " 1 "
    elif erros == 3:
        linha2 = " \ 1 "
    elif erros >= 4:
        linha2 = " \ 1/ "
    print(f"X{linha2} ")
    linha3 = ""
    if erros == 5:
        linha3 += "/"
    elif erros >= 6:
        linha3 += "/ \ "
    print(f"X{linha3}")
    print("X\n----------- ")
    if erros == 6:
        print(" Enforcado !")
        print(f'A palavra correta é {palavra}')
        break
