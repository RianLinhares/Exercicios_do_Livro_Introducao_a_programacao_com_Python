#Modifique o programa para trabalhar com duas filas. Para facilitar
#seu trabalho, considere o comando A para atendimento da fila 1; e B, para atendimento
#da fila 2. O mesmo para a chegada de clientes: F para fila 1; e G, para fila 2.

ultimo = 10
fila1 = list(range(1, ultimo + 1))
fila2 = list(range(1, ultimo + 1))
while True:
    print(f'Existem {len(fila1)} pessoas na fila 1')
    print(f'Senhas Atuais da fila 1: {fila1}')
    print(f'Existem {len(fila2)} pessoas na fila 2')
    print(f'Senhas Atuais da fila 2: {fila2}')
    fila = str(input('Digite a fila que você deseja acessar, ou S paraa sair: '))
    if fila == '1':
        print(f'''Digite F para adicionar um cliente no fim da fila,
A para realizar o atendimento ''')
        operaco = str(input('Sua escolha: (F ou A ) ')).upper()
        for l in operaco:
            if l == 'A':
                if len(fila1) > 0:
                    fila1.pop(0)
                else:
                    print('Fila Vazia, Nínguem para atender!!')
            elif l == 'F':
                ultimo += 1
                fila1.append(ultimo)
            else:
                print('Desculpe, Tentativa ínvalida tente novamente')
                print('Usando F, A ou S')
    elif fila == '2':
        print(f'''Digite G para adicionar um cliente no fim da fila,
B para realizar o atendimento''')
        operaco = str(input('Sua escolha: (G ou B ) ')).upper()
        for l in operaco:
            if l == 'B':
                if len(fila2) > 0:
                    fila2.pop(0)
                else:
                    print('Fila Vazia, Nínguem para atender!!')
            elif l == 'G':
                ultimo += 1
                fila2.append(ultimo)
            else:
                print('Desculpe, Tentativa ínvalida tente novamente')
                print('Usando G ou B')
    elif fila == 'S' or fila == 's':
        break
