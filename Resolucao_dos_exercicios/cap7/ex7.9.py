#Modifique o Programa 7.2 para utilizar listas de strings para desenhar
#o boneco da forca . Você pode utilizar uma lista para cada linha e organizá-las em
#uma lista de listas. Em vez de controlar quando imprimir cada parte, desenhe nessas
# listas, substituindo o elemento a desenhar.
'''Exemplo:
linha= list( "X-- --- -
linha['X,, ' _',, , _, , , _, ,
11
)
1 1 _ 1]
, _, , I , ]
 linha[6] = "I"
»> linha
[ 'X,, , _, , , _,, , _, , , _,
 "".join(linha)
'X- - - - -1'''

palavras = [
          "casa",
          "bola",
          "mangueira",
          "uva",
          "quiabo",
          "computador",
          "cobra",
          "lentilha",
          "arroz"]
indice = int(input("Digite um numero:"))
palavra = palavras[(indice * 776) % len(palavras)]
for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0

linhas_txt = """
X==:==
X  :
X
X
X
X
=======

"""

linhas = []

for linha in linhas_txt.splitlines():
    linhas.append(list(linha))

while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
            if erros == 1:
                linhas[3][3] = "O"
            elif erros == 2:
                linhas[4][3] = "|"
            elif erros == 3:
                linhas[4][2] = "\\"
            elif erros == 4:
                linhas[4][4] = "/"
            elif erros == 5:
                linhas[5][2] = "/"
            elif erros == 6:
                linhas[5][4] = "\\"

    for l in linhas:
        print("".join(l))
    if erros == 6:
        print("Enforcado!")
        print(f"A palavra secreta era: {palavra}")
        break
