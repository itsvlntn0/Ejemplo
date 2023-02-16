import numpy as np
import random

def punto1():
    arreglo = np.ones([5,2])
    cont = 0

    for f in range (5):
        for c in range (2):

            arreglo[f,c]= random.randint(0, 5)

    num = int(input("Digite un numero entre el 0 y el 5: "))

    for f in range(5):
        for c in range(2):

            if num == arreglo[f,c]:
                cont +=1

    print(arreglo)
    print(f'El numero que ingresaste se repite {cont} veces.')


def punto2():
    cant= int(input("Digite la cantidad de numeros que va a ingresar: "))

    arreglo = np.zeros([cant])
    numeros = []

    for i in range (cant):
        repeticion = True

        while(repeticion):
            num = int(input("Digite un numero entre el 0 y el 1000: "))
            if(num >= 0 and num <= 1000):
                arreglo[i] = num
                numeros.append(num)
                repeticion = False
                    

    print(f'Este es el numero menor {min(numeros)} y este el mayor {max(numeros)}')

def punto3():
    lista = []
    n = 0

    while n < 100:

        n += 1
        cont = 1
        i = 1

        while cont <= n :

            if n % cont == 0:
                i += 1
        
        if i == 2:
            lista.append(n)

    arreglo = np.zeros([len(lista)])

    for a in range (len(lista)):
        for b in range(len(arreglo)):
            if ( a == b):
                arreglo[b] = lista[a]

    print(arreglo)


def punto4():

    arreglo = np.ones([5,2])
    cont = 0

    for f in range (5):
        for c in range (2):

            arreglo[f,c]= random.randint(0, 10)

    num = int(input("Digite un numero: "))

    for f in range(5):
        for c in range(2):

            if num == arreglo[f,c]:
                cont +=1

    
    if cont != 0:
        print(f'El numero que ingresaste se repite {cont} veces.')
    else:
        print("El numero no se encontro")
    print(arreglo)


def punto5():

    arreglo = np.zeros([5,5])
    i = 0

    for f in range (5):
        for c in range (5):
            arreglo[f,c]= random.randint(0, 100)
    
    for f in range (5):
        for c in range (5):
            i += arreglo[f,c]

    print(arreglo)
    print(i)


def punto6():
    arreglo = np.zeros([10])
    lista = []

    for f in range (10):
        arreglo[f]= int(input("Digite un numero: "))
    
    for i in arreglo:
        if i % 2 == 0:
            lista.append(i)

    print(arreglo)
    print(lista)    

def punto7():

    arreglo = np.zeros([5])
    i = 0

    for f in range (5):
            arreglo[f]= float(input("Digite una nota: "))
    
    for f in range (5):
        i += arreglo[f]

    total = i / 5
    print(arreglo)
    print(f'Este es el promedio de las notas: {total}')


def punto8():
    cant = int(input("¿Cuantos atletas van a participar? "))

    arreglo = np.zeros([cant])

    for i in range (cant):
        time = int(input("Digite el tiempo del competidor: "))
        arreglo[i] = time

    print(f'El mejor tiempo fue : {min(arreglo)}')

def punto9():

    cant = int(input("¿cuantos numeros va a digitar?: "))
    arreglo = np.zeros([cant])
    i = 0

    for f in range (cant):
        num = int(input("Digite un numero: "))
        arreglo[f]= num
    
    for f in range (cant):
        i += arreglo[f]

    print(arreglo)
    print(i)

def punto10():

    numero = []

    for c in range (1,100):
        if c % 3 == 0:
            numero.append(c)

    arreglo = np.zeros([len(numero)])

    for a in range(len(numero)):
        for b in range(len(arreglo)):
            if(a == b):
                arreglo[b] = numero [a]
    
    print(arreglo)

def punto11():

    i = 0 
    lista = []
    pares = []
    impares = []

    while i < 10:

        doc = int(input("Ingrese el numero de su documento: "))
        usuario = input("Ingrese su usuario: ")
        lista.append(doc)

        i += 1

    
        if doc % 2 == 0:
            pares.append(doc)
        else:
            impares.append(doc)

    elegir = int(input("¿Qué documentos desea ver? 1.PARES 2. IMPARES "))

    if elegir == 1:
        print(pares)
    else:
        print(impares)

def punto12():
    arreglo = np.zeros([2,10])
    i = 0

    for f in range (2):
        for c in range (10):
            arreglo[f,c]= random.randint(0, 100)

    num = int(input("Digite un numero: "))

    for f in range (2):
        for c in range (10):
            if num == arreglo[f,c]:
                print(f'El numero {num} se encontro')
            else:
                print(f'El numero {num} no se encontro')

    print(arreglo)

#def punto13():

def punto14():

    num1 = int(input("Digite un numero: "))
    num2 = int(input("Digite un numero: "))
    
    a = max(num1, num2)
    b = min(num1, num2)

    while b:
        mcd = b
        b = a % b
        a = mcd
    
    mcm =  (num1 * num2) // mcd

    print('El Minimo comun multiplo de {0} y {1} es {2}'.format(num1, num2, mcm))

#def punto15():

def punto16():

    arreglo = np.zeros([10])
    par = []
    impar = []
    x = 0

    for f in range (10):
        num = int(input("Digite un numero: "))
        arreglo[f]= num

    while x < 10:
        if arreglo[x] % 2 == 0:
            par.append(arreglo[x])
            
        if arreglo[x] % 2 != 0:
            impar.append(arreglo[x])
        
        x += 1

    par.extend(impar)

    print(par)


opcion = int(input("¿Digite el número del punto que quiere ver? "))

if opcion == 1:
    punto1()
elif opcion == 2:
    punto2()
elif opcion == 3:
    punto3()
elif opcion == 4:
    punto4()
elif opcion == 5:
    punto5()
elif opcion == 6:
    punto6()
elif opcion == 7:
    punto7()
elif opcion == 8:
    punto8()
elif opcion == 9:
    punto9()
elif opcion == 10:
    punto10()
elif opcion == 11:
    punto11()
elif opcion == 12:
    punto12()
#elif opcion == 13:
    #punto13()
elif opcion == 14:
    punto14()
#elif opcion == 15:
    #punto15()
elif opcion == 16:
    punto16()
else:
    print("Opcion no valida")