canciones = []

while True:
    print("Menú:")
    print("1. Registrar canción")
    print("2. Mostrar canciones")
    print("3. Modificar canción")
    print("4. Eliminar canción")
    print("5. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == '1':
        nombre = input("Nombre de la canción: ")
        autor = input("Autor de la canción: ")
        cantante = input("Cantante de la canción: ")
        album = input("Álbum en el que salió la canción: ")
        año = input("Año del álbum: ")

        cancion = {
            'nombre': nombre,
            'autor': autor,
            'cantante': cantante,
            'album': album,
            'año': año
        }

        canciones.append(cancion)
        print("Canción registrada con éxito.")

    elif opcion == '2':
        print("Canciones registradas:")
        for i, cancion in enumerate(canciones):
            print(f"{i+1}. {cancion['nombre']} - {cancion['cantante']} ({cancion['año']})")

    elif opcion == '3':
        indice = int(input("Ingrese el número de la canción que desea modificar: ")) - 1
        if 0 <= indice < len(canciones):
            cancion = canciones[indice]
            print(f"Canción seleccionada: {cancion['nombre']} - {cancion['cantante']} ({cancion['año']})")
            opcion_mod = input("¿Qué campo desea modificar? (nombre, autor, cantante, album, año): ")
            if opcion_mod in cancion:
                nuevo_valor = input(f"Ingrese el nuevo valor para {opcion_mod}: ")
                cancion[opcion_mod] = nuevo_valor
                print("Canción modificada con éxito.")
            else:
                print("Opción inválida.")
        else:
            print("Número de canción inválido.")

    elif opcion == '4':
        indice = int(input("Ingrese el número de la canción que desea eliminar: ")) - 1
        if 0 <= indice < len(canciones):
            cancion = canciones[indice]
            confirmacion = input(f"¿Está seguro de que desea eliminar la canción {cancion['nombre']} - {cancion['cantante']} ({cancion['año']})? (s/n): ")
            if confirmacion == 's':
                canciones.pop(indice)
                print("Canción eliminada con éxito.")
        else:
            print("Número de canción inválido.")

    elif opcion == '5':
        print("Saliendo de la aplicación...")
        break

    else:
        print("Opción inválida.")

    print()  # Imprimir una línea en blanco para separar las opciones.