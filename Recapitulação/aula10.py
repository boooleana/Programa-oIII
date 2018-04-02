arq = open('rh.csv', 'r')
dados = arq.read ()
arq.close ()
linhas = dados.splitlines()

a = []

for i in linhas:
    a.append(i.split(";"))


masc = 0
fem = 0
masc_anos = 0
fem_anos = 0


#inserção de qtd de mulheres ou homens e anos de estudo

for i in a:
    if str(i[2]) != " ":
        if str(i[0]) == "Masculino":
            masc += 1
            masc_anos += int(i[2])
        elif str(i[0]) == "Feminino":
            fem += 1
            fem_anos += int(i[2])

# média
mi_fem = fem_anos/fem
mi_masc = masc_anos/masc


#desvio padrão

sigma_fem = 0
sigma_masc = 0

for i in a:
    if str(i[2]) != " ":
        if str(i[0]) == "Masculino":
            sigma_masc += (int(i[2])-int(mi_masc))**2
        elif str(i[0]) == "Feminino":
            sigma_fem += (int(i[2])-int(mi_fem))**2

sigma_fem = (sigma_fem/fem)**(1/2)
sigma_masc = (sigma_masc/masc)**(1/2)

print(sigma_fem)
print(sigma_masc)

