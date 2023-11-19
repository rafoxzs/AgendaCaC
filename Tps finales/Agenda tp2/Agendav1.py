agenda = {}


def add_contacto(nombre, telefono, email, direccion):
    if nombre in agenda:  # verifica si el nombre ya esta en la agenda
        print("el contacto ya se encuentra agendado")
    else:
        agenda[nombre] = {"telefono": telefono,
                          "email": email, "direccion": direccion}
        print(f"Contacto '{nombre}' agregado correctamente.")


def mod_contacto(nombre, telefono, email, direccion):
    if nombre in agenda:  # verifica si el nombre ya esta en la agenda
        agenda[nombre] = {"telefono": telefono,
                          "email": email, "direccion": direccion}
        print(f"Contacto '{nombre}' modificado correctamente.")
    else:
        print("el contacto no se encuentra agendado")


def elim_contacto(nombre):
    if nombre in agenda:  # verifica si el nombre ya esta en la agenda
        del agenda[nombre]

    else:
        print("el contacto no se encuentra agendado")


def cons_contacto(nombre):
    if nombre in agenda:
        print(f"nombre : {nombre}")
        print(f"Telefono : {agenda[nombre]['telefono']}")
        print(f"email: {agenda[nombre]['email']}")
        print(f"Dirección: {agenda[nombre]['direccion']}")
    else:
        print("El contacto no existe en la agenda.")


def main():
    while True:
        print("\n1. Agregar contacto")
        print("2. Modificar contacto")
        print("3. Eliminar contacto")
        print("4. Consultar contacto")
        print("5. Salir")
        opcion = int(input("Selecciona una opción: "))
        match opcion:
            case 1:
                # aca hay que meter una comprobacion que sean todas letras
                nombre = input("ingrese el nombre :")
                # aca hay que meter una comprobacion que sean todos numeros
                telefono = input("ingrese el telefono :")
                # hay que poner una comprobacion que detecte el arroba y el .com
                email = input("ingrese el Email :")
                # nidea que comprobacion meterle
                direccion = input("ingrese direccion :")
                add_contacto(nombre, telefono, email, direccion)
            case 2:
                # aca hay que meter una comprobacion que sean todas letras
                nombre = input("nombre del contacto a modificar :")
                # aca hay que meter una comprobacion que sean todos numeros
                telefono = input("telefono nuevo :")
                # hay que poner una comprobacion que detecte el arroba y el .com
                email = input("email nuevo :")
                # nidea que comprobacion meterle
                direccion = input("nueva direccion :")
                mod_contacto(nombre, telefono, email, direccion)
            case 3:
                nombre = input("nombre del contacto a eliminar :")
                elim_contacto(nombre)
            case 4:
                nombre = input("nombre del contacto a consultar :")
                cons_contacto(nombre)
            case 5:
                print("Hasta luegito!")
                break
            case _:
                print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()


# to do list
#    - usbirlo a github y empezar a usar control de versiones
#    - implementar funciones de comprobacion
#    - funcion que me muestre todos los contactos agendados
#    - guardar en archivo
#    -guardarlos con base de datos
#    - interfaz grafica
#
#
#
#
