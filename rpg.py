nombre = input("ingrese tu nombre aventurero:")

print("...DESPERTASTE")
print(f"{nombre}:¿donde estoy? ¿que es este lugar?")
print("(vez a tu alrededor y solo ves oscuridad)")
print("a lo lejos vez una ventana y estas en una especie de pieza")

while True:
    print(" 1.ver afuera de la ventana\n 2.buscar la puerta")

    opciones = int(input("que haras ahora :"))
    opcion_1 = 1
    opcion_2 = 2

    if opciones == 1:
        print("ves afuera de la ventana.... solo vez niebla")
        
    else :
        opciones == 2
        print("encuentras una puerta y intentas abrirla")
        break

print("sales de una especie de celda")
print(f"{nombre}: ¿como llegue hasta aca? porque hay un pasillo tan largo?")
print(f"{nombre}: no veo el final")
print("ves muchas puertas y cada una tiene un texto diferente")
print("llegas a la primera puerta a mano derecha, tiene una fecha ")
print(" 23/08/1960")
print("te entra una jaqueca enorme")

while True:
    print("1.entrar en la puerta?\n2.seguir a la siguiente")
    print(" (si sigues tu camino no habra regreso atras) ")
    opciones = int(input("que haras ahora?:"))
    opcion_1 = 1
    opcion_2 = 2
    if opcion_1 == 1:
        print(" regresas a la fecha exacta.. 23/08/1960")
    else:
        opcion_2 == 2
        print("llegas a la siguiente puerta a mano izquierda")
        break
print("al abrir la puerta ves un salón enorme")
print("las paredes están cubiertas de relojes, todos marcando horas distintas")
print(f"{nombre}: ¿qué significa todo esto?")
print("en el centro hay un espejo antiguo, con tu reflejo mirándote fijamente")
print("pero tu reflejo sonríe... y te habla")

print(f"{nombre}: ¡¿qué está pasando?!")
print("reflejo: 'Has cruzado el pasillo del tiempo. Cada puerta era un destino posible.'")
print("reflejo: 'Ahora debes elegir: quedarte atrapado en un recuerdo... o seguir adelante.'")

while True:
    print("1. Romper el espejo\n2. Aceptar tu reflejo y entrar en él")
    decision = int(input("¿Qué harás ahora?:"))
    if decision == 1:
        print("rompes el espejo... la oscuridad te envuelve")
        print("cuando abres los ojos, despiertas en tu cama. ¿Fue todo un sueño?")
        break
    elif decision == 2:
        print("tocas el espejo y tu reflejo te absorbe")
        print("te conviertes en parte del pasillo eterno, guardián de las puertas del tiempo")
        print("tu historia termina... pero el pasillo sigue esperando nuevos aventureros")
        break

