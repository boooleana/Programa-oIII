criar = True  #  se for preciso criar o arquivo
inserir = False  #  se quando for o arquivo o usuario for inserir dados

if criar:
    arq = open('arquivo.txt', 'w')

    if inserir:
        texto = ""
        ## Criar arquivo
        for i in range(1,4):
            print("\nInsira os valores da maça " + str(i) + "\n")
            tipo = input("Tipo: ")
            pais = input("País de Origem: ")
            cor = input("Cor: ")
            texto += tipo + " " + pais + " " + cor + " \n"
    else:
        texto = """Fuji Brasil Vermelha
                   Gala Colombia Verde
                   Fuji Chile Vermelha"""
    arq.write(texto)

    arq.close()



## Leitura de arquivo

arq = open('arquivo.txt', 'r')

lista = []
texto = arq.readlines()
for string in texto:
    lista.append(string.split()) #lista de maças

arq.close()


#exibir maças


for maca in lista:
    fruta = ""
    for caracteristicas in maca:
        fruta += caracteristicas + " "
    print(fruta)
