class Hipoteca:
    
    def __init__(self, nombre, casa):
        self.__nombre = nombre
        self.__casa = casa

    def getNombre (self):
        return self.__nombre

    def getValCasa(self):
        return self.__casa

    def valHipoteca(nombre, casa):
        hipoteca = casa * 0.70
        print(f"El banco le presta por su casa: ${hipoteca}")
        if hipoteca < 100000000:
            print(f"{nombre}, este es el monto que se depositara en su cuenta bancaria")
            print(f"Usted invertira el 50% de su hipoteca, que es: ${hipoteca / 2}")