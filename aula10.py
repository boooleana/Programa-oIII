arq = open('aula10_arquivo.csv', 'r')
dados = arq.read ()
arq.close ()
linhas = dados.splitlines()
for linha in linhas:
    print(linha)

bd = []
string_tmp = ''

for j in linha:
    tmp = []
    for i in j:
        if j != ';':
            string_tmp += j
        else:
            tmp.append(string_tmp)
            string_tmp = ''
        
        bd.append(tmp)

print(bd)
