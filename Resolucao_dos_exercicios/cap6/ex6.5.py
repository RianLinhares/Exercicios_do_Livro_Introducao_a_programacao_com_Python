#Altere o Programa 6.7 de forma a poder trabalhar com vários comandos
#digitados de uma só vez. Atualmente, apenas um comando pode ser inserido
#por vez. Altere-o de forma a considerar operação como uma string.
#Exemplo: FFFAAAS significaria três chegadas de novos clientes, três atendimentos
#e, finalmente, a saída do programa.
# Progama da fila
ultimo = 10
fila = list(range(1, ultimo + 1))
while True:
    print(f'Existem {len(fila)} pessoas na fila')
    print(f'Senhas Atuais: {fila}')
    print(f'''Digite F para adicionar um cliente no fim da fila,
A para realizar o atendimento, S para sair''')
    operaco = str(input('Sua escolha: (F, A ou S) ')).upper()
    for l in operaco:
        if l == 'A':
            if len(fila) > 0:
                fila.pop(0)
            else:
                print('Fila Vazia, Nínguem para atender!!')
        elif l == 'F':
            ultimo += 1
            fila.append(ultimo)
        elif l == 'S':
            break
        else:
            print('Desculpe, Tentativa ínvalida tente novamente')
            print('Usando F, A ou S')

