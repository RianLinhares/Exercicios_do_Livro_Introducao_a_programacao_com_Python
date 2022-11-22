s = "Alô mundo"
print(s.find("l"))
#Se o objetivo for pesquisar, mas da direita para a esquerda, utilize o método
#rfind, que realiza essa tarefa:
a = "Alô mundo"
print(a.rfind("A"))
#Tanto fi.nd quanto rfi.nd suportam duas opções adicionais: início (start) e fim
#(end). Se você especificar início, a pesquisa começará a partir dessa posição. Se
#especificar o fim, a pesquisa utilizará essa posição como último caractere a considerar
# na pesquisa. Por exemplo:

s = "um tigre, dois tigres, três tigres"
print(s.find("tigres"))
print(s.rfind("tigres"))
print(s.find("tigres", 7)) # Início=7
print(s.find("tigres", 30)) # Início=30
print(s.find("tigres", 0, 10)) # Início=0 fim=10
