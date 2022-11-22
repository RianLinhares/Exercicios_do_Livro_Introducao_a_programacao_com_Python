#O método get tenta obter a chave procurada; caso não a encontre, retorna o
#segundo parâmetro, no caso O (zero). Se o segundo parâmetro não for especificado,
# get retornará None. Quando a chave é encontrada no dicionário, get retorna
#o valor atualmente associado.
#None é um tipo especial no Python que representa nada ou nenhum valor. Assim,
#uma string vazia "" não é a mesma coisa que None . Todo objeto Python pode
#receber None.

d = {}
for letra in "abracadabra ":
    d[letra] = d.get(letra, 0) + 1
print(d)
