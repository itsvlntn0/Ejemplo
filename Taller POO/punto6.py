class laboratorio:

    def __init__(self, nombre, sexo, hemoglobina, edad, tipo):

        self.__nombre = nombre
        self.__sexo = sexo
        self.__hemoglobina = hemoglobina
        self.__edad = edad
        self.__tipo = tipo

    def getNombre (self):
        return self.__nombre
    
    def getSexo (self):
        return self.__sexo
    
    def getHemoglobina (self):
        return self.__hemoglobina

    def getEdad (self):
        return self.__edad
    
    def getTipo (self):
        return self.__tipo

    def analisisClinicos(nombre, sexo, hemoglobina,edad, tipo):

        if edad > 0 & edad < 1 & tipo == 1:

            if hemoglobina > 12 & hemoglobina < 27:

                print(f"El resultado del paciente {nombre} es negativo")
            
            elif hemoglobina < 13:
                print(f"El resultado del paciente {nombre} es positivo")
        
        elif edad > 1 & edad < 7 & tipo == 1:

            if hemoglobina > 9 & hemoglobina < 19:

                print(f"El resultado del paciente {nombre} es negativo")
            
            elif hemoglobina < 10:

                print(f"El resultado del paciente {nombre} es positivo")

        elif edad > 6 & edad < 13 & tipo == 1:

            if hemoglobina > 10 & hemoglobina < 16:

                print(f"El resultado del paciente {nombre} es negativo")
            
            elif hemoglobina < 11:

                print(f"El resultado del paciente {nombre} es positivo")

        elif edad > 1 & edad < 6 & tipo == 2:

            if hemoglobina >= 11.5 & hemoglobina < 16:

                print(f"El resultado del paciente {nombre} es negativo")

            elif hemoglobina < 11.5:
                
                print(f"El resultado del paciente {nombre} es positivo")

        elif edad > 5 & edad < 11 and tipo == 2:

            if hemoglobina >= 12.6 &hemoglobina <= 15.5:

                print(f"El resultado del paciente {nombre} es negativo")

            elif hemoglobina < 12.6:

                print(f"El resultado del paciente {nombre} es positivo")

        elif edad > 10 & edad < 16 & tipo == 2:

            if hemoglobina > 14 & hemoglobina <= 15.5:

                print(f"El resultado del paciente {nombre} es negativo")

            elif hemoglobina < 13:

                print(f"El resultado del paciente {nombre} es positivo")

        elif sexo == 1 & edad > 15 & tipo == 2:

            if hemoglobina > 11 & hemoglobina < 17:

                print(f"El resultado del paciente {nombre} es negativo")
            
            elif hemoglobina < 12:

                print(f"El resultado del paciente {nombre} es positivo")

        elif sexo == 2 & edad > 15 & tipo == 2:

            if hemoglobina > 13 & hemoglobina < 19:

                print(f"El resultado del paciente {nombre} es negativo")
            
            elif hemoglobina < 14:

                print(f"El resultado del paciente {nombre} es positivo")

