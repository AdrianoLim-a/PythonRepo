
#funciona apenas em listas sequênciais
def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    print(alto)
    while baixo <= alto:
        meio = int((baixo + alto) / 2)
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


minha_lista = [5, 2, 150, 25,14,45,46, 41, 23]


print(pesquisa_binaria(minha_lista, 45))
print(pesquisa_binaria(minha_lista, -0))