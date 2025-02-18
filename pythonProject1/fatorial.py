
def fatorial(i):
    if i <=0:
        return 1
    else:
        return i*fatorial(i-1)


numeroUser = int(input('Digite um número: '))
print(f' O fatorial de {numeroUser} é {fatorial(numeroUser)}')