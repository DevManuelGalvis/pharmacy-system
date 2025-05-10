from models.ventas import ventas
from models.compras import compras

def menu_principal():
    print("Bienvenido al sistema de gestión de farmacia")
    while True:
        print("\n¿Qué desea hacer?")
        print("1. Registrar una venta")
        print("2. Registrar una compra")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1/2/3): ").strip()

        if opcion == '1':
            ventas()  # Llamada al módulo de ventas
        elif opcion == '2':
            compras()  # Llamada al módulo de compras
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor seleccione una opción válida.")

if __name__ == "__main__":
    menu_principal()
