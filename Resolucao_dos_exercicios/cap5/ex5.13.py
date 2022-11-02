'''Escreva um programa que pergunte o valor inicial de uma dívida e
o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número
de meses para que a dívida seja paga, o total pago e o total de juros pago.'''

divida = float(input('Digite o valor da dívida: '))
taxa = float(input('Taxa mensal de juros: '))
pagamento = float(input('Pagamento mensal: '))
mes = 0
if (divida * (taxa / 100)) > pagamento:
    print("Sua dívida não será paga nunca, pois os juros são superiores ao pagamento mensal.")
else:
    saldo = divida
    juros_pago = 0
    while saldo > pagamento:
        juros = saldo * (taxa/100)
        saldo += juros - pagamento
        juros_pago += juros
        print(f"Saldo da dívida no mês {mes} é de R${saldo:6.2f}.")
        mes = mes + 1
    print(f"Para pagar uma dívida de R${divida:8.2f}, a {taxa:5.2f} % de juros,")
    print(f"você precisará de {mes - 1} meses, pagando um total de R${juros_pago:8.2f} de juros.")
    print(f"No último mês, você teria um saldo residual de R${saldo:8.2f} a pagar.")