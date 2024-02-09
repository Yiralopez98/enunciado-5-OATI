from utils.logica import agregar_serie, modificar_serie, eliminar_serie, listar_series

# Función principal para interactuar con la aplicación
def main():
    while True:
        print("Bienvenido a la aplicación de gestión de series y directores.")
        print("Seleccione una opción:")
        print("1. Agregar serie")
        print("2. Modificar serie")
        print("3. Eliminar serie")
        print("4. Agregar director")
        print("5. Listar series")
        print("6. Salir")
        
        opcion = input("Opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título de la serie: ")
            fecha_lanzamiento = input("Ingrese la fecha de lanzamiento de la serie: ")
            descripcion = input("Ingrese la descripción de la serie: ")
            agregar_serie(titulo, fecha_lanzamiento, descripcion)
        elif opcion == "2":
            serie_id = input("Ingrese el ID de la serie que desea modificar: ")
            nuevo_titulo = input("Ingrese el nuevo título de la serie (deje en blanco para mantener el mismo): ")
            nuevo_fecha_lanzamiento = input("Ingrese la nueva fecha de lanzamiento de la serie (deje en blanco para mantener la misma): ")
            nueva_descripcion = input("Ingrese la nueva descripción de la serie (deje en blanco para mantener la misma): ")
            modificar_serie(serie_id, nuevo_titulo, nuevo_fecha_lanzamiento, nueva_descripcion)
        elif opcion == "3":
            serie_id = input("Ingrese el ID de la serie que desea eliminar: ")
            eliminar_serie(serie_id)
        elif opcion == "4":
            print("Función de agregar director aún no implementada.")
        elif opcion == "5":
            listar_series()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()