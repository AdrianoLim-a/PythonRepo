from buscarMenor import buscarMenor

def ordenacaoPorSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscarMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr


print(ordenacaoPorSelecao([5,3,6,2,10]))