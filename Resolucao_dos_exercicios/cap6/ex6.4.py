#O que acontece quando não verificamos se a lista está vazia antes de
#chamarmos o método pop?
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
    elif opcao == 'S':
        break
    else:
        print('Desculpe, Tentativa ínvalida tente novamente')
        print('Usando F, A ou S')
'''Acontece um erro, mensagem de erroTraceback (most recent call last):
  File "/home/rian/PycharmProjects/Projects/exericioscap6livro/filas2.py", line 13, in <module>
    fila.pop(0)
IndexError: pop from empty list'''