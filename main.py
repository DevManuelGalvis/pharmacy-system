from models.ventas import ventas
from models.compras import compras
from services.auth import iniciar_sesion

def menu_principal():
    print("📦 Bienvenido al sistema de gestión de farmacia")

    rol = None
    while not rol:
        rol = iniciar_sesion()

    while True:
        print("\n¿Qué desea hacer?")
        print("1. Registrar una venta")
        print("2. Registrar una compra")
        if rol in ['administrador', 'gerente']:
            print("3. Ver reportes")
            print("4. Salir")
        else:
            print("3. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            ventas()
        elif opcion == '2':
            compras()
        elif opcion == '3':
            if rol in ['administrador', 'gerente']:
                print("📊 Módulo de reportes aún en desarrollo...")
            else:
                print("👋 ¡Hasta luego!")
                break
        elif opcion == '4' and rol in ['administrador', 'gerente']:
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida.")



	

if __name__ == "__main__":
    menu_principal() 