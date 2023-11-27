# import permite acceder a un modulo dentro de python. El modulo "random" permite trabajar sobre la aleatoriedad.
import random

# Cada uno le pone la ruta en la cual lo tiene TIP: copiar ruta de acceso relativa y le cambian el sentido de las barras
ruta = "Tps finales/ahorcado/"


def palabras_faciles():  # Se crea una funcion para cada dificultad del juego.
    palabras = ['perro', 'gato', 'mesa', 'silla', 'variable', 'imprimir',
                'lista', 'suma', 'computadora', 'programa', 'pajaro', 'pelota']
    return random.choice(palabras)


def palabras_intermedias():
    palabras = ['elefante', 'leopardo', 'heladera', 'ventilador', 'condicion',
                'diccionario', 'bucle', 'funcion', 'algoritmo', 'iteracion', 'cocodrilo', 'teclado']
    return random.choice(palabras)


def palabras_dificiles():
    palabras = ['quimera', 'ornitórrinco', 'microscopio', 'espectroscopio', 'polimorfismo', 'abstraccion',
                'herencia', 'recursividad', 'electrico', 'monosacarido', 'anfibio', 'biodegradabilidad']
    return random.choice(palabras)


# Definimos una funcion para mostrar las casillas a llenar.
def mostrar_tablero(palabra, letras_adivinadas):
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    # Elimina los espacios en blanco al principio y al final de una cadena.
    return resultado.strip()


def select_dif():
    print("Selecciona la dificultad: ")
    print("1. Facil")
    print("2. Normal")
    print("3. Dificíl")

    while True:
        dificultad = int(input(""))
        match dificultad:
            case 1:
                palabra_secreta = palabras_faciles()
                return palabra_secreta
            case 2:
                palabra_secreta = palabras_intermedias()
                return palabra_secreta
            case 3:
                palabra_secreta = palabras_dificiles()
                return palabra_secreta


def jugar(palabra_secreta):
    # esto hay que pasarselo todo desde la otra funcion
    palabra_secreta = palabras_faciles()
    intentos_restantes = 6
    letras_adivinadas = []
    puntos = 0

    palabra_oculta = "_" * len(palabra_secreta)

    while intentos_restantes > 0:
        print(mostrar_tablero(palabra_secreta, letras_adivinadas))
        letra = input("Ingresa una letra: ").lower()

        if letra in letras_adivinadas:
            print("¡Ya adivinaste esa letra! Ingresa una nueva letra.")
        if letra in palabra_secreta:
            # Agregar la letra acertada a las letras adivinadas
            letras_adivinadas.append(letra)
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    palabra_oculta = palabra_oculta[:i] + \
                        letra + palabra_oculta[i+1:]
                    puntos += 1
                    print("\nPuntos: ", puntos)  # Muestra el puntaje actual
            print("Buen trabajo!, la palabra es:", palabra_oculta)
            # Para registrar el puntaje obtenido.
            print(f"Total de puntaje: {puntos}")

        else:
            intentos_restantes -= 1
            print(f"Incorrecto. Te quedan {intentos_restantes} intentos.")

        if "_" not in palabra_oculta:
            print("¡Felicidades! Descubriste la palabra!")
            break

        if intentos_restantes == 0:
            print("\n O")
            print("/|\\")
            print("/ \\")
            print("\n¡Oh no! Te quedaste sin intentos. La palabra era:",
                  palabra_secreta)
        if intentos_restantes == 5:
            print("\nO")
        elif intentos_restantes == 4:
            print("\nO")
            print("|")
        elif intentos_restantes == 3:
            print("\n O")
            print("/|")
        elif intentos_restantes == 2:
            print("\n O")
            print("/|")
            print("/")
        elif intentos_restantes == 1:
            print("\n O")
            print("/|\\")
            print("/")

    nombre_jugador = input("Ingresa tu nombre para registrar tu puntaje: ")
    with open(ruta + "Puntaje.txt", "a") as puntaje:
        puntaje.write(f"{nombre_jugador}: {puntos}\n")


def show_creditos():
    printed_message = False

    while True:
        if not printed_message:
            print("\nTrabajo practico Python CAC inicial.\n")
            print("Juego de ahorcado, en consola.")
            print("\nRealizado por el grupo D integrantes:")
            print("\nBLABLABLA\n")
            printed_message = True

        input("Presiona enter para continuar")
        break


def show_puntajes():

    jugadores = {}

    with open(ruta + "Puntaje.txt", "r") as puntaje:
        lineas = puntaje.readlines()

        for linea in lineas:
            datos = linea.split(',')
            if len(datos) == 2:  # Verificar que haya dos elementos separados por coma
                nombre, puntaje = datos
                jugadores[int(puntaje)] = nombre.strip()

    puntajes_ordenados = sorted(jugadores.keys(), reverse=True)
    mejores_puntajes = [(jugadores[puntaje], puntaje)
                        for puntaje in puntajes_ordenados]

    for nombre, puntaje in mejores_puntajes:
        print(f"{nombre}: {puntaje}")

    input("Presiona Enter para continuar...")


def main():
    print("Bienvenido al juego del ahorcado.\n")
    print("Las reglas son simples. La computadora elige una palabra al azar y debes adivinar la palabra correcta indicando una letra a la vez. ")
    print("\nCada acierto te muestra la letra que adivinaste en el lugar que tiene en la palabra.")
    print("\nTienes 6 intentos para adivinar. Cada acierto suma un punto!\n")
    while True:

        print("1. Ver puntajes.")
        print("2. Jugar.")
        print("3 Creditos")
        print("4. Salir")
        opcion = int(input("\nSelecciona una opción: "))
        match opcion:
            case 1:  # muestra los puntajes
                show_puntajes()
            case 2:
                palabra_secreta = select_dif()
                jugar(palabra_secreta)
            case 3:
                show_creditos()
            case 4:
                print("Hasta luegito!")
                break
            case _:
                print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()


# Cosas que fui cambiando
# - Estructure el codigo , en funciones para que sea mas ordenado
# - la lista letras_adivinadas , puntos , vidas paso a la funcion jugar , en ves de definirla en cada nivel de dificultad , que solo devuelve la palabra
# - los input ya los tomo como INT , asi te ahorras todo el codigo que chekea que sea int , y sino lo convierte
# - Agregue la funcion show_creditos , que muestra los creditos , podriamos hacer uns lista con los miembros del grupo , para no complicarla leyendo un archivo
# - Agregue la funcion show_puntajes , agarra el txt , separa los valores , los ordena de mayor a menor y los muestra en pantalla
#
#
# COSAS Q faltarian hacer

# - que se pueda seguir jugando cuando ganas
# - que el puntaje lo pida una ves que perdes
