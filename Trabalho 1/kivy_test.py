arq = open('teste.txt', 'r')
lista = []

for i in range(len(arq.readlines())):
    print(i)

lista.append(arq.readline().split())


print(lista)

arq.close()
