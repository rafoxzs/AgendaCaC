import csv

agenda = {}
contacts = 'Tps finales/Agenda tp2/agenda.csv'


def add_contacto(nombre, telefono, email, direccion):
    if nombre in agenda:  # verifica si el nombre ya esta en la agenda tipo de dato , de borra claramente cuando reinicio
        print("el contacto ya se encuentra agendado")
    else:
        agenda[nombre] = {"telefono": telefono,
                          "email": email, "direccion": direccion}

        with open(contacts, 'a', newline='') as archivo_csv:  # lo guarda en la base de datos csv

            escritor_csv = csv.writer(archivo_csv)
            if archivo_csv.tell() == 0:
                escritor_csv.writerow(
                    ["Nombre", "Teléfono", "Email", "Dirección"])

            escritor_csv.writerow([nombre, telefono, email, direccion])

        print(f"Contacto '{nombre}' agregado correctamente.")


def mod_contacto(nombre, telefono, email, direccion):
    if nombre in agenda:  # verifica si el nombre ya esta en la agenda
        agenda[nombre] = {"telefono": telefono,
                          "email": email, "direccion": direccion}
        print(f"Contacto '{nombre}' modificado correctamente.")
    else:
        print("el contacto no se encuentra agendado")


def elim_contacto(nombre):
    contactos_actualizados = []
    encontrado = False
    with open(contacts, 'r', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        # recorre cada fila del archivo CSV
        for fila in lector_csv:
            # Si el nombre coincide se encontroo el contact
            if fila[0] == nombre:
                encontrado = True
                continue
            contactos_actualizados.append(fila)
    with open(contacts, 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerows(contactos_actualizados)
    print(f"El contacto '{nombre}' se ah eliminado.")
    if not encontrado:
        print(f"El contacto '{nombre}' no se encuentra en la agenda.")


def cons_contacto(nombre):
    encontrado = False
    with open(contacts, 'r', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        # recorre cada fila del archivo CSV
        for fila in lector_csv:
            # Si el nombre coincide se encontroo el contact
            if fila[0] == nombre:
                telefono = fila[1]
                email = fila[2]
                direccion = fila[3]
                print(f"Contacto:{nombre}")
                print(f"Teléfono: {telefono}")
                print(f"Email: {email}")
                print(f"Dirección: {direccion}")
                encontrado = True
    if not encontrado:
        print(f"El contacto '{nombre}' no se encuentra en la agenda.")


def verif_name():
    while True:
        nombre = input("ingrese el nombre :")
        if nombre.replace(" ", "").isalpha() or nombre.replace("-", "").isalpha() or nombre.replace("'", "").isalpha():
            return str(nombre)
        else:
            print("Por favor, ingrese un nombre y apellido valido.")


def verif_tel():
    while True:
        telefono = input("ingrese el telefono :")
        if len(str(telefono)) > 6 and telefono.isdigit():
            return int(telefono)
        else:
            print("Por favor, ingrese un telefono valido.")


def verif_email():
    while True:
        email = input("ingrese el email :")
        if "@" in email and "." in email[email.index("@"):]:
            return str(email)
        else:
            print("Por favor, ingrese un email valido.")


def main():
    while True:
        print("\n1. Agregar contacto")
        print("2. Modificar contacto")
        print("3. Eliminar contacto")
        print("4. Consultar contacto")
        print("5. Salir")
        opcion = int(input("\nSelecciona una opción: "))
        match opcion:
            case 1:
                nombre = verif_name()
                telefono = verif_tel()
                email = verif_email()
                direccion = input("ingrese direccion :")
                add_contacto(nombre, telefono, email, direccion)
            case 2:
                print("Modificar contacto")
                nombre = verif_name()
                telefono = verif_tel()
                email = verif_email()
                direccion = input("nueva direccion :")
                mod_contacto(nombre, telefono, email, direccion)
            case 3:
                print("Eliminar contacto")
                nombre = verif_name()
                elim_contacto(nombre)
            case 4:
                print("Consultar contacto")
                nombre = verif_name()
                cons_contacto(nombre)
            case 5:
                print("Hasta luegito!")
                break
            case _:
                print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()


# to do list
#    - tenerlo funcionando con un diccionario , sin comprobaciones , menu basico.
#    - usbirlo a github y empezar a usar control de versionesa  ok
#    - implementar funciones de comprobacion OK YA TA FALTARIA VER COMO HACER PARA QUE DEPENDIENDO SEA EL CASO , AGREGAR O MODIFICAR CAMBIE EL PRINT DE CADA F
#    - funcion que me muestre todos los contactos agendados
#    - guardar en archivo  // lo hacemos directamente en CSV .  .dat es una paja para esto
#
#    - interfaz grafica
#
#
#
# #Verificar cambios: Antes de hacer un commit, verifica los cambios que se van a incluir con git status. Esto te mostrará qué archivos han sido modificados, agregados o eliminados.

# Agregar archivos: Usa git add <nombre_archivo> para agregar archivos específicos o git add . para incluir todos los archivos modificados en el commit.

# Realizar el commit: Ejecuta git commit -m "Mensaje descriptivo aquí" para confirmar los cambios. Es importante incluir un mensaje claro que describa los cambios realizados.

# Verificar el estado: Después del commit, puedes usar nuevamente git status para asegurarte de que no haya más cambios pendientes por agregar.

# Recuerda que estos pasos te permiten guardar tus cambios de forma local. Para enviar los cambios al repositorio remoto, se usa git push.
