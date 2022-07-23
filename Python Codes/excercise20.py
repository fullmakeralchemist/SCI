#AÑADIR Y OBTENER ELEMENTOS DE UN DICCIONARIO

elementos = {}

elementos['nombre'] = 'Cody' # Crea la llave

elementos['nombre'] = 'Codigo facilito' #Actualiza el valor que la llave almacena

print(elementos)
print(len(elementos))

###

"""
elementos = {'a': 1, 'b': 2, 'c': 3, 'a': 4}
print(elementos)
print(len(elementos))

"""

#OBTENER ELEMENTOS

"""
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print('a' in diccionario)

valor = diccionario['d']

print(valor)
"""

## PART II

"""
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print('z' in diccionario)
#get
valor = diccionario.get('z', 'la llave no existe') # coma en caso el valor no exita
print(valor)

"""

### PART3

"""
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print('z' in diccionario)
#setfedault
valor = diccionario.setdefault('e', 5) # coma en caso el valor no exita
print(valor)
print(diccionario)
"""

## PART 4

"""
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print('z' in diccionario)
#setfedault
valor = diccionario.setdefault('c', 5) # coma en caso el valor no exita
print(valor)
print(diccionario)

"""