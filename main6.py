#6


#Crea una lista en la cual cada elemento de esa lista sea una lista con dos valores: tamaño y peso.
dic1 = {
  "Tamaño": "1.92",
  "Peso": "127"
}
dic2 = {
    "Tamaño": "1.90",
    "Peso": "106"
}
list= [dic1,dic2]

print(list)

#Utilizando Key functions, haz que esta lista se ordene por mayor altura y, en caso de igualdad, por menor peso.
dic3 = {
  "Tamaño": "1.94",
  "Peso": "127"
}
dic4 = {
    "Tamaño": "1.93",
    "Peso": "106"
}
list2 = [dic3,dic4]

def sort_heigth(people):
    return -float(people["Tamaño"]), float(people["Peso"])

sorted_list = sorted(key=sort_heigth(list2))

print(sorted_list)