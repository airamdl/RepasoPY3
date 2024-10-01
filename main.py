#Clonar una lista.
"""
list = ["hola", "pepe", "Roberto"]
list_backup = list.copy()

print(list)
print(list_backup)"""
#Añadir un elemento a una lista.
"""
list = ["hola", "pepe", "Roberto"]
list_backup = list.copy()

list.append("hola2")
print(list)
print(list_backup) """

#Quitar un elemento de una lista.
""" list = ["hola", "pepe", "Roberto"]
list_backup = list.copy()

list.append("hola2")
list.remove("hola")
print(list)
print(list_backup) """

#Crear una nueva lista con los 4 últimos elementos de una lista.
"""
list = ["hola", "pepe", "Roberto", "lista nueva1", "lista nueva2", "listanueva3", "listanueva4"]
list_backup = list.copy()
list_4= list[-4:]

list.append("hola2")
print(list)
print(list_4)
"""
#Convertir las palabras de una cadena (separadas por espacios) en una lista.
"""
cadena = "Hola soy airam y tu"
list = cadena.split()
print(list)
"""