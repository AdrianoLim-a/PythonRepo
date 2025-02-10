paises = {
    'Brasil': 'Brasília',
    'França': 'Paris',
    'Japão': 'Tóquio',
    'Canada': 'Ottawa',
    'Austrália': 'Canberra'
}

paisUsuario = input('Digite o nome de um país: ')

if paisUsuario in paises:
    capital = paises[paisUsuario]
    print(f'A Capital do pais {paisUsuario} é {capital}')
else:
    print('Desculpe, não temos a informação deste país.')