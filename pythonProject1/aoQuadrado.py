import math
def aoQuadrado(i) :
   return math.pow(i, 2)

numeroUsuario = int(input('Digite um numero: '))

print(f'O quadrado de {numeroUsuario} é {aoQuadrado(numeroUsuario)}')
