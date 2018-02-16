status = True

lista = ["a) mitos e lendas indígenas provocaram mudanças na cultura religiosa portuguesa do século XVI, em Portugal.",
         "b) a pesca, a caça e os frutos do Brasil serviram como base alimentar na culinária colonial luso-brasileira.",
         "c) o uso do algodão entre os nativos brasileiros para a fabricação de redes foi reutilizado pelos colonos portugueses para a confecção de tecidos rústicos.",
         "d) o cultivo entre algumas tribos brasileiras de frutas, milho e tubérculos foi rapidamente incorporado à agricultura de subsistência entre colonos portugueses.",
         "e) a cultura do fumo utilizada por nativos brasileiros tornou-se um dos hábitos culturais mais apreciados pelos europeus."]

busca = input("Insira uma palavra para a busca: ")
print("")

while status:
    for i in lista:
        if busca in i:
            print(i)
            status = False
        else:
            print("Alternativa não encontrada.")
