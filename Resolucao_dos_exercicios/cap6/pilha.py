# algoritmo pilha

prato = 5
pilha = list(range(1, prato + 1))
while True:
    print(f'Têm {len(pilha)} prato(s), para serem lavados.')
    print(f'Pilha Atual: {pilha}')
    print(f'''Digite E para empilhar, D para desempilhar, S para sair''')
    escolha = str(input('Sua Escolha: [E, D ou S] ')).upper()
    if escolha == 'E':
        prato += 1
        pilha.append(prato)
    elif escolha == 'D':
        if len(pilha) > 0:
            pilha.pop(-1)
        else:
            print('Pilha Vazia!!!')
    elif escolha == 'S':
        break
    else:
        print('Tentativa Ínvalida, Tente novamente digitando E, D ou S')
