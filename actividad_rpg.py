import time
def imprimir(texto, velocidad=0.03):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(velocidad)
    print()
import sys

imprimir("=== BIENVENIDO AL JUEGO, VE  COMIENZA TU AVENTURA ===")
entrar = 1
nombre_jugador = input("POR FAVOR INGRESE SU NOMBRE DE AVENTURERO: ")
entrada_aljuego = int(input("1. ENTRAR  2. SALIR \n"))
if entrada_aljuego == 1:
    print("//// ESCOGE TU CLASE ////")
    clase = int(input("[[[1. MAGO]]] \n[[[2.CABALLERO]]] \n[[[3.ASESINO]]] \n"))
    if clase == 1:
        hpmago = 75
        atkmago = 5
        apmago = 35
        manamago = 50
    elif clase == 2:
        hpcaballero = 150
        atkcaballero = 40
        apcaballero = 0
        manacaballero = 0
    elif clase == 3:
        hpasesino = 90
        atkasesino = 55
        apasesino = 5
        manaasesino = 20
    else:
        print("Aún no tenemos disponible más clases lo sentimos :( .)")
    time.sleep(1)
    imprimir(f"°|||=> {nombre_jugador} para empezar su aventura se dirige al gremio para reclamar su primera misión <=|||°", 0.05)
    time.sleep(1.5)
    mision = int(input(f"Maestra del Gremio: Bienvenido {nombre_jugador}, aqui tenemos las distintas misiones para tu aventura. \n--- 1. Derrotar al jefe de la mazmorra oculta entre las montañas --- \n--- 2. Pelear contra Cerbero, el perro del inframundo --- \n ---> "))
    if mision == 1:
        if clase == 1:
            imprimir("Te diriges en busca de la mazmorra con tu equipamiento principiante y con tu magia iluminas tu camino.")
            imprimir("Dentro de la mazmorra sientes como un escalofrio recorre tu columna desde abajo hacia arriba, sabes que se acerca algo peligroso por tu maná.")
            time.sleep(1)
            imprimir(".")
            time.sleep(1.5)
            imprimir("..")
            time.sleep(1.8)
            imprimir("...")
            imprimir("¡¡¡¡HAZ ENTRADO EN COMBATE CON EL JEFE DIRECTAMENTE!!!!",0.03)
            bosshp = 500
            bossatk = 20
            while bosshp > 0 and hpmago > 0:
                if bosshp <= 0:
                    print("Combate finalizado.\nHaz derrotado al jefe.")
                    break
                elif hpmago <= 0:
                    print("Haz sido derrotado por el jefe de la mazmorra, intentalo mejor la proxima vez.")
                    sys.exit()
                accion = int(input("\n1.Atacar\n2.Ver estadisticas\n3.Curarse\n4.Intentar huir. \n---> "))
                if accion == 1:
                    rayodeluz = 5
                    vendaval = 3
                    pelluco = 10
                    ataquesmago = int(input("\n1.|Rayo de luz|\n2.|Vendaval del sur|\n3.|Invocar a Pelluco|\n---> "))
                    if ataquesmago == 1:
                        bosshp = bosshp - (rayodeluz * apmago)
                        manamago = manamago - 10
                        print(f"Ataque efectivo, vida restante del enemigo : {bosshp}.")
                    elif ataquesmago ==2:
                        bosshp = bosshp - (vendaval * apmago)
                        manamago -= 5
                        print(f"Azotas con fuertes vientos a tu enemigo, su vida restante : {bosshp}.")
                    elif ataquesmago == 3:
                        print(f"¡Pelluco ha aparecido!\nEstá muy enojado por haberlo despertado de su sueño.")
                        bosshp = bosshp - (pelluco *apmago)
                        manamago -= 10
                        print(f"Le ha causado fatales heridas al enemigo, su hp es de {bosshp}.")
                    else:
                        print("Haz pérdido un turno y el enemigo aprovecha para atacarte")
                        hpmago -= bossatk
                        print(f"Tu vida restante es : {hpmago}.")
                elif accion == 2:
                    print(f"Vida total del enemigo : {bosshp}.\nAtaque del enemigo : {bossatk}.")
                elif accion == 3:
                    if manamago > 0:
                        hpmago += 15
                        manamago -= 5
                        print(f"Te haz curado 15 puntos vitales, tu HP restante : {hpmago}.\n Maná restante : {manamago}.")
                    else:
                        print("No tienes suficiente maná, no puedes curarte.")
                elif accion == 4:
                    print("No puedes huir en este combate, que lamentable.")
            imprimir("Al derrotar al jefe quedas exhausto del combate, decides tomar el botín que estaba a su lado y regresar al gremio para descansar.")
            print("==== AVENTURA FINALIZADA ====")

        elif clase == 2:
            print("")

        elif clase == 3:
            print("")

    elif mision == 2:
        if clase == 1:
            imprimir("Te armas de valor, sabes que probablemente no regreses con vida...",0.01, "Pero vale la pena intentarlo.")
            
        elif clase == 2:
            print("")
        elif clase == 3:
            print("")
        
    else:
        print("Escoja una misión disponible porfavor.")
else:
    print("Hasta la próxima jugador(a). )")
