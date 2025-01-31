

def lista_ordenada(dicionario):
    return sorted(dicionario, key=dicionario.get, reverse=True)


meu_dicionario = {
    "radiohead":100,
    "linkin park": 200,
    "the black keys": 10,
    "beck": 150
}

print(lista_ordenada(meu_dicionario))