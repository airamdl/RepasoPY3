#Airam de León
def sumar(num1, num2):
    sum = num1 + num2
    return sum

num1 = 14
num2 = 65
result = sumar(num1, num2)
print("La suma de", num1, "y", num2, "es:", result)

#Reciban una lista y modifiquen esa misma lista (referencia) duplicando los valores de todos los elementos. No debe devolver nada.
def duplicate(list):
    for i in range(len(list)):
        list[i] *= 2

list = [1, 2, 3, 4]
duplicate(list)
print(list)

#Reciban una lista y devuelvan una copia de esa misma lista (referencia) duplicando los valores de todos los elementos. La lista original no debe modificarse.

def duplicate2(list2):
    for i in range(len(list2)):
        list2[i] *= 2

list2 = [1, 2, 3, 4]
new_list = duplicate2(list2)
print(new_list)
print(list2)