def lectura():
    with open ('covid.csv', 'r') as csv:
        datos = csv.readlines()
        return datos

def insertar():
    with open('covid.csv','a')as csv:
        documento = input("Digite su numero de documento: ")
        nombre = input("Digite sus nombres: ")
        apellido = input("Digite sus apellidos: ")
        correo = input("Digite su correo: ")
        celular = input("Digite su numero telefonico: ")
        genero = input("Digite su genero: ")
        edad = int(input("Digite su edad: "))
        rh = input("Digite su tipo de sangre: ")
        covid =input("¿Tiene Covid? Si / No: ")
        
        if(covid == 'Si'):
            casa = input("¿Se encuentra en su casa? Si No: ")
            if (casa == 'No'):
                hospital = input("¿Se encuentra en el hospital? Si No: ")
        
                
        
        cont = 0 
        lista = []
        

        if len(lista) > 0:

            for i in lista:
                if i.strip() == documento:
                    cont+=1
                    if cont>0:
                        print("El registro ya existe")

                else:
                    if covid == 'Si':
                        covid = 'True'
                        if casa =='Si':
                            hospital = "False"
                            casa = "True"
                            csv.write (documento + ", ")
                            csv.write (nombre + ", ")
                            csv.write (apellido + ", ")
                            csv.write (correo + ", ")
                            csv.write (celular + ", ")
                            csv.write (genero + ", ")
                            csv.write (str(edad) + ", ")
                            csv.write (rh + ", ")
                            csv.write (str(covid) + ',')
                            csv.write (casa + ", ")
                            csv.write (hospital + "\n")
                            lista = lectura()
                        elif casa == 'No':
                            hospital = "True"
                            casa = "False"
                            csv.write (documento + ", ")
                            csv.write (nombre + ", ")
                            csv.write (apellido + ", ")
                            csv.write (correo + ", ")
                            csv.write (celular + ", ")
                            csv.write (genero + ", ")
                            csv.write (str(edad) + ", ")
                            csv.write (rh + ", ")
                            csv.write (str(covid) + ',')
                            csv.write (casa + ", ")
                            csv.write (hospital + "\n")
                            lista = lectura()
                    else:
                        covid = 'False'
                        casa = "False"
                        hospital = "False"
                        csv.write (documento + ", ")
                        csv.write (nombre + ", ")
                        csv.write (apellido + ", ")
                        csv.write (correo + ", ")
                        csv.write (celular + ", ")
                        csv.write (genero + ", ")
                        csv.write (str(edad) + ", ")
                        csv.write (rh + ", ")
                        csv.write (str(covid) + ',')
                        csv.write (casa + ", ")
                        csv.write (hospital + "\n")
                        lista = lectura()

        else:
            if covid == 'Si':
                covid = 'True'
                if casa =='Si':
                    casa = "True"
                    hospital = "False"
                    csv.write (documento + ", ")
                    csv.write (nombre + ", ")
                    csv.write (apellido + ", ")
                    csv.write (correo + ", ")
                    csv.write (celular + ", ")
                    csv.write (genero + ", ")
                    csv.write (str(edad) + ", ")
                    csv.write (rh + ", ")
                    csv.write (str(covid) + ',')
                    csv.write (casa + ", ")
                    csv.write (hospital + "\n")
                elif casa == 'No':
                    casa = "False"
                    hospital =" True"
                    csv.write (documento + ", ")
                    csv.write (nombre + ", ")
                    csv.write (apellido + ", ")
                    csv.write (correo + ", ")
                    csv.write (celular + ", ")
                    csv.write (genero + ", ")
                    csv.write (str(edad) + ", ")
                    csv.write (rh + ", ")
                    csv.write (str(covid) + ',')
                    csv.write (casa + ", ")
                    csv.write (hospital + "\n")
                
            else:
                covid = 'False'
                csv.write (documento + ", ")
                csv.write (nombre + ", ")
                csv.write (apellido + ", ")
                csv.write (correo + ", ")
                csv.write (celular + ", ")
                csv.write (genero + ", ")
                csv.write (str(edad) + ", ")
                csv.write (rh + ", ")
                csv.write (str(covid) + ',')
                csv.write (casa + ", ")
                csv.write (hospital + "\n")
                        

def escribir():
    with open ('Covid_hospitalizados.csv', 'w') as csv:

        lista = []
        lista = lectura()
        mostrar = []
        mostrar.append( "Documento    Nombre      Apellido        Covid       Estado")
        for i in range(len(lista)):
            linea = lista[i].split(",")
    
            if i > 0 and linea[8] != "False":
                if linea[9] == "False":
                    estado = "Hospitalizado"
                    dato = linea[0] +"      " + linea[1] +"      " + linea[2] +"      " + linea[8] +"      " + estado
                else:
                    estado = "En casa"
                    dato = linea[0] +"      " + linea[1] +"      " + linea[2] +"      " + linea[8] +"      " + estado 
            else:
                estado = "En casa"
                dato = linea[0] +"      " + linea[1] +"      " + linea[2] +"      " + linea[8] +"      " + estado

            lineas = dato.split("      ")
            if lineas[4] == "Hospitalizado":
                mostrar.append(dato)
        
        for i in mostrar:
            csv.write(i + "\n")
                



def edades():
    with open ('Covid_edades.csv', 'w') as csv:
        lista = []
        lista = lectura()
        mostrar = []
        j = 0
        k = 0
        l = 0
        x = 0
        y = 0
        z = 0

        for i in range(len(lista)):
            linea = lista[i].split(",")
    
            if i > 0 and int(linea[6]) < 6:
                j += 1
                dato = "Menores de 6: " + str(j)
            elif i > 0 and int(linea[6]) > 5 and int(linea[6]) < 13:
                x += 1
                dato = "Entre 6 y 12 años: " + str(x)
            elif i > 0 and int(linea[6]) > 12 and int(linea[6]) < 19:
                y += 1
                dato = "Entre 13 y 18 años: " + str(y)
            elif i > 0 and int(linea[6]) > 18 and int(linea[6]) < 41:
                l += 1
                dato = "Entre 19 y 40 años: " + str(l)
            elif i > 0 and int(linea[6]) > 59 and int(linea[6]) < 80:
                k += 1
                dato = "Entre 60 y 80 años: " + str(k)
            else:
                z += 1
                dato = "Mayores de 80 años: " + str(z)

            mostrar.append(dato)
        mostrar [0] = "Cantidad de personas por edades"
        for i in mostrar:
            csv.write(i + '\n')



def covid_Doce():
    with open ('CovidMenoresDoce.csv', 'w') as csv:
        cont = 0
        lista = []
        lista = lectura()
        mostrar = []
        

        for i in range(len(lista)):
                linea = lista[i].split(",")

                if i > 0 and int(linea[6]) > 12:
                    cont +=1
                else:
                    if linea[8] != "False":
                        dato = linea[0] +"      " + linea[1] +"         " + linea[2] +"         " + linea[6] 
                 
               
                        mostrar.append(dato)
        mostrar[0] = ("Niños menores de 12 con covid")
        for i in mostrar:
            csv.write(i + '\n')

edades()
    
def contar():
    with open ('ContarHospitalizados.csv', 'w') as csv:

        x = 0
        lista = []
        lista = lectura()
        mostrar = []
        mostrar.append( "Catidad Hospitalizados: ")
        for i in range(len(lista)):
            linea = lista[i].split(",")

            if i > 0 and linea[8] != "False":
                if linea[9] == "False":
                    x += 1
                    
                else:
                    x = 0
            else:
                x -= 1

            if x > 0:
                mostrar.append(str(x))
        
        for i in mostrar:
            csv.write(i + "\n")
        
contar()
