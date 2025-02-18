
def dobro(i):
    return i*2

def quadradro(i):
    return dobro(i)**2

numUser = int(input('Digite um número: '))

print(f'O dobro de {numUser} é {dobro(numUser)} e o quadrado de {dobro(numUser)} é {quadradro(numUser)}')