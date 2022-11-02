#Escreva um programa que leia a quantidade de dias, horas, minutos e
#segundos do usuário. Calcule o total em segundos.

dias = int(input('Digite a quantidade de dias: '))
horas = int(input('Digite a quantidade de horas: '))
minutos = int(input('Digite a quantidade de minutos: '))
segundos = int(input('Digite a quantidade de segundos: '))
segundos_totais = segundos + (60*minutos) + (3600*horas) + (86400*dias)
print(f'O total de segundos é {segundos_totais}')
