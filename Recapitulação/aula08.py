trajetos = []

def rota(trajeto, percorrer):
    if percorrer == []:
        trajetos.append(trajeto)
    else:
        for i in percorrer:
            trajeto_novo = trajeto[:]
            trajeto_novo.append(i)

            percorrer_novo = percorrer[:]
            percorrer_novo.remove(i)

            rota(trajeto_novo, percorrer_novo)

rota([],['A','B','C','D'])

for i in trajetos:
    print(i)
