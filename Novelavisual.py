nombre = input("Antes de comenzar, ingrese su nombre de usuario")
print(nombre)
print(f"Bienvenido {nombre}, estabamos esperando tu llegada al gremio")

Caballero = 1
Mago = 2
Paladín = 3
Asesino = 4
Prisionero = 5

print("1)Caballero  2)Mago  3)Paladín   4)Asesino   5)Prisionero")
clase = int(input("¿Que clase escogeras para tu aventura?"))
if clase == 1:
    print("Haz escogido la clase Caballero, tus estadisticas son:")
    print("HP: 100")
    print("ATK: 60")
    print("PODER MÁGICO: 0")
    print("DEFENSA: 75")
elif clase == 2:
    print("Haz escogido la clase Mago, tus estadisticas son:")
    print("HP: 90")
    print("ATK: 10")
    print("PODER MÁGICO: 70")
    print("DEFENSA: 50")
elif clase == 3:
    print("Haz escogido la clase Paladín, tus estadisticas son:")
    print("HP: 80")
    print("ATK: 45")
    print("PODER MÁGICO: 10")
    print("DEFENSA: 150")
elif clase == 4:
    print("Haz escogido la clase Asesino, tus estadisticas son:")
    print("HP: 70")
    print("ATK: 100")
    print("PODER MÁGICO: 40")
    print("DEFENSA: 30")
else:
    print("Haz escogido ser un Prisionero, Dios se apiade de tu aventura.")
    print("HP: 100")
    print("ATK: 10")
    print("PODER MÁGICO: 10")
    print("DEFENSA: 10")

print("Ahora que ya has escogido tu clase, es hora de comenzar tu aventura")
print(f"{nombre} se adentra en una mazmorra en ruinas.")
print("El viento aulla, el frío te hace sentir intranquilo y la oscuridad es tu único compañero.")
print("1)Te armas de valor y entras en la mazmorra  2)Tal vez para otro momento.    3) Padre nuestro y con fé entras a la mazmorra")
decision = int(input("¿Que haras?"))
if decision == 1:
    print("La mazmorra aparentemente no está vacía, hay sangre fresca entre las lugubres paredes.")
    print(f"Escuchas un estruendo y te pones en alerta, {nombre} se prepara para lo que pueda venir.")
    print("Aparece una criatura grotesca, no parece producir ningún sonido, es rápido pero aparentemente es débil")
    Atacar = 1
    Huir = 2
    Defender = 3
    print("1)No es rival para ti.  2)Me da miedo.  3)Puedo con esto.")
    accion = int(input("¿Qué harás?"))
    if 


elif decision == 2:
