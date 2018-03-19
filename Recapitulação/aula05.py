alternativas = [(1, False, "Com a modernização acelerada do campo na década de 1970, hoje menos de 50%' das propriedades rurais no Brasil têm menos de 100 hectares."),
                (2, False, "As propriedades com menos de 100 hectares empregam pouca mãode-obra, em razão de seu alto custo, utilizando basicamente a mão-de-obra familiar e, nos períodos de colheita, os bóias-frias."),
                (3, True, "As propriedades com menos de 100 hectares são responsáveis por cerca de 70%' dos alimentos produzidos no país, com destaque para a mandioca, o feijão, o milho, as aves e os suínos.")]

teste = [3]
resposta = []
i = 0

for i in alternativas:
    if i[1] == True:
        resposta.append(i[0])

if sorted(teste) == sorted(resposta):
    print("Nice")
else:
    print("Moios")
