#7
#Define la clase Car en Python 3. La clase tendrá como atributos “matrícula” (numérica) y “color”. Crea un metodo imprimir y, además, dos métodos adicionales que elijas.

class Car:
    matricula = 12312313,
    color = "white"
    def __init__(self, matricula, color):
        self.matricula = matricula
        self.color = color
    def get_matricula(self):
        return self.matricula
    def get_color(self):
        return self.color
    def to_string(self):
        print(f"La matricula es: {self.get_matricula()}  y el color es: {self.get_color()}")

def main():
    car1 = Car(123123, "red")
    #print(car1.matricula)
    car2 = Car("sasd","azul")
    car1.to_string()
    car2.to_string()

if __name__ == "__main__":
    main()

