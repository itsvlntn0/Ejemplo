class Numero:

    def __init__(self,objetivo):
        self.__objetivo=objetivo
    
    def getObjetivo(self):
        return self.__objetivo

    def encontrarIndices(lista, suma):
        numeros_indices= {}

        for i , n in enumerate(lista):
            if suma - n in numeros_indices:
                return numeros_indices[suma - n], i

            numeros_indices[n] = i
