class ManipularArquivo(object):
    def __init__(self):
        self.lista = []  #  lista de informações (maça)
        self.inserir = False  #  váriavel que controla se será inserido os dados do arquivo ou não
        criar = True   #  se for preciso criar o arquivo
        if criar:
            self.run_criar_arquivo()
        self.run_ler_arquivo()

    def abrir_arquivo(self, tipo = 'r'):
        self.arquivo = open('arquivo.txt', tipo)  #  default abre o arquivo para leitura

    def ler_arquivo(self):
        texto = self.arquivo.readlines()  # lê todas as linhas do arquivo
        for string in texto:  #  percorre o texto
            self.lista.append(string.split())  #  coloca as informações em uma lista

    def criar_arquivo(self):  #  cria o arquivo
        texto = ""
        if self.inserir:  #  se o usuario for inserir os valores
            for i in range(1,4):
                print("\nInsira os valores da maça " + str(i) + "\n")
                tipo = input("Tipo: ")
                pais = input("País de Origem: ")
                cor = input("Cor: ")
                texto += tipo + " " + pais + " " + cor + " \n"
        else:  #  se o usuario não for inserir os valores
            texto = """Fuji Brasil Vermelha
                       Gala Colombia Verde
                       Fuji Chile Vermelha"""
        self.arquivo.writelines(texto)

    def to_string(self):
        print("\nARQUIVO\n")
        print(self.lista)  #  mostra a lista
        print()

    def fechar_arquivo(self):
        self.arquivo.close()  # fecha o arquivo

    def run_criar_arquivo(self):  #  roda a classe para escrever o arquivo
        self.abrir_arquivo('w')
        self.criar_arquivo()
        self.fechar_arquivo()

    def run_ler_arquivo(self):  #  roda a classe para ler o arquivo
        self.abrir_arquivo()
        self.ler_arquivo()
        self.fechar_arquivo()

class Maca(object):  #  objeto para a maça
    def __init__(self, lista = None): # define o default da lista para None # lista = caracteristicas
        self.tipo, self.pais_origem, self.cor = lista  #  atribui valores

    def to_string(self): #  exibe valores
        print("Tipo: " + self.tipo)
        print("País de origem: " + self.pais_origem)
        print("Cor: " + self.cor)


class Cesta(object):  #  cesta de maças
    def __init__(self):
        self.lista_de_macas = []  #  lista de maças (lista de objetos)

    def encher_cesta(self): #lê arquivo e cadastra na classe Maça
        self.lista = ManipularArquivo()  #  lê arquivo usando a classe ManipularArquivo
        for i in self.lista.lista:  #  percorre pela lista criada em ManipularArquivo
            self.lista_de_macas.append(Maca(i))  #  cria as maças com os valores da lista(ManipularArquivo) e atribui valores em lista_de_macas

    def to_string(self):  #  mostra o conteúdo da cesta
        print("---------")
        print("\n  CESTA\n")
        print("---------")

        for i in self.lista_de_macas:
            print()
            i.to_string()

if __name__ == "__main__":  #  programa principal
    cesta = Cesta()
    cesta.encher_cesta()
    cesta.lista.to_string()  #  para executar o to_string de ManipularArquivo (requesito do trabalho)
    cesta.to_string()


"""
Verificação se todas os métodos estãos sendo usados (requesito g do trabalho)

Classe: ManipularArquivo
    Métodos: __init__ = ok
            abrir_arquivo = ok
            ler_arquivo = ok
            criar_arquivo = ok
            to_string = ok
            fechar_arquivo = ok
            run_criar_arquivo = ok
            run_ler_arquivo = ok

Classe: Maça
    Métodos: __init__ = ok
            to_string = ok

Classe: Cesta
    Métodos: __init__ = ok
            encher_cesta = ok
            to_string = ok
"""
