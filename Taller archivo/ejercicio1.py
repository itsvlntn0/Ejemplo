
def lectura():
    with open('informe.csv', 'r') as csv:
        datos = csv.readlines()
        return datos


def escribir():
    with open('analisis_archivo.csv', 'w') as csv:
        lista = []
        lista = lectura()
        mostrar = []

        for i in range(len(lista)-1):
            linea = lista[i].split(",")
            if i > 0:
                total = (int(float(linea[2])) - int(float(linea[3]))) / 2
            if i > 0 and int(float(linea[4])) - int(float(linea[1])) > 0:
                comportamiento = "SUBE"
                dato = linea[0] + "     " + \
                    comportamiento + "     " + str(total)
            elif i > 0 and int(float(linea[4])) - int(float(linea[1])) < 0:
                comportamiento = "BAJA"
                dato = linea[0] + "     " + \
                    comportamiento + "     " + str(total)
            elif i > 0 and int(float(linea[4])) - int(float(linea[1])) == 0:
                comportamiento = "ESTABLE"
                dato = linea[0] + "     " + \
                    comportamiento + "     " + str(total)
            else:
                dato = linea[0] + "     "
            mostrar.append(dato)
        mostrar[0] = "Fecha     Comportamiendo de la accion     Punto medio HIGH - LOW"

        for i in mostrar:
            csv.write(i + '\n')


def detalles():
    with open('analisis_archivo.csv', 'r') as csv:
        lectura = csv.readlines()

        lista1 = lectura

        for i in range(len(lista1)):

            linea = lista1[i]
            datos = linea.split('   ')
            mayor = 0

            if i > 1 and float(datos[2].strip()) > mayor:
                mayor = float(datos[2])
                fecha_mayor = datos[0]

        minimo = mayor

        for i in range(len(lista1)):

            linea = lista1[1]
            datos = linea.split('   ')
            if i > 1 and float(datos[2].strip()) < minimo:
                minimo = float(datos[2])
                fecha_minimo = datos[0]

    sube = 0
    baja = 0
    estable = 0

    for i in range(len(lista1)):
        linea = lista1[i]
        datos = linea.split('   ')

        if datos[1].strip() == "SUBE":
            sube += 1

        if datos[1].strip() == "BAJA":
            baja += 1

        if datos[1].strip() == "ESTABLE":
            estable += 1

    datos = {"date_lowest_price": fecha_minimo, "lowest_price": minimo, "date_highest_price": fecha_mayor,
             "highest_price": mayor, "cantidad_veces_sube": sube, "cantidad_veces_baja": baja, "cantidad_veces_estable": estable}

    with open('detalles.json', 'w') as leer:

        lista = list(str(datos))
        json = ""
        lista[0] = "{   \n"

        lista[len(lista)-1] = "\n}"

        for i in range(len(lista)):

            if "'" == lista[i]:
                posicion = lista.index(lista[i])
                lista[posicion] = '"'

            if "," == lista[i]:
                posicion = lista.index(lista[i])
                lista[posicion] = ',    \n'
            
            json += lista[i]

        leer.write(json)

lectura()
escribir()
detalles()