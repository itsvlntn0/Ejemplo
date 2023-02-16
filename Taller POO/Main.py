import punto1 as pt1
import punto2 as pt2
import punto3 as pt3
import punto4 as pt4
import punto5 as pt5
import punto6 as pt6

opcion = int(input("¿Que ejercico desea ver? "))

if opcion == 1:
    suma = int(input("Digite la suma de 2 indices de la lista"))
    objetivo = pt1.Numero(suma)
    lista = [10,20,10,40,50,60,70]
    print("Los numeros para hacer esta suma estan en los indices ",pt1.Numero.encontarIndices(lista,suma))

elif opcion == 2:
    nombre = input("Escriba su nombre ")
    apellido = input("Escriba su apellido ")
    prom = input("Escriba su ultimo promedio ")

    est = pt2.Estudiante(nombre, apellido, prom)
    print(pt2.Estudiante.valorColegiatura(nombre, apellido, prom))

elif opcion == 3:
    nombre = input("Escriba su nombre ")
    apellido = input("Escriba su apellido ")
    ingreso = int(input("¿De cuanto es su ingreso? "))
    casa = int(input("¿Cual es el valor de la casa? "))

    comp = pt3.Comprador(nombre,apellido,ingreso,casa)
    print(pt3.Comprador.pagos(nombre,apellido,ingreso,casa))

elif opcion == 4:
    nombre = input("Escriba su nombre ")
    salario = input("Ingrese su salario ")

    sal = pt4.Salud(nombre, salario)
    print(pt4.Salud.pagoSAR(nombre, salario))

    opc = int(input("¿Quiere ingresar un monto voluntario? 1) Si 2) No"))

    if opc == 1:
        print(pt4.Salud.pago_Voluntario(salario))
    elif opc == 2:
        print("Vuelva pronto, Adios.")
    else:
        print("Opcion no valida")

elif opcion == 5:
    nombre = input("Escriba su nombre ")
    valCasa = int(input("Ingrese el valor de la casa: "))
    hipo = pt5.Hipoteca(nombre, valCasa)
    print(pt5.Hipoteca.valHipoteca(nombre, valCasa))

elif opcion == 6:

    nombre = input("Escriba su nombre ")
    sexo = int(input("Sexo del paciente: 1)Femenino  2) Masculino "))
    hemoglobina = float(input("Nivel de hemoglobina del paciente: "))
    edad = int(input("Ingrese la edad del paciente"))
    tipo = int(input("¿La edad esta en mese o años? 1) meses 2) años"))

    resultados = pt6.laboratorio(nombre, sexo, hemoglobina, edad, tipo)
    print(pt6.laboratorio.analisisClinicos(nombre, sexo, hemoglobina, edad, tipo))