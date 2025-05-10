from datetime import datetime
from services.utils import cargar_json, guardar_json, obtener_medicamento

def compras():
    PATH_MEDICAMENTOS = "data/Medicamentos.json"
    PATH_COMPRAS = "data/Compras.json"

    medicamentos = cargar_json(PATH_MEDICAMENTOS)
    compras = cargar_json(PATH_COMPRAS)

    # Pedir datos del proveedor solo una vez
    nombre_proveedor = input("Ingrese el nombre del proveedor: ").strip()
    contacto_proveedor = input("Ingrese el contacto del proveedor: ").strip()

    while True:
        medicamento = obtener_medicamento(medicamentos)

        if medicamento is None:
            print("❌ Compra cancelada.")
            break

        if not medicamento:
            nombre_medicamento = input("Ingrese el nombre del nuevo medicamento: ").strip().title()
            cantidad = int(input(f"Ingrese la cantidad de '{nombre_medicamento}' a comprar: "))
            precio = float(input(f"Ingrese el precio de compra de '{nombre_medicamento}': "))
            fecha_expiracion = input(f"Ingrese la fecha de expiración de '{nombre_medicamento}' (YYYY-MM-DD): ")

            nuevo_medicamento = {
                "nombre": nombre_medicamento,
                "precio": precio,
                "stock": cantidad,
                "fechaExpiracion": f"{fecha_expiracion}T00:00:00Z",
                "proveedor": {
                    "nombre": nombre_proveedor,
                    "contacto": contacto_proveedor
                }
            }

            medicamentos.append(nuevo_medicamento)
            print(f"✅ Medicamento '{nombre_medicamento}' agregado al inventario con {cantidad} unidades.")
        else:
            nombre_medicamento = medicamento["nombre"]
            cantidad = int(input(f"Ingrese la cantidad de '{nombre_medicamento}' a comprar: "))
            precio = float(input(f"Ingrese el precio de compra de '{nombre_medicamento}': "))
            fecha_expiracion = input(f"Ingrese la fecha de expiración de '{nombre_medicamento}' (YYYY-MM-DD): ")

            # Actualizar el medicamento existente
            for m in medicamentos:
                if m["nombre"] == nombre_medicamento:
                    m["stock"] += cantidad
                    m["precio"] = precio  # opcional: podrías preguntar si se desea actualizar
                    m["fechaExpiracion"] = f"{fecha_expiracion}T00:00:00Z"
                    m["proveedor"] = {
                        "nombre": nombre_proveedor,
                        "contacto": contacto_proveedor
                    }
                    print(f"✅ Stock de '{nombre_medicamento}' actualizado a {m['stock']} unidades.")
                    break

        # Registrar la compra
        registro_compra = {
            "fechaCompra": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "proveedor": {
                "nombre": nombre_proveedor,
                "contacto": contacto_proveedor
            },
            "medicamentosComprados": [
                {
                    "nombreMedicamento": nombre_medicamento,
                    "cantidadComprada": cantidad,
                    "precioCompra": precio,
                    "fechaExpiracion": fecha_expiracion
                }
            ]
        }

        compras.append(registro_compra)
        guardar_json(PATH_MEDICAMENTOS, medicamentos)
        guardar_json(PATH_COMPRAS, compras)

        print("✅ Compra registrada correctamente.")

        continuar = input("\n¿Desea registrar otra compra? (s/n): ").strip().lower()
        if continuar != 's':
            break
