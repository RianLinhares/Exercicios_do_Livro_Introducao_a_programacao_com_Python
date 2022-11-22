# codigo

ultimo = 10
fila = list(range(1, ultimo + 1))
while True:
    print(f'Existem {len(fila)} pessoas na fila')
    print(f'Senhas Atuais: {fila}')
    print(f'''Digite F para adicionar um cliente no fim da fila,
A para realizar o atendimento, S para sair''')
    operaco = str(input('Sua escolha: (F, A ou S) ')).upper()
    if operaco == 'A':
        if len(fila) > 0:
            fila.pop(0)
        else:
            print('Fila Vazia, Nínguem para atender!!')
    elif operaco == 'F':
        ultimo += 1
        fila.append(ultimo)
    elif operaco == 'S':
        break
    else:
        print('Desculpe, Tentativa ínvalida tente novamente')
        print('Usando F, A ou S')
