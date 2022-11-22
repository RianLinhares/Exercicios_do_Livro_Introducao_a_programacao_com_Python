palavra = str(input('Digite a palavra secreta: ')).strip().lower()
digitadas = []
acertos = []
erros = 0
while True:
    senha = ''
    for letra in palavra:
        if letra in acertos:
            senha += letra
        else:
            senha += '.'
    print(senha)
    if senha == palavra:
        print('VOCÊ ACERTOU!!!')
        break
    tentativa = str(input('\nDigite uma letra: ')).lower().strip()
    if tentativa in digitadas:
        print('Você já digitou essa letra!!')
    else:
        digitadas += tentativa
    if tentativa in palavra:
        acertos += tentativa
    else:
        erros += 1
    if erros == 6:
        print('Enforcado')
        break
