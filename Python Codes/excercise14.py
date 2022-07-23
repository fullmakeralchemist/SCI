#MODIFICAR LISTAS
lista_cursos = ['Python', 'Java', 'Django', 'Flask', 'Ruby']
lista_cursos_dos = ['C++', 'C', 'Matlab']
print(len(lista_cursos))

lista_cursos.append('MongoDB')

lista_cursos.insert(1, 'Rails')

lista_cursos.extend(lista_cursos_dos)
print(lista_cursos)
print(len(lista_cursos))

lista_cursos.remove('MongoDB')
print(lista_cursos)

# PART II

"""
lista_cursos = ['Python', 'Java', 'Django', 'Flask', 'Ruby']
lista_cursos_dos = ['C++', 'C', 'Matlab']
print(len(lista_cursos))

lista_cursos.append('MongoDB')

lista_cursos.insert(1, 'Rails')

lista_cursos.extend(lista_cursos_dos)
print(lista_cursos)
print(len(lista_cursos))

del lista_cursos[0]
print(lista_cursos)
"""


#PART III

"""
lista_cursos = ['Python', 'Java', 'Django', 'Flask', 'Ruby']
lista_cursos_dos = ['C++', 'C', 'Matlab']
print(len(lista_cursos))

lista_cursos.append('MongoDB')

lista_cursos.insert(1, 'Rails')

lista_cursos.extend(lista_cursos_dos)
print(lista_cursos)
print(len(lista_cursos))

lista_cursos.clear()
print(lista_cursos)
"""