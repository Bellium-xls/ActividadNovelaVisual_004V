import time
print("=== BIENVENIDO AL JUEGO, VE  COMIENZA TU AVENTURA ===")
entrar = 1
nombre_jugador = input("POR FAVOR INGRESE SU NOMBRE DE AVENTURERO: ")
entrada_aljuego = input("1. ENTRAR  2. SALIR \n")
while entrada_aljuego == "ENTRAR" or "Entrar" or "entrar" or "1" or 1:
    print("//// ESCOGE TU CLASE ////")
    clase = int(input("[[[1. MAGO]]] \n[[[2.CABALLERO]]] \n[[[3.ASESINO]]] \n"))
    if clase == 1:
        hpmago = 75
        atkmago = 5
        apmago = 35
        manamago = 50
        speedmago = 80
    elif clase == 2:
        hpcaballero = 150
        atkcaballero = 40
        apcaballero = 0
        manacaballero = 0
        speedcaballero = 100
    elif clase == 3:
        hpasesino = 90
        atkasesino = 55
        apasesino = 5
        manaasesino = 20
        speedasesino = 160
    else:
        print("Aún no tenemos disponible más clases lo sentimos :( .)")
    print(f"°|||=> {nombre_jugador} para empezar su aventura se dirige al gremio para reclamar su primera misión <=|||°")
    mision = int(input(f"Maestra del Gremio: Bienvenido {nombre_jugador}, aqui tenemos las distintas misiones para tu aventura. \n--- 1. Derrotar al jefe de la mazmorra oculta entre las montañas --- \n--- 2. Pelear contra Cerbero, el perro del inframundo --- \n ---> "))
    if mision == 1:
        if clase == 1:
            print("Te diriges en busca de la mazmorra con tu equipamiento principiante y con tu magia iluminas tu camino.")
            print("En el camino sientes como un escalofrio recorre tu columna desde abajo hacia arriba, sabes que se acerca algo peligroso por tu maná.")
            print(".\n..\n...\n....\n.....")
            print("¡¡¡¡HAZ ENTRADO EN COMBATE CON UN NO-MUERTO!!!!")
            enemyhp = 500
            atkenemy = 15
            while enemyhp > 0 and hpmago > 0:
                accion = int(input("\n1.Atacar\n2.Ver estadisticas\n3.Curarse\n4.Intentar huir. \n---> "))
                if accion == 1:
                    rayodeluz = 5
                    vendaval = 3
                    pelluco = 10
                    ataquesmago = int(input("\n1.|Rayo de luz|\n2.|Vendaval del sur|\n3.|Invocar a Pelluco|\n---> "))
                    if ataquesmago == 1:
                        enemyhp = enemyhp - (rayodeluz * apmago)
                        manamago = manamago - 10
                        print(f"Ataque efectivo, vida restante del enemigo : {enemyhp}.")
                    elif ataquesmago ==2:
                        enemyhp = enemyhp - (vendaval * apmago)
                        manamago -= 5
                        print(f"Azotas con fuertes vientos a tu enemigo, su vida restante : {enemyhp}.")
                    elif ataquesmago == 3:
                        print(f"¡Pelluco ha aparecido!\nEstá muy enojado por haberlo despertado de su sueño.")
                        enemyhp = enemyhp - (pelluco *apmago)
                        manamago -= 10
                    else:
                        print("Haz pérdido un turno y el enemigo aprovecha para atacarte")
                elif accion == 2:
                    print(f"Vida total del enemigo : {enemyhp}.\nAtaque del enemigo : {atkenemy}.")
                elif accion == 3:
                    hpmago += 15
                    manamago -= 5
                    print(f"Te haz curado 15 puntos vitales, tu HP restante : {hpmago}.")
                elif accion == 4:
                    numero = int(input("Escoge un número. "))
                    if numero % 2 == 0:
                        print("Huyes épicamente.")
                        break
                    else:
                        print("Pérdiste un turno.")
                        hpmago -= atkenemy
                        print(f"El enemigo aprovechó para atacarte, HP restante : {hpmago}.")
                        continue
                else:
                    print("Pérdiste un turno.")
                    hpmago -= atkenemy
                    print(f"El enemigo aprovechó para atacarte, HP restante : {hpmago}.")
                    continue
                