ultimo = 0
fila = []
while True:
    print(f'Existem {len(fila)} pessoas na fila')
    print(f'Senhas atuais: {fila}')
    print('''Digite F pa adicionar uma pessoas no fim da fila
A para atender uma pessoa, S para sair''')
    opcao = str(input('Sua Escolha: ')).upper()
    if opcao == 'F':
        ultimo += 1
        fila.append(ultimo)
    elif opcao == 'A':
        fila.pop(0)
        '''if len(fila) > 0:
            fila.pop(0)
        else:
            print('Fila vazia, Nínguém para atender!!')'''
    elif opcao == 'S':
        break
    else:
        print('Desculpe, Tentativa ínvalida tente novamente')
        print('Usando F, A ou S')
