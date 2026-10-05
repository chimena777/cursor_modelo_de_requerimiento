from servicio.saludo_service import SaludoService


def registrar_datos(servicio: SaludoService) -> None:
    print("\n--- Registrar datos ---")
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    hora = input("Hora (HH:MM, 24h): ")
    try:
        estudiante = servicio.registrar(nombre, edad, hora)
        print(
            f"Datos guardados: {estudiante.nombre}, "
            f"{estudiante.edad} años, {estudiante.hora}."
        )
    except ValueError as e:
        print(f"Error: {e}")


def solicitar_saludo(servicio: SaludoService) -> None:
    print("\n--- Saludo ---")
    try:
        print(servicio.saludar())
    except ValueError as e:
        print(f"Error: {e}")


def menu() -> None:
    servicio = SaludoService()
    print("=== Sistema de saludo al estudiante ===")

    while True:
        print("\n1. Ingresar / actualizar datos")
        print("2. Solicitar saludo")
        print("3. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            registrar_datos(servicio)
        elif opcion == "2":
            solicitar_saludo(servicio)
        elif opcion == "3":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida. Elija 1, 2 o 3.")


if __name__ == "__main__":
    menu()
