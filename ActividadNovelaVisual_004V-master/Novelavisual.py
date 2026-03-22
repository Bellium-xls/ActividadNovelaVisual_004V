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
        print("La entidad elfica se acerca hacia ti y como muestra de su gratitud te ofrece un poco de su sangre para curarte las heridas")
        print("¿Decides confiar en la elfica?")
        print("1)Decides confiar y aceptar su sanger, 2)Decides desconfiar y negarle su sangre")
        confiar =  1   
        desconfiar = 2
        accion = int(input("¿Decides confiar?"))
        if accion == 1:
            print("Decides confiar y aceptas su sangre, la bebes, sientes como regeneras energias y todo tu cuerpo tiembla")
        else:
            print("Decides desconfiar y rechazas coordial mente su regalo de gratitud ")

    elif accion == 2:
        print("Te ocultas entre las gruesas ramas de los arboles y embistes a dos bandidos que estaban separados del grupo")
        print("Consecutivamente obliteras a otros tres y quedas contra los ultimos dos de frente")
        print("Tus habilidades de combate llegan a ser superiores a manos desnudas y logras derrotar al grupo de bandidos")
    else:
        print("Decides probar la negociación, pero te obligan a entregar tus pertenencias y todo lo de valor en tu posesión.")
        
elif Ruta == 2:
        print("Has elegido la montaña, el camino es difícil y peligroso, pero las vistas son impresionantes, ten cuidado con los acantilados.")
        print("Mientras caminas por las montañas, te percatas de humo, signifiacado de bandidos cerca,")
        print("Decides seguir el humo, y mientras te vas acercando te percatas de cadaveres y huesos tirados por todos lados, ")
        print("Llegas a donde proviene el humo y ves un campamento bandido destruido y muchos muertos,")
        print("Te acercas para investigar, y de repente empieza a temblar el suelo, el terreno solido se empieza a agrietar, Detras de unas montañas, aparece una silueta oscura con ojos blancos brillantes, la silueta te mira mientras tu la observas,")
        print("un escalofrio recorre todo tu cuerpo y sientes un mal presentimiento, la silueta oscura se va acercando con lentitud hacia ti")
        print("¿Que acción quieres realizar?")
        print("1) Huir, 2) Huir, 3) HUIR, 4) Atacar")
        Huir = 1-2
        HUIR = 3
        Atacar = 4
        accion = int(input("¿Que acción quieres realizar?"))
        if accion ==1-2:
            print("Decides correr como una gallina, pero no te servira de nada ya que la silueta oscura se da cuenta de tu acción y empieza a preseguirte, la silueta ocura es más rapida y alcanza a agarrarte, te agarra con sus dos manos y meintras tu gritas de dolor, te parte en dos terminando con tu agonía")
        elif accion == 3:
            print("Al tener miedo extremo, te paralizas, solo puedes observar como la solueta oscura se va acercando poco a poco, deformando su cara y exponiendo si horrible rostro, te das cuenta de que es el mismismo satanás, la silueta oscura te agarra, y meintras tu no puedes hacer nada, te acerca para olfatearte, se burlta de ti y luego te va metiendo en su boca lentamente para luego masticarte, muriendo y terminando con tu existencia")
        elif accion == 4:
            print("Decides hacerte el valiente, corres hacia la silueta oscura, la silueta oscura te lanza arboles y rocas, tu con mucha facilidad esquivas todo lo que te lanza, subes una montaña y te lanzas de cara contra la criatura, confiado de que ganaras, no te percatas de sus cuernos y te atravieza con uno, cegado por la confianza y el ego, terminas empalado muriendo al instante")

else:
        print("Has elegido la cueva, es un lugar oscuro y húmedo, lleno de misterios y peligros, asegúrate de llevar una antorcha.")
    