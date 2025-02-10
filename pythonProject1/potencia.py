


def potencia(based,expo=2):
    return based ** expo


baseUsuario = int(input('Digite o número base: '))
expoUsuario = input('Digite o número expoente (default 2):')

if expoUsuario:
    print(f'O resultado é: {potencia(baseUsuario,int(expoUsuario))}')
else:
    print(f'O resultado é: {potencia(baseUsuario)}')

print(potencia(baseUsuario, expoUsuario))