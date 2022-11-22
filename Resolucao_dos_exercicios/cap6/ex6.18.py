#Escreva um programa que gere um dicionário, em que cada chave seja
#um caractere, e seu valor seja o número desse caractere encontrado em uma frase lida.
#Exemplo : O rato -> { "O" : 1 , " r " : 1 , " a " : 1 , " t " : 1 , " o " : 1}

frase = input("Digite uma frase para contar as letras: ")
d = {}
for letra in frase:
    # Se letra não existir no dicionário, retorna 0
    # se existir, retorna o valor anterior
    d[letra] = d.get(letra, 0) + 1
print(d)
