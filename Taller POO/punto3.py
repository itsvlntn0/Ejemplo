class Comprador:

    def __init__(self, nombre, apellido,ingreso,casa):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__ingreso = ingreso
        self.__casa = casa
    
    def getNOmbre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getIngreso(self):
        return self.__ingreso
    
    def getCasa(self):
        return self.__casa

    def pagos(nombre, apellido,ingreso,casa):
        if ingreso < 8000:
            enganche = (casa * 15) / 100
            sub = casa - enganche
            print(f"{nombre} {apellido}, el enganche de la casa es de: ${enganche}")
            print(f"Mensualemnte debera pagar: ${sub / 120}")

        else:
            enganche = (casa * 30) / 100
            sub = casa - enganche
            print(f"{nombre} {apellido}, el enganche de la casa es de: ${enganche}")
            print(f"Mensualemnte debera pagar: ${sub / 84}")