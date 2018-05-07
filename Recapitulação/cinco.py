"""
    ATRIBUTOS

    nome pessoa
    ultimo produto comprado
    data ultima comprado
    recomendação de produto
    desconto oferecido
    email cliente
"""

class AbrirArquivo:
    def __init__(self):
        self.ler()
        self.separar_em_linhas()
        self.separar_em_info()

    def ler(self):
        self.arquivo = open("cinco.txt", "r")
        self.dados = self.arquivo.read()
        self.arquivo.close()

    def separar_em_linhas(self):
        self.linhas = self.dados.splitlines()

    def separar_em_info(self):
        self.lista_dado = []
        for i in self.linhas:
            self.lista_dado.append(i.split(";"))

class MalaDireta:
    def __init__(self):
        self.mala = """
Prezado(a) <CLIENTE>,

Em sua última visita ao nosso estabelecimento (<DATA>),
registramos que você adquiriu <PRODUTO>.
Estamos com grandes descontos previstos para o próximo feriado (dia 1 de maio).
Por isso, gostaríamos de recomendar a você especialmente o produto <RECOMENDADO>,
que se encontra com <DESCONTO> porcento de desconto.

--
Esse email foi enviado para <EMAIL>.
Respeitamos sua privacidade, para não receber mais nossas mensagens
envie email para sair@minhaloja.com.br, com o assunto 'SAIR'.

Atenciosamente,
Equipe de interação com o clienta da minhaloja.com.br

                        """
        self.valores = []
        self.atributos()
        self.lista_email = []
        self.variaveis()

    def atributos(self):
        arquivo = AbrirArquivo()
        for i in arquivo.lista_dado:
            if i[0] != "nome":
                cliente = i

                d = {"nome": 0,
                      "produto": 1,
                      "data":2,
                      "recomendado": 3,
                      "desconto": 4,
                      "email": 5
                }

                self.valores.append([("<CLIENTE>", cliente[d["nome"]]),
                                  ("<DATA>",cliente[d["data"]]),
                                  ("<PRODUTO>", cliente[d["produto"]]),
                                  ("<RECOMENDADO>", cliente[d["recomendado"]]),
                                  ("<DESCONTO>", cliente[d["desconto"]]),
                                  ("<EMAIL>", cliente[d["email"]])])

    def variaveis(self):
        for i in self.valores:
            email = self.mala[:]
            for j in i:
                email = email.replace(j[0], j[1])

            self.lista_email.append(email)



a = MalaDireta()
print(a.lista_email[1])
