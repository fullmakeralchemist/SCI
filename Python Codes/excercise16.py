#LISTAS Y TUPLAS

#Si los elementos no cambiaran usaremos tuplas y en caso contrario listas
#Generar tuplas apartir de listas o caso contrario 


cursos = ['Python', 'Flask', 'Django']

cursos_tupla = tuple(cursos)

print(cursos_tupla)
print(type(cursos_tupla))

niveles = ('Basico', 'Intermedio', 'Avanzado')

niveles_lista = list(niveles)

print(niveles_lista)
print(type(niveles_lista))