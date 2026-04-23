 # TRABAJO PRACTICO - LISTAS

# ACTIVIDADES:

# PRIMER EJERCICIO:

print("\n")
print("PRIMER EJERCICIO:\n")

notas = [6, 7, 8, 9, 10, 10, 3, 4, 2, 4]
num = 0
promedio = 0
mayor = 0
menor = 10

for i in notas:
    num += 1
    promedio += i
    print(f"Notas de estudiante {num}: {i}")
    if i >= mayor:
        mayor = i
    if i <= menor:
        menor = i
print("")
print(f"El promeeio es de: {promedio/len(notas)}\n")
print(f"Nota mas baja: {menor}")
print(f"Nota mas alta: {mayor}")


# SEGUNDO EJERCICIO:

print("\n")
print("SEGUNDO EJERCICIO:\n")

lista = []
num = 0
menu = True

for a in range(1,5+1):
    print("Ingrese sus productos (no más de 5).")
    productos = input(f"Producto {a}: ")
    lista.append(productos)

ordenados = sorted(lista)

print("")
for e in ordenados:
    num += 1
    print(f"Producto {num}: {e}")

while menu:
    print("")
    eliminar = input("Que producto desea eliminar: ")
    if eliminar in ordenados:
        ordenados.remove(eliminar)
        menu = False
    else:
        print("El producto no existe.\n")
    
print("")
print(f"Productos: {ordenados}")


# TERCER EJERCICIO:

print("\n")
print("TERCER EJERCICIO:\n")


import random 
lista = []
num = 0
pares = []
impares = []

for i in range(15):
    num = random.randint(1,100)
    lista.append(num)
    if (num % 2) == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"Lista: {lista}\n")
print(f"Lista de pares: {pares}")
print(f"Lista de inpares: {impares}\n")
print(f"Cantidad de númeors en la lista de pares: {len(pares)}")
print(f"Cantidad de númeors en la lista de impares: {len(impares)}") 

# CUARTO EJERCICIO:

print("\n")
print("CUARTO EJERCICIO:\n")

lista = [1, 3, 5, 3, 7, 1, 9, 5, 3]
nueva_lista = []

for i in (lista):
    if i not in nueva_lista:
        nueva_lista.append(i)

print(f"Lista: {lista}")
print(f"Nueva lista: {nueva_lista}")

# QUINTO EJERCICIO:

print("\n")
print("QUINTO EJERCICIO:\n")

lista = ["Federico", "Alejo", "Bautista", "Carlos", "Dante", "Eduardo", "Gabriela", "Hida"]
nuevo_alumno = []
eliminado = []
num = 0
menu = True

print("Alumnos:")

for i in lista:
    num += 1
    print(f"{num}. {i}")

while menu:
    print("")
    print("¿Quiere eliminar o agregar un alumna/o?\n\n 1. Agregar.\n 2. Eliminar.\n")
    usuario = input("Ingrese el número: ")
    
    if usuario == "1":
        nuevo_alumno = input("Ingrese el alumno/a: ")
        print("")
        lista.append(nuevo_alumno)
        menu = False
        print("Nueva lisa actualizada:\n")
        for j in lista:
            num = 0
            num += 1
            print(f"{num}. {j}")

    elif usuario == "2":
        eliminado = input("Alumna/o desea eliminar:").title()
        print("")
        if eliminado in lista:
            lista.remove(eliminado)
            print("Nueva lista actualizada:\n")
            for h in lista:
                num = 0
                num += 1
                print(f"{num}. {h}")
        else:
            print("Alumno/a no encontrado.")
        menu = False

    else:
        print("Ingrese sólo un número.")

# SEXTO EJERCICIO:

print("\n")
print("SEXTO EJERCICIO:\n")

import random

lista = []
num = 0

for i in range (7):
    lista.append(random.randint(1,100))

print(lista)

num = lista[-1]

lista.remove(num)
lista.insert(0,num)

print(lista)

# SEPTIMO EJERCICIO:

print("\n")
print("SEPTIMO EJERCICIO:\n")

import random
semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
dia = 0
temp = [[], []]
promedio_min = 0
promedio_max = 0
amplitud_termica = 0
dato = 0
dato2 = "0"

print("Temperaturas de la semana:\n")
for h in semana:
    dia = h
    temp[0].append(random.randint(20,40))
    temp[1].append(random.randint(0,19))
    dato = temp[0][-1] - temp[1][-1]
    print(f"{dia}: Minima: {temp[1][-1]} - Maxima: {temp[0][-1]}")
    if dato > amplitud_termica:
        amplitud_termica = dato
        dato2 = h

promedio_max = sum(temp[0]) / len(temp[0])
promedio_min = sum(temp[1]) / len(temp[1])

print("")
print(f"Promedio maximas: {promedio_max:.2f}.")
print(f"Promedio minimas: {promedio_min:.2f}.\n")
print(f"La mayor amplitud termica fue el {dato2} con {amplitud_termica}.")

# OCTAVO EJERCICIO:

print("\n")
print("OCTAVO EJERCICIO:\n")

import random

lista = [[],[],[]]

for i in range(5):
    lista[0].append(random.randint(1,10))
    lista[1].append(random.randint(1,10))
    lista[2].append(random.randint(1,10))

estudiante_0 = (lista[0][0] + lista[1][0] + lista[2][0]) / 3
estudiante_1 = (lista[0][1] + lista[1][1] + lista[2][1]) / 3
estudiante_2 = (lista[0][2] + lista[1][2] + lista[2][2]) / 3
estudiante_3 = (lista[0][3] + lista[1][3] + lista[2][3]) / 3
estudiante_4 = (lista[0][4] + lista[1][4] + lista[2][4]) / 3

materia_0 = sum(lista[0]) / 5
materia_1 = sum(lista[1]) / 5
materia_2 = sum(lista[2]) / 5

print(f"Promedio de estudiante 1. {estudiante_0:.2f}")
print(f"Promedio de estudiante 2. {estudiante_1:.2f}")
print(f"Promedio de estudiante 3. {estudiante_2:.2f}")
print(f"Promedio de estudiante 4. {estudiante_3:.2f}")
print(f"Promedio de estudiante 5. {estudiante_4:.2f}\n")

print(f"Promedio de materia 1. {materia_0:.2f}")
print(f"Promedio de materia 2. {materia_1:.2f}")
print(f"Promedio de materia 3. {materia_2:.2f}")

# NOVENO EJERCICIO:

print("\n")
print("NOVENO EJERCICIO:\n")

lista = [["-","-","-"],["-","-","-"],["-","-","-"]]
menu0 = True
menu1 = True
menu2 = False

for i in lista:
    print(i)

while menu0:


    while menu1:
        print("")
        print("PRIMER JUGADOR\n")
        print("Ficha 'X'")
        x_columna = input("Columna: ")
        x_fila = input("Fila: ")
        print("")

        if (x_columna == "1") and (x_fila == "1"):
            lista[0].pop(0)
            lista[0].insert(0, "X")
            for i in lista:
                print(i)
            menu1 = False
            menu2 = True
        elif (x_columna == "2") and (x_fila == "1"):
            lista[0].pop(1)
            lista[0].insert(1, "X")
            for i in lista:
                print(i)
            menu1 = False
            menu2 = True
        elif (x_columna == "3") and (x_fila == "1"):
            lista[0].pop(2)
            lista[0].insert(2, "X")
            for i in lista:
                print(i)
            menu1 = False
            menu2 = True

        elif (x_columna == "1") and (x_fila == "2"):
            lista[1].pop(0)
            lista[1].insert(0, "X")
            for i in lista:
                print(i)
            menu1 = False
            menu2 = True
        elif (x_columna == "2") and (x_fila == "2"):
            lista[1].pop(1)
            lista[1].insert(1, "X")
            for i in lista:
                print(i)
            menu1 = False
            menu2 = True
        elif (x_columna == "3") and (x_fila == "2"):
            lista[1].pop(2)
            lista[1].insert(2, "X")
            for i in lista:
                print(i)
            menu1 = False
            menu2 = True

        elif (x_columna == "1") and (x_fila == "3"):
            lista[2].pop(0)
            lista[2].insert(0, "X")
            for i in lista:
                print(i)
            menu1 = False
            menu2 = True
        elif (x_columna == "2") and (x_fila == "3"):
            lista[2].pop(1)
            lista[2].insert(1, "X")
            for i in lista:
                print(i)
            menu1 = False
            menu2 = True
        elif (x_columna == "3") and (x_fila == "3"):
            lista[2].pop(2)
            lista[2].insert(2, "X")
            for i in lista:
                print(i)
            menu1 = False
            menu2 = True
        else:
            print("Caracter invalido.")


    while menu2:
        print("")
        print("SEGUNDO JUGADOR\n")
        print("Ficha 'O'")
        x_columna = input("Columna: ")
        x_fila = input("Fila: ")
        print("")

        if (x_columna == "1") and (x_fila == "1"):
            lista[0].pop(0)
            lista[0].insert(0, "O")
            for i in lista:
                print(i)
            menu2 = False
            menu1 = True
        elif (x_columna == "2") and (x_fila == "1"):
            lista[0].pop(1)
            lista[0].insert(1, "O")
            for i in lista:
                print(i)
            menu2 = False
            menu1 = True
        elif (x_columna == "3") and (x_fila == "1"):
            lista[0].pop(2)
            lista[0].insert(2, "O")
            for i in lista:
                print(i)
            menu2 = False
            menu1 = True

        elif (x_columna == "1") and (x_fila == "2"):
            lista[1].pop(0)
            lista[1].insert(0, "O")
            for i in lista:
                print(i)
            menu2 = False
            menu1 = True
        elif (x_columna == "2") and (x_fila == "2"):
            lista[1].pop(1)
            lista[1].insert(1, "O")
            for i in lista:
                print(i)
            menu2 = False
            menu1 = True
        elif (x_columna == "3") and (x_fila == "2"):
            lista[1].pop(2)
            lista[1].insert(2, "O")
            for i in lista:
                print(i)
            menu2 = False
            menu1 = True

        elif (x_columna == "1") and (x_fila == "3"):
            lista[2].pop(0)
            lista[2].insert(0, "O")
            for i in lista:
                print(i)
            menu2 = False
            menu1 = True
        elif (x_columna == "2") and (x_fila == "3"):
            lista[2].pop(1)
            lista[2].insert(1, "O")
            for i in lista:
                print(i)
            menu2 = False
            menu1 = True
        elif (x_columna == "3") and (x_fila == "3"):
            lista[2].pop(2)
            lista[2].insert(2, "O")
            for i in lista:
                print(i)
            menu2 = False
            menu1 = True
        else:
            print("Caracter invalido. Vuelva  intentarlo.\n")

# DECIMO EJERCICIO:

print("\n")
print("DECIMO EJERCICIO:\n")

import random
lista = [[],[],[],[]]
lista_2 = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
lista_3 = []
lista_4 = ["Producto 1","Producto 2","Producto 3","Producto 4"]
producto_1 = 0
producto_2 = 0
producto_3 = 0
producto_4 = 0
ventas_mejor_dia = 0
mejor_producto = []


for i in range (7):
    lista[0].append(random.randint(0,100))
    lista[1].append(random.randint(0,100))
    lista[2].append(random.randint(0,100))
    lista[3].append(random.randint(0,100))

producto_1 = sum(lista[0])
producto_2 = sum(lista[1])
producto_3 = sum(lista[2])
producto_4 = sum(lista[3])

print("Total de productos vendidos en la semana:\n")

print(f"Producto 1. {producto_1}")
print(f"Producto 2. {producto_2}")
print(f"Producto 3. {producto_3}")
print(f"Producto 4. {producto_4}\n")

ventas_lunes = lista[0][0] + lista[1][0] + lista[2][0] + lista[3][0]
ventas_martes = lista[0][1] + lista[1][1] + lista[2][1] + lista[3][1]
ventas_miercoles = lista[0][2] + lista[1][2] + lista[2][2] + lista[3][2]
ventas_jueves = lista[0][3] + lista[1][3] + lista[2][3] + lista[3][3]
ventas_viernes = lista[0][4] + lista[1][4] + lista[2][4] + lista[3][4]
ventas_sabado = lista[0][5] + lista[1][5] + lista[2][5] + lista[3][5]
ventas_domingo = lista[0][6] + lista[1][6] + lista[2][6] + lista[3][6]

lista_3 = [ventas_lunes, ventas_martes, ventas_miercoles, ventas_jueves, ventas_viernes,ventas_sabado, ventas_domingo]
ventas_mejor_dia = max(lista_3)
dia = lista_3.index(ventas_mejor_dia)
venta_dia = lista_2[dia]

print(f"El día con mayores ventas totales fue el {venta_dia} con {ventas_mejor_dia}.\n")

productos = [producto_1, producto_2, producto_3, producto_4]
producto_mas_vendido = max(productos)
mejor_producto = productos.index(producto_mas_vendido)
dia_2 = lista_4[mejor_producto]

print(f"El producto más vendido de la semana fue el {dia_2} con {producto_mas_vendido}")

# UNDÉCIMO EJERCICIO:

print("\n")
print("UNDÉCIMO EJERCICIO:\n")

lista_1 = ["Zafiro", "Xiomara", "Wadalupe", "Valentino", "Ulises", "Tomas", "Soledad", "Ricardo", "Quela", "Olga"]
dato_1 = 0
dato_2 = 0
usuaio = 0
menu_1 = True

while menu_1:
    usuario = input("Ingrese el nombre: ").title()
    print("")

    if not usuario.isalpha():
        print("Nombre no encontrado. Ingrese solo letras\n")

    elif usuario in lista_1:
        print("El alumno si se encuentra en la lista.")
        dato_2 = lista_1.index(usuario)
        print(f"Está en la prosición {dato_2+1}.\n")
        menu_1 = False

    else:
        print("El alumno no se encuentra en la lista.\n")
        menu_1 = False

# DUODÉCIMO EJERCICIO:

print("\n")
print("DUODÉCIMO EJERCICIO:\n")

lista_1 = []
lista_2 = []
lista_3 = []
menu_1 = 0

while menu_1 < 8:
    num = input("Ingrese los números enteros: ")

    if not num.isdigit():
        print("Ingrese sólo números enteros.")

    elif num.isdigit():
        num = int(num)
        lista_1.append(num)
        menu_1 += 1

print("")
print(lista_1)

lista_2 = sorted(lista_1)

print(lista_2)

lista_2.reverse()

print(lista_2)

# DÉCIMO TERCER EJERCICIO:

print("\n")
print("DÉCIMO TERCER EJERCICIO:\n")

puntajes = [450, 1200, 875, 990, 300, 1500, 640]
ranking = []
pocision = 0

print(f"Puntaje mas alto: {max(puntajes)}")
print(f"Puntaje mas bajo: {min(puntajes)}\n")

ranking = sorted(puntajes)
ranking.reverse()
pocision = ranking.index(990)

print("RANKING:")
for i in ranking:
    print(f"♦ {i} ♦")

print("")
print(f"El puntaje ♦ 990 ♦ se encuentra en la pocisió {pocision+1}")