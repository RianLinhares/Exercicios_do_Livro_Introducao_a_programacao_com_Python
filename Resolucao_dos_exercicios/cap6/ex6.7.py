'''Faça um programa que leia uma expressão com parênteses. Usando
pilhas, verifique se os parênteses foram abertos e fechados na ordem correta.
Exemplo:
        ( ()) OK
        ()() (( ) ()) OK
        ()) Erro
Você pode adicionar elementos à pilha sempre que encontrar abre parênteses e
desempilhá-la a cada fecha parênteses. Ao desempilhar, verifique se o copo da pilha
é um abre parênteses. Se a expressão estiver correta, sua pilha estará vazia no final.'''

pilha = []
expressao = str(input('Digite sua expressão: '))
for item in expressao:
    if item == '(':
        pilha.append(0)
    elif item == ')':
        if len(pilha) > 0:
            pilha.pop(0)
        elif len(pilha) == 0:
            pilha.append(1)
print(pilha)
if len(pilha) == 0:
    print('OK')
else:
    print('ERRO')
