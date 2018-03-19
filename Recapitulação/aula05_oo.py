class Alternativa:
    def __init__(self, i, resposta, enunciado):
        self.id = i
        self.resposta = resposta
        self.enunciado = enunciado

class Questao:
    alternativas = []
    corretas = []
    teste = [3,1]

    def definir_alternativas(self, i, resposta, enunciado):
        self.alternativas.append(Alternativa(i, resposta, enunciado))

    def verificar(self):
        for i in self.alternativas:
            if i.resposta == True:
                self.corretas.append(i.id)

    def comparar(self):
        if sorted(self.teste) == sorted(self.corretas):
            print("Nice")
        else:
            print("Moios")

if __name__ == "__main__":
    questao = Questao()
    questao.definir_alternativas(1, True, "Com a modernização acelerada do campo na década de 1970, hoje menos de 50%' das propriedades rurais no Brasil têm menos de 100 hectares.")
    questao.definir_alternativas(2, False, "As propriedades com menos de 100 hectares empregam pouca mãode-obra, em razão de seu alto custo, utilizando basicamente a mão-de-obra familiar e, nos períodos de colheita, os bóias-frias.")
    questao.definir_alternativas(3, True, "As propriedades com menos de 100 hectares são responsáveis por cerca de 70%' dos alimentos produzidos no país, com destaque para a mandioca, o feijão, o milho, as aves e os suínos.")
    questao.verificar()
    questao.comparar()
