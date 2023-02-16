class Estudiante:
    def __init__(self, nombre, apellido, prom):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__prom = prom

    def getNOmbre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getProm(self):
        return self.__prom

    def valorColegiatura(nombre, apellido, prom):
        print("El valor de la colegiatura sin IVA es de $100 ")
        colegiatura = 100

        if prom >= 9:
            print(f"{nombre} {apellido}, Su promedio es mayor {prom}, no se le cobra IVA y tiene un descuento de 30%")
            desc = (100 * 30) / 100
            print(f"El pago de su colegiatura es de: ${colegiatura-desc}")

        else:
            print(f"{nombre} {apellido}, Su promedio es menor a 9, se le cobra IVA ")
            iva = (colegiatura * 10) / 100
            print(f"El pago de su colegiatura es de: ${colegiatura+iva}")