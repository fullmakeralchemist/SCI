#DICCIONARIOS

#Los diccionarios contienen llaves para cada valor
#Una llave puede ser cualquier objeto inmutable en python

diccionario = {}

diccionario = dict()

## { } llave : el valor el cual queremos asociar 

diccionario = { "Total": 55}

diccionario = { "Total": 55, "descuento": True, "subtotal": 15}

print(diccionario)

#PART II

"""
diccionario = {"total": 55, 10: "Curso de Python", (1,2,3): True}

# Llaves 

# Un String ("total") 
# un numero entero 10 
# una tupla que almacena numeros enteros

"""

# PART III

"""
usuario = {
    'nombre' : 'nombre de usuario',
    'edad' : 23,
    'curso' : 'Curso de Python',
    'skills' : {
        'programacion' : True,
        'base de datos' : False
    },
    'medallas' : ['basico', 'intermedio']
}
"""


#

"""
# Para hacer cualquier modificacion en el diccionario haremos el uso de corchetes

#Creacion del diccionario 
diccionario = dict()

#Agregar nueva llave valor
diccionario['usuario'] = 'eduardo'

#Actualizar valor mediante una llave
diccionario['usuario'] = 'eduardo_1erp'

# Obtener valor mediante una llave
print(diccionario['usuario'])
"""

###
"""
diccionario = {'Eduardo': 1, 'Fernando': 2, 'Uriel': 3, 'Rafael': 4}

diccionario.keys()
"""


####


"""
diccionario.values()
"""

###

"""
for key, value in diccionario.items():
  print(key, value)
"""