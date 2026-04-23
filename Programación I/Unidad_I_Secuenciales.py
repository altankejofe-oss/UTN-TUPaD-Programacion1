
# TRABAJO PRACTICO N°1
# RESPUESTAS:

# EJERCICIO N°1:

texto = "Hola Mundo!"
print(texto)

# EJERCICIO N°2:

usuario = input("Ingrese su nombre: ")

print(f"Hola",usuario,"!")

# EJERCICIO N°3:

nombre = input("Ingrese su/s nobre/s: ")
apellido = input("Ingrese su/s apellido/s: ")
edad = input("Ingrese su edad: ")
recidencia = input("Ingrese su lugar de recidencia: ")

print(f"Soy",nombre,apellido,", tengo",edad,"años y vivo en",recidencia,)

# EJERCICIO N°4:

from math import pi

radio = int(input("Ingrese el radio: "))

area = pi * radio**2
perimetro = 2 * pi * radio

print(f"Area:",area,)
print("Perimetro:",perimetro,)

# EJERCICIO N°5:

seg = int(input("Ingrese los segundos: "))

hora = seg / 3600

print(f"Los",seg,"segundos equibalen a",hora,"horas")

# EJERCICIO N°6:

num = int(input("Ingrese su número: "))

for i in range(1, 11):
    res = num * i
    print(f"",num,"x",i,"=",res,)

# EJERCICIO N°7:

num1 = input("Ingrese su primer número entero:")
num2 = input("Ingrese su segundo número entero:")

if num1.isdigit() or num1.startswith("-"):
    enta = int(num1)
    if enta == 0:
        print("Su numero no puede ser 0.")
    else:
        ent1 = enta

else:
    print("Caracter invalido.")

if num2.isdigit() or num2.startswith("-"):
    entb = int(num2)
    if entb == 0:
        print("Su numero no puede ser 0.")
    else:
        ent2 = entb

else:
    print("Caracter invalido.")

suma = ent1 + ent2
resta = ent1 - ent2
multi = ent1 * ent2
divi = ent1 / ent2

print("La sumatoria de los números es:",suma,)
print("La resta de los números es:",resta,)
print("La multiplicación de los números es:",multi,)
print("La división de los números es:",divi,)

# EJERCICIO N°8:

dato1 = input("Ingrese su altura en metros: ")
dato2 = input("Ingrese su peso en kg: ")

try:
    altura = float(dato1)
    peso = float(dato2)

    if altura <= 0 or peso <= 0:
        print("Ingrese valores positivos.")

    else:
        imc = peso / (altura ** 2)
        print("Su índice de masa corporal es:",imc,)

except:
    print("Ingrese datos válidos.")

# EJERCICIO N°9:

dato = input("Ingrese la temperatura: ")

try:
    celsius = float(dato)

    far = celsius * 9/5 + 32

    print("La temperatura en Fahrenheit es:",far,)

except:
    print("Ingrese un numero valido.")

# EJERCICIO N°10:

try:
    dato1 = float(input("Ingrese el primer número: "))
    dato2 = float(input("Ingrese el segundo número: "))
    dato3 = float(input("Ingrese el tercer número: "))

    prom = (dato1 + dato2 + dato3) / 3

    print("El promedio de los tres números es de:",prom,)

except:
    print("Dato invalido.")