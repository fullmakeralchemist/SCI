#Concatenar

nombre = 'Jose Eduardo'
apellido = 'Padron'

#nombre_completo = nombre + ' ' + apellido
nombre_completo = 'Mr. %s %s.' %(nombre, apellido)
print(nombre_completo)


# PART II
"""
nombre = 'Jose Eduardo'
apellido = 'Padron'

nombre_completo = 'Mr. {} {}.'.format(nombre, apellido)

print(nombre_completo)
"""
# PART III
"""
nombre = 'Jose Eduardo'
apellido = 'Padron'

nombre_completo = 'Mr. {nombre} {primer_apellido} {segundo_apellido} .'.format(
    nombre=nombre,
    primer_apellido=apellido,
    segundo_apellido='perez'
)

print(nombre_completo)
"""