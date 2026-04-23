# TRABAJO PRACTICO - ESTRUCTURAS CONDICIONALES 

# RESPUESTAS:

print("")
print("PRIMERA ACTIVIDAD:")
print("")

numero = int(input("Ingrese su edad: "))

if numero > 18:
    print("Es mayor de edad.")
elif numero == 18:
    print("Tiene 18 años.")
else:
    print("Es menor de edad.")

print("")
print("SEGUNDA ACTIVIDAD:")
print("")

nota = int(input("Ingrese la nota: "))

if (nota >= 6) and (nota <= 10):
    print("Aprobado.")
elif nota < 6:
    print("Desaprobado.")
else:
    print("Ingrese un número entre 0 y 10.")

print("")
print("TERCERA ACTIVIDAD:")
print("")

numero = int(input("Ingrese un número: "))

if (numero % 2) == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")

print("")
print("CUARTA ACTIVIDAD:")
print("")

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Es Niña/o.")
elif (edad >= 12) and (edad < 18):
    print("Es adolescente.")
elif (edad >= 18) and (edad < 30):
    print("Es adulta/o joven.")
else:
    print("Es adulta/o.")

print("")
print("QUINTA ACTIVIDAD:")
print("")

contraseña = input("Ingrese su contraseña: ")

longitud = len(contraseña)
numero = int(longitud)

if (numero <= 14) and (numero >= 8):
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

print("")
print("SEXTA ACTIVIDAD:")
print("")

usuario = input("Ingrese su consumo en kilovatios(kWh): ")

if usuario.isdigit():
    consumo = int(usuario)
    if consumo > 500:
        print("Considere medidas de ahorro de energia.")
    elif (consumo > 300) and (consumo < 500):
        print("Consumo alto.")
    elif (consumo >= 150) and (consumo <= 300):
        print("Condumo medio.")
    else:
        print("Consumo bajo.")
else:
    print("Ingrese solo números.")

print("")
print("SEPTIMA ACTIVIDAD:")
print("")

usuario = input("Ingrese una palabra o frase: ")

if usuario.endswith("a","e","i","o","u"):
    usuario += "!"
    print(usuario)
else:
    print(usuario)

print("")
print("OCTAVA ACTIVIDAD:")
print("")

nombre = input("Ingrese su nombre: ")

print("")

print("Ingrese el numero de la opcion que desee: \n " \
"1. Si quiere su nombre en mayúsculas. \n " \
"2. Si quiere su nombre en minúsculas. \n " \
"3. Si quiere su nombre con la primera letra mayúscula.")

print("")

dia = int(input("Ingrese el número: "))

print("")

if dia == 1:
    print(nombre.upper())
elif dia == 2:
    print(nombre.lower())
elif dia == 3:
    print(nombre.title())
else:
    print("Su número es invalido:")

print("")
print("NOVENA ACTIVIDAD:")
print("")

dia = int(input("Ingrese el valor del terremoto en escala de Ritcher: "))

if dia < 3:
    print("Muy leve (inperceptible).")
elif dia >= 3 and dia < 4:
    print("Leve (ligeramente perceptible).")
elif dia >= 4 and dia < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif dia >= 5 and dia < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif dia >= 6 and dia < 7:
    print( "Muy Fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")

print("")
print("DECIMA ACTIVIDAD:")
print("")

hemisferio = input("Ingrese su hemisferio: ").upper()
mes = int(input("Ingrese el número de su mes: "))
dia = int(input("Ingrese su día: "))

if hemisferio.startswith("N"):
    match mes:
        case 1:
            if (dia >= 1) and (dia <= 30):
                print("Es invierno.")
            else: 
                print("El día no es valido.")
        case 2:
            if (dia >= 1) and (dia <= 28):
                print("Es invierno.")
            else: 
                print("El día no es valido.")
        case 3:
            if dia <= 20:
                print("Es invierno.")
            elif (dia >= 21) and (dia <= 31):
                print("Es primavera.")
            else: 
                print("El día no es valido.")
        case 4:
            if (dia >= 1) and (dia <= 30):
                print("Es primavera.")
            else: 
                print("El día no es valido.")
        case 5:
            if (dia >= 1) and (dia <= 31):
                print("Es primavera.")
            else: 
                print("El día no es valido.")
        case 6:
            if dia <= 20:
                print("Es primavera.")
            elif (dia >= 21) and (dia <= 30):
                print("Es verano.")
            else: 
                print("El día no es valido.")
        case 7:
            if (dia >= 1) and (dia <= 31):
                print("Es verano.")
            else: 
                print("El día no es valido.")
        case 8:
            if (dia >= 1) and (dia <= 31):
                print("Es verano.")
            else: 
                print("El día no es valido.")
        case 9:
            if dia <= 20:
                print("Es verano.")
            elif (dia >= 21) and (dia <= 30):
                print("Es otoño.")
            else: 
                print("El día no es valido.")
        case 10:
            if (dia >= 1) and (dia <= 31):
                print("Es otoño.")
            else: 
                print("El día no es valido.")
        case 11:
            if (dia >= 1) and (dia <= 31):
                print("Es otoño.")
            else: 
                print("El día no es valido.")
        case 12:
            if dia <= 20:
                print("Es otoño.")
            elif (dia >= 21) and (dia <= 30):
                print("Es invierno.")
            else: 
                print("El día no es valido.")
        case _:
            print("Mes invalido.")

elif hemisferio.startswith("S"):
    match mes:
        case 1:
            if (dia >= 1) and (dia <= 30):
                print("Es verano.")
            else: 
                print("El día no es valido.")
        case 2:
            if (dia >= 1) and (dia <= 28):
                print("Es verano.")
            else: 
                print("El día no es valido.")
        case 3:
            if dia <= 20:
                print("Es verano.")
            elif (dia >= 21) and (dia <= 31):
                print("Es otoño.")
            else: 
                print("El día no es valido.")
        case 4:
            if (dia >= 1) and (dia <= 30):
                print("Es otoño.")
            else: 
                print("El día no es valido.")
        case 5:
            if (dia >= 1) and (dia <= 31):
                print("Es otoño.")
            else: 
                print("El día no es valido.")
        case 6:
            if dia <= 20:
                print("Es otoño.")
            elif (dia >= 21) and (dia <= 30):
                print("Es invierno.")
            else: 
                print("El día no es valido.")
        case 7:
            if (dia >= 1) and (dia <= 31):
                print("Es invierno.")
            else: 
                print("El día no es valido.")
        case 8:
            if (dia >= 1) and (dia <= 31):
                print("Es invierno.")
            else: 
                print("El día no es valido.")
        case 9:
            if dia <= 20:
                print("Es invierno.")
            elif (dia >= 21) and (dia <= 30):
                print("Es primavera.")
            else: 
                print("El día no es valido.")
        case 10:
            if (dia >= 1) and (dia <= 31):
                print("Es primavera.")
            else: 
                print("El día no es valido.")
        case 11:
            if (dia >= 1) and (dia <= 31):
                print("Es primavera.")
            else: 
                print("El día no es valido.")
        case 12:
            if dia <= 20:
                print("Es primavera.")
            elif (dia >= 21) and (dia <= 30):
                print("Es verano.")
            else: 
                print("El día no es valido.")
        case _:
            print("Mes invalido.")
else:
    print("Hemisferio invalido.")