# Modifique o Programa 6.2 para ler 7 notas em vez de 5.
# Faça um progama que calcule a média de 7 notas de um aluno

notas = [0, 0, 0, 0, 0, 0, 0]
count = 0
soma = 0
while count < 7:
    notas[count] = float(input(f'Nota {count+1}: '))
    soma += notas[count]
    count += 1
count = 0
while count < 7:
    print(f'Nota {count+1} = {notas[count]}')
    count += 1
media = soma / count
print(f'A média do aluno é igual a {media:.2f}')