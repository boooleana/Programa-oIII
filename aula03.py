pontos = [[1,2], [5,3], [3,5], [2,4]]
distancia = 0
soma = 0
i = 0

for i in len(pontos):
    if i+1 > len(pontos):
        n = 0
    else:
        n = i+1
    distancia = ((abs(pontos[i,0]-pontos[n,0]))**2 + (abs(pontos[i,1]-pontos[n,1]))**2)**(1/2)
    soma += distancia
print(soma)
