#7 Airam
#Define la clase Car en Python 3. La clase tendrá como atributos “matrícula” (numérica) y “color”. Crea un metodo imprimir y, además, dos métodos adicionales que elijas.
import random


class Car:

    def __init__(self, matricula, color, marca, precio):
        self.matricula = matricula
        self.color = color
        self.marca = marca
        self.precio=precio
    def get_matricula(self):
        return self.matricula
    def get_color(self):
        return self.color
    def get_marca(self):
        return self.marca
    def get_precio(self):
        return  self.precio
    def to_string(self):
        print(f"Los datos del vehiculo son: La matricula: {self.get_matricula()}  El color: {self.get_color()}  La marca: {self.marca}   El precio: {self.precio}")

def main():
    # car1 = Car("123123aa", "red", "audi", 67500)
    # car2 = Car("1213sasd","azul", "Seat", 14500)
    # car1.to_string()
    # car2.to_string()
    colores = ["red", "white", "black", "pink", "blue"]
    marcas = ["Audi", "Bmw", "Seat", "Opel", "Renault"]
    n = int(input("Introduce el número de coches que quieres crear: "))

    coches = []
    for i in range(1, n + 1):
        color = random.choice(colores)
        marca = random.choice(marcas)
        precio = random.randint(5000 , 200000)
        coche = Car(i, color, marca, precio)
        coches.append(coche)
        if i <=10:
            coche.to_string()


if __name__ == "__main__":
    main()

