print("Bienvenido aventurer@, ¿Estarás listo para el camino que te espera?")
nombre = input("¿Cuál es tu nombre? ")
print(f"Oh, con que {nombre}, sin duda un nombre para un heroe.")
print("¿Qué clase de aventurer@ quieres ser?")
Caballero = 1
Mago = 2
Asesino = 3
Arquero = 4
clase = int(input("1) Caballero, 2) Mago, 3) Asesino, 4) Arquero"))
if clase == 1:
    print("Has escogido ser un caballero, tus estadisticas son las siguientes: ")
    print("Vida: 100")
    print("Fuerza: 10")
    print("Defensa : 8")
    print("Agilidad: 5")
    print("Magia: 0")
elif clase == 2:
    print("Has escogido ser un mago, tus estadisticas son las siguientes: ")
    print("Vida: 70")
    print("Fuerza: 3")
    print("Defensa : 4")
    print("Agilidad: 6")
    print("Magia: 10")
elif clase == 3:
    print("Has escogido ser un asesino, tus estadisticas son las siguientes: ")
    print("Vida: 80")
    print("Fuerza: 15")
    print("Defensa : 5")
    print("Agilidad: 10")
    print("Magia: 0")
else:
    print("Has escogido ser un arquero, tus estadisticas son las siguientes: ")
    print("Vida: 90")
    print("Fuerza: 8")
    print("Defensa : 6")
    print("Agilidad: 12")
    print("Magia: 5")

print("Ya decisite que clase de aventurer@ quieres ser, ahora es momento de elegir tu primera ruta, ¿Qué camino quieres tomar?")
Bosque = 1
Montaña = 2
Cueva = 3
Ruta = int(input("1) Bosque, 2) Montaña, 3) Cueva"))
if Ruta == 1:
    print("Has elegido el bosque, puede ser tranquilo durante el día, pero se precavid@ en la noche, el peligro acecha en cada esquina.")
    print("Mientras caminas cerca de los arboles, sientes una presencia detras de ti, te das la vuelta y es un Golem, una criatura bastante resistente.")
    print("¡Rápido!, escoge tu acción: ")
    print("1) Atacar, 2) Defender, 3) Huir")
    Atacar = 1
    Defender = 2
    Huir = 3
    accion = int(input("¿Qué acción quieres realizar? "))
    if accion == 1:
        print("Decidiste atacar al Golem, tu destreza y fuerza son increibles, terminas derrotando al Golem en segundos")
    elif accion == 2:
        print("Decidiste defenderte y esperar a lograr un contraataque")
        print("No te esperabas la rapidez y fuerza del Golem, recibes el golpe pero logras lanzar un contraataque, ganas el combate con dificultad")
    else:
        print("Decidiste huir del Golem, consideras que es una perdida de tiempo enfrentarlo")
    
    print("Sigues tu camino por el bosque y te percatas de un escandalo, te decides acercar.")
    print("De lo poco que puedes ver entre los arbustos, aparentemente es un grupo de siete bandidos y también al parecer una entidad elfica")
    print("Decides intervenir, pero primero piensas como: ")
    print("1) Atacar de frente, 2) Planear un asalto, 3) Probar la negociación")
    Atacar = 1
    Planear = 2
    Negociar = 3
    accion = int(input("¿Qué acción quieres realizar? "))
    if accion == 1:
        print("Decidiste atacar de frente contra los siete bandidos, son habiles pero no más que tú")
        print("Tras una ardua pelea, logras vencer pero con varias heridas y apuñaladas")
    elif accion == 2:
        print("Te ocultas entre las gruesas ramas de los arboles y embistes a dos bandidos que estaban separados del grupo")
        print("Consecutivamente obliteras a otros tres y quedas contra los ultimos dos de frente")
        print("Tus habilidades de combate llegan a ser superiores a manos desnudas y logras derrotar al grupo de bandidos")
    else:
        print("Decides probar la negociación, pero te obligan a entregar tus pertenencias y todo lo de valor en tu posesión.")
        print("")
elif Ruta == 2:
    print("Has elegido la montaña, el camino es difícil y peligroso, pero las vistas son impresionantes, ten cuidado con los acantilados.")
else:
    print("Has elegido la cueva, es un lugar oscuro y húmedo, lleno de misterios y peligros, asegúrate de llevar una antorcha.")

