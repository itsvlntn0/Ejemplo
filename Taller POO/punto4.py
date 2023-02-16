class Salud:
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario

    def getNombre(self):
        return self.__nombre

    def getSalario(self):
        return self.__salario
    
    def pagoSAR(nombre, salario):
        print(f"{nombre}, el porcentaje obligatorio a ingresar es del 10% de su salario por el pago del SAR \n")
        desc = salario * (10/100)
        print(f"Se le descontara {desc} de su salario por el pago der SAR")
        print(f"Su nuevo salario es de: ${salario - desc}")

    def pago_Voluntario(salario):
        sub = salario -(salario * (10/100))
        opc = int(input("Elija una opcion: 1) Monto Fijo 2) Porcentaje del sueldo "))

        if opc == 1:
            monto = int(input("Ingrese el monto fijo que va ingresar a la cuenta: "))
            total = sub - monto
            print(f"Su salario final sera de: ${total}")

        elif opc == 2:
            monto = int(input("Ingrese el porcentaje que va ingresar a la cuenta: "))
            desc = sub * (monto / 100)
            total = sub - desc
            print(f"Su salario final sera de: ${total}")
        
        else:
            print("Elija una opcion valida")