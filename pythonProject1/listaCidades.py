

cidades = ('Rio de Janeiro','São Paulo', 'Salvador')

cidadeVerificador = input('Digite o nome de uma cidade: ')

for i in range(len(cidades)):
    if  cidades[i] == cidadeVerificador:
        print('A sua cidade esta na lista')
        break
else:
    print("A sua cidade não esta na lista")

