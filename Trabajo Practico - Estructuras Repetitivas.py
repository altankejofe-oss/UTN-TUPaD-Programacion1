# TRABAJO PRACTICO

# RESPUESTAS:

# PRIMERA ACTIVIDAD:
print("\n")
print("PRIMERA ACTIVIDAD:\n")

menu = True

while menu:
    total_sin = 0
    total_con = 0
    ahorro = 0
    print("")
    print("----- INGRESE 'EXIT' PARA SALIR -----\n")
    while True:
        nombre = input("Ingrese su nombre: ").strip()
        if nombre.upper() == "EXIT":
            menu = False
            break
        if nombre != "" and nombre.replace(" ", "").isalpha():
            print(f"\nHola {nombre.title()}!\n")
            break
        else:
            print("Nombre inválido.")
    if not menu:
        break

    while True:
        productos = input("Cantidad de productos: ")
        if productos.upper() == "EXIT":
            menu = False
            break
        if productos.isdigit() and int(productos) > 0:
            productos = int(productos)
            break
        else:
            print("Ingrese un número mayor a 0.")
    if not menu:
        break

    for i in range(1, productos + 1):        
        while True:
            precio = input(f"\nProducto {i} - Precio: ")
            if precio.upper() == "EXIT":
                menu = False
                break
            if precio.isdigit():
                precio = int(precio)
                break
            else:
                print("Precio inválido.")
        if not menu:
            break
        total_sin += precio

        while True:
            desc = input("Descuento (S/N): ")
            if desc.upper() == "EXIT":
                menu = False
                break
            if desc.lower() == "s" or desc.lower() == "n":
                break
            else:
                print("Ingrese S o N.")
        if not menu:
            break
        if desc.lower() == "s":
            total_con += precio * 0.9
            ahorro += precio * 0.1
        else:
            total_con += precio
    if not menu:
        break

    promedio = total_con / productos

    print("\n------ TICKET ------")
    print(f"Cliente: {nombre.title()}")
    print(f"Total de productos sin descuentos: ${total_sin:.2f}")
    print(f"Total de productos con descuentos: ${total_con:.2f}")
    print(f"Total ahorrado: ${ahorro:.2f}")
    print(f"Total del promedio por producto: ${promedio:.2f}")
    print("--------------------\n")
    
# SEGUNDA ACTIVIDAD:
print("\n")
print("SEGUNDA ACTIVIDAD:\n")

usuario = "alumno"
contraseña = "python123"
menu = True
menu2 = True
menu3 = True
menu31 = True
intentos = 1
opcion = "0"

while menu == True:
    
    usuarioingresado = input("Ingrese el usuario: ").lower()
    if usuarioingresado == usuario:
        menu = False
    
    elif usuarioingresado != usuario:
        print(f"Usuario incorrecto. Vuelva a ingresarlo (intento {intentos}/3)")
        intentos +=1

    if intentos == 4:
        print("Demasiados intentos. Cuenta bloqueada.")
        menu = False
        menu2 = False
    
while menu2 == True:
    
    contraseñaingresada = input("Ingrese la contraseña: ").lower()
    if contraseñaingresada == contraseña:
        menu2 = False
    
    elif contraseñaingresada != contraseña:
        print(f"Contraseña incorrecto. Vuelva a ingresarla (intento {intentos}/3)")
        intentos +=1

    if intentos == 4:
        print("Demasiados intentos. Cuenta bloqueada.")
        menu2 = False

while menu3 == True:

    print("MENÚ:")
    print("1. Ver estado de inscripción.")
    print("2. Cambiar clave.")
    print("3. Mostrar mensaje motivacional.")
    print("4. Salir.")

    opcion = input("Ingrese la opción que desee: ")

    if opcion == "1":
        print("Alumna/o Inscripto.")
    
    elif opcion == "2":

        while menu31 == True:
            print("Ingrese su nueva contraseña:")
            nuevaclave = input("")
            print("Confirme la contraseña:")
            nuevaclave2 = input("")

            if nuevaclave == nuevaclave2:
                contraseña = nuevaclave
                print("Contraseña actualizada.")
                menu31 = False

            else:
                print("Las contraseñas deven coincidir.")

    elif opcion == "3":

            print("POR LA HORDA")
    
    elif opcion == "4":
        menu3 = False
    
    else:
        print("Solo ingrese números para acceder a las opciones. Vuelva a intentarlo.")

# TERCERA ACTIVIDAD:
print("\n")
print("TERCERA ACTIVIDAD:\n")

menu1 = True
menu2 = True
menu2_1 = True
menu2_2 = True
menu2_3 = True
menu2_3_1 = True
menu2_1_2 = True
menu2_1_3 = True
menu2_4 = True

dia = "0"
turno = "0"
paciente = "0"
turnos_lunes = 0
lunes1 = "ramon romero"
lunes2 = "libre"
lunes3 = "carolina carola"
turnos_martes = 0
martes1 = "juan jofre"
martes2 = "libre"
martes3 = "libre"


while menu1 == True:
    nombre = input("Ingrese su nombre: ")
    print("")

    if nombre.isalpha():
        menu1 = False
    
    else:
        print("Solo ingrese letras por favor.")
        print("")

while menu2 == True:
    print("MENÚ PRINCIPAL:\n")
    print("1. Reservar turno.")
    print("2. Cancelar turno.")
    print("3. Ver agenda del día.")
    print("4. Ver resumen general.")
    print("5. Cerrar sistema.\n")
    opcion = input("Ingrese el número de la opcion a la que desee ingresar: ")

    match opcion:
        case "1":
            while menu2_1 == True:
                print("RESERVAR TURNO:\n")
                print("Elija el dia que desee reservar:\n")
                print("1. Lunes.")
                print("2. Martes.\n")
                dia = input("Ingrese el día: ")

                while menu2_2 == True:
                    if dia == "1":
                        paciente = input("Ingrese el nombre del paciente: ").lower().strip()
                        if (paciente == "") or (paciente.isdigit()):
                            print("Por favor, ingrese solo el nombre.\n")                   
                        elif " ".join(paciente.split()) == lunes3:
                            print(f"Turno ya registrado.({lunes3.title()})\n")
                        elif " ".join(paciente.split()) == lunes1:
                            print(f"Turno ya registrado.({lunes1.title()})\n")
                        elif " ".join(paciente.split()) not in (lunes1, lunes3):
                            lunes2 = paciente
                            print(f"Paciente {lunes2.title()} registrado (Segundo turno).\n")                        
                            menu2_2 = False
                            menu2_3 = False
                
                while menu2_3 == True:
                    if dia == "2":
                        paciente = input("Ingrese el nombre del paciente: ").lower().strip()
                        if (paciente == "") or (paciente.isdigit()):
                            print("Por favor, ingrese solo el nombre.\n")                   
                        elif " ".join(paciente.split()) == martes1:
                            print(f"Turno ya registrado.({martes1.title()})\n")
                        else:
                            while menu2_3_1 == True:
                                turno = input("Que turno desea? (2 o 3): ")
                                if turno == "2":
                                    martes2 = paciente
                                    print(f"Paciente {martes2.title()} registrado (Segundo turno).\n")
                                    menu2_3 = False
                                    menu2_2 = False
                                    menu2_3_1 = False
                                elif turno == "3":
                                    martes3 = paciente
                                    print(f"Paciente {martes3.title()} registrado (Tercer turno).\n")
                                    menu2_3 = False
                                    menu2_2 = False
                                    menu2_3_1 = False
                                else:
                                    print("Ingrese un numero.")
        
        case "2":
            while menu2_4 == True:
                print("CANCELAR TURNO:\n")
                print("Turnos Lunes:\n")
                print(f"Primer turno: {lunes1.title()}")
                print(f"Segundo turno: {lunes2.title()}")
                print(f"Tercer turno: {lunes3.title()}\n")
                print("Turnos Martes:\n")
                print(f"Primer turno: {martes1.title()}")
                print(f"Segundo turno: {martes2.title()}")
                print(f"Tercer turno: {martes3.title()}\n")
                paciente = input("Ingrese el nombre del paciente: ").lower().strip()
                if (paciente == "") or (paciente.isdigit()):
                            print("Por favor, ingrese solo el nombre.\n") 
                elif " ".join(paciente.split()) == lunes1:
                    lunes1 = ""
                    print("Turno cancelado.\n")
                    menu2_4 = False
                elif " ".join(paciente.split()) == lunes2:
                    lunes2 = ""
                    print("Turno cancelado.\n")
                    menu2_4 = False
                elif " ".join(paciente.split()) == lunes3:
                    lunes3 = ""
                    print("Turno cancelado.\n")
                    menu2_4 = False
                elif " ".join(paciente.split()) == martes1:
                    martes1 = ""
                    print("Turno cancelado.\n")
                    menu2_4 = False
                elif " ".join(paciente.split()) == martes2:
                    martes2 = ""
                    print("Turno cancelado.\n")
                    menu2_4 = False
                elif " ".join(paciente.split()) == martes3:
                    martes3 = ""
                    print("Turno cancelado.\n")
                    menu2_4 = False
                else:
                    print("Paciente no encontrado.")

        case "3":
            print("AGENDA:\n")
            print("Turnos Lunes:\n")
            print(f"Primer turno: {lunes1.title()}")
            print(f"Segundo turno: {lunes2.title()}")
            print(f"Tercer turno: {lunes3.title()}\n")
            print("Turnos Martes:\n")
            print(f"Primer turno: {martes1.title()}")
            print(f"Segundo turno: {martes2.title()}")
            print(f"Tercer turno: {martes3.title()}\n")
        
        case "4":
            print("RESUMEN:\n")
            print("Lunes:")
            if lunes1 != "libre":
                turnos_lunes += 1
            if lunes2 != "libre":
                turnos_lunes += 1
            if lunes3 != "libre":
                turnos_lunes += 1
            print("Turnos ocupados:",turnos_lunes )
            print("Turnos libres:",3 - (turnos_lunes))
            print("Martes:")
            if martes1 != "libre":
                turnos_lunes += 1
            if martes2 != "libre":
                turnos_lunes += 1
            if martes3 != "libre":
                turnos_lunes += 1
            print("Turnos ocupados:",turnos_martes )
            print("Turnos libres:",3 - (turnos_martes))

            if turnos_martes < turnos_lunes:
                print("Tienes mas turnos el día lunes.\n")
            elif turnos_martes > turnos_lunes:
                print("Tienes mas turnos el día martes.\n")
            else:
                print("Tiene la misma cantidad de turnos en ambos días.")
            
        case "5":
            print("Adiós.")
            menu2 = False

# CUARTA ACTIVIDAD:
print("\n")
print("CUARTA ACTIVIDAD:\n")

energia = 100
tiempo = 12 
cerraduras_abiertas = 0 
alarma = False 
codigo_parcial = ""
accion = ""
opcion = ""
cerradura_forzada = 0
menu1 = True
menu2 = True
menu3 = True

while menu1 == True:
    agente = input("Ingrese su nombre Agente: ")
    print("")
    if agente.isalpha():
        print(f"Hola agente {agente.capitalize()}\n")
        menu1 = False
    elif agente == "":
        print("Igrese el nombre.\n")
    else:
        print("El nombre solo debe incluir letras. Vuelva a ingresarlo.\n")

while (energia >= 1) and (tiempo >= 1) and (cerraduras_abiertas < 3):
    if (alarma == True) and (tiempo <= 3):
        energia = 0
    elif alarma == True:
        print("¡ALARMA ACTIVADA!\n")

    print(f"Energia: {energia}      Tiempo:{tiempo}     Cerraduras abiertas:{cerraduras_abiertas}/3\n")
    print(f"¿Agente {agente.capitalize()} que desea hacer?\n")
    print("OPCIONES:")
    print("1. Forzar cerradura.")
    print("2. Hackear panel.")
    print("3. Descansar.\n")

    while menu2 == True:
        accion = input("Ingrese el número de la opción: ")
        print("")
        if accion.isdigit():
            print("Estudiando cerradura...\n")
            menu2 = False
        else:
            print("Ingrese solo el número. Vuelva a intentarlo.\n")

    match accion:
        case "1":
            cerradura_forzada += 1
            energia -= 20
            tiempo -= 2
            if cerradura_forzada == 3:
                alarma = True
                print("¡La cerradura se trabó!\n")
                print("¡ALARMA ACTIVADA!\n")
            if alarma == False:
                if energia < 40:
                    print("RIESGO DE ALARMA!\n")
                    print("1. Forzar.")
                    print("2. Forzar.")
                    print("3. Forzar.\n")

                    while menu3 == True:
                        opcion = input("Elija una opción: ")
                        print("")
                        if accion.isdigit():
                            print("Forzando cerradura...\n")
                            opcion = int(opcion)
                            if opcion < 4:
                                match opcion:
                                    case 1:
                                        cerraduras_abiertas += 1
                                        print("Cerradura abierta!\n")
                                        menu3 = False
                                    case 2:
                                        cerraduras_abiertas += 1
                                        print("Cerradura abierta!\n")
                                        menu3 = False
                                    case 3:
                                        alarma = True
                                        print("¡ALARMA ACTIVADA!\n")
                                        menu3 = False
                            else:
                                print("El número no puede ser mayor a 4.")                        
                        else:
                            print("Ingrese solo el número. Vuelva a intentarlo.\n")

                elif energia >= 40:
                    cerraduras_abiertas += 1
                    print("Cerradura abierta!\n")
                else:
                    print("¡Solo números!\n")

            elif alarma == True:
                print("¡No puedes forzar la cerradura con la alarma activada!\n")

        case "2":
            cerradura_forzada = 0
            energia -= 10
            tiempo -= 3

            if energia >= 1:
                for i in range(1,5):
                    letra = input(f"{i}/4 Ingrese el código: {codigo_parcial}")    
                    codigo_parcial += letra
                    print("")

                if len(codigo_parcial) >= 8:
                    cerraduras_abiertas += 1
                    codigo_parcial = ""
                    print("Cerradura abierta!\n")
                elif len(codigo_parcial) < 8:
                    codigo_parcial = ""
                    print("El hackeo falló.\n")
            
        case "3":
            cerradura_forzada = 0
            if alarma == False:
                energia += 15
                tiempo -= 1
            elif alarma == True:
                energia -= 10
                tiempo -= 1
            if energia > 100:
                energia = 100

if cerraduras_abiertas == 3:
    print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
    print("La puerta se abrió.")
else:
    print("GAME OVER")

# QUINTA ACTIVIDAD:
print("\n")
print("QUINTA ACTIVIDAD:\n")

jugador = "nombre"
turno_gladiador = True
opcion = "0"
menu1 = True
vida_del_gladiador = 11  
vida_del_enemigo = 100
pociones_de_vida = 3  
daño_base_rafaga = 5
daño_base_ataque_pesado = 15 
daño_base_del_enemigo = 12
turno_gladiador = True
turno_enemigo = True
daño_critico = 0

while menu1 == True:
    print("--- BIENVENIDO A LA ARENA ---  \n")
    print("¡Ingrese su nombre gladiador!:\n")
    jugador = input("")
    print("")
    if jugador.isalpha():
        print(f"BIENVENIDO GLADIADOR ¡{jugador.upper()}!\n")
        print("=== INICIO DEL COMBATE ===\n")  
        menu1 = False
    else:
        print("Error: Solo se permiten letras. Vuelva a ingresar su nombre.\n")

while (vida_del_gladiador > 0) and (vida_del_enemigo > 0): 
    turno_gladiador = True
    turno_enemigo = True

    while turno_gladiador == True:
        print(f"{jugador.upper()} (HP: {vida_del_gladiador}) vs Enemigo (HP: {vida_del_enemigo}) | Pociones: {pociones_de_vida}\n")
        print("Elige acción:\n")
        print("1. Ataque Pesado.")
        print("2. Ráfaga Veloz.")  
        print("3. Curar.")

        opcion = input("Opcion: ")
        print("")
        if opcion.isdigit():
            opcion = int(opcion)
            if (opcion <= 3) and (opcion >= 1):
                match opcion:
                    case 1:
                        
                            print("¡Inicias un golpe pesado!")
                            if vida_del_enemigo < 20:
                                daño_base_ataque_pesado = float(daño_base_ataque_pesado)
                                vida_del_enemigo = float(vida_del_enemigo)
                                daño_critico = daño_base_ataque_pesado * 1.5
                                vida_del_enemigo -= daño_critico
                                turno_gladiador = False
                                print("♦ GOLPE CRITICO ♦\n")
                            else:
                                vida_del_enemigo -= daño_base_ataque_pesado
                                turno_gladiador = False
                                print(f"♦ ¡ Golpe conectado por {daño_base_ataque_pesado} de daño  !\n")
                    
                    case 2:
                        print("¡Inicias una ráfaga de golpes!\n")
                        for i in range(3):
                            print(f"♦ ¡Golpe conectado por {daño_base_rafaga} de daño!")
                            vida_del_enemigo -= daño_base_rafaga
                            turno_gladiador = False
                            if vida_del_enemigo <= 0:
                                turno_enemigo = False
                        print("")

                    case 3:
                        if pociones_de_vida > 0:
                            vida_del_gladiador += 30
                            pociones_de_vida -= 1
                            turno_gladiador = False
                            print("¡Vida restaurada!\n")
                        else:
                            print("¡No quedan pociones!\n")
                            turno_enemigo = True
            else:
                print("Ingrese un número entre 1 y 3.\n")
                turno_enemigo = False

        else:
            print("Error: Ingrese un número válido. Vuelva a intentarlo.\n")
    
    while turno_enemigo == True:
        print(f"♦==♦ ¡El enemigo contraataca por {daño_base_del_enemigo} puntos!♦==♦\n")
        print("=== NUEVO TURNO ===\n")
        vida_del_gladiador -= daño_base_del_enemigo
        turno_enemigo = False

if vida_del_enemigo <= 0:
    print(f"¡VICTORIA! {jugador} ha ganado la batalla.\n")
elif vida_del_gladiador <=0:
    print("DERROTA. Has caído en combate.\n")
