import os
import json
from datetime import datetime
from services.utils import cargar_json, guardar_json
from models.pacientes import registrar_paciente


def obtener_medicamento(medicamentos):
    while True:
        nombre = input("Ingrese el nombre del medicamento (o 'cancelar' para salir): ").strip().title()
        if nombre.lower() == "cancelar":
            return None
        medicamento = next((m for m in medicamentos if m["nombre"] == nombre), None)
        if medicamento:
            return medicamento
        print(f"❌ El medicamento '{nombre}' no está en el inventario. Intente de nuevo.")

def obtener_cantidad(stock_disponible):
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del medicamento: "))
            if cantidad <= 0:
                print("❌ La cantidad debe ser mayor a cero.")
            elif cantidad > stock_disponible:
                print(f"❌ Solo hay {stock_disponible} unidades disponibles.")
            else:
                return cantidad
        except ValueError:
            print("❌ Ingrese un número válido para la cantidad.")


def ventas():
    PATH_MEDICAMENTOS = "data/Medicamentos.json"
    PATH_VENTAS = "data/Ventas.json"

    medicamentos = cargar_json(PATH_MEDICAMENTOS)
    ventas = cargar_json(PATH_VENTAS)

    if not medicamentos:
        print("⚠️ No hay medicamentos registrados en el inventario.")
        return

    # Datos del paciente y empleado
    nombre_paciente = input("Ingrese el nombre del paciente: ").strip()
    direccion_paciente = input("Ingrese la dirección del paciente: ").strip()
    telefono_paciente = input("Ingrese el teléfono del paciente: ").strip()
    nombre_empleado = input("Ingrese el nombre del empleado: ").strip()
    cargo = input("Ingrese el cargo del empleado: ").strip()

    while True:
        # Buscar medicamento
        medicamento_encontrado = obtener_medicamento(medicamentos)
        if not medicamento_encontrado:
            print("❌ Venta cancelada por el usuario.")
            return

        stock_disponible = medicamento_encontrado.get("stock", 0)

        # Obtener cantidad válida
        cantidad_medicamento = obtener_cantidad(stock_disponible)

        precio_unitario = medicamento_encontrado["precio"]
        total = round(cantidad_medicamento * precio_unitario, 2)

        # Mostrar resumen de la venta hasta el momento
        print("\nResumen de la venta:")
        print(f"Paciente: {nombre_paciente}")
        print(f"Dirección: {direccion_paciente}")
        print(f"Teléfono: {telefono_paciente}")
        print(f"Empleado: {nombre_empleado} ({cargo})")
        print(f"Medicamento: {medicamento_encontrado['nombre']}")
        print(f"Cantidad: {cantidad_medicamento}")
        print(f"Precio unitario: ${precio_unitario}")
        print(f"Total: ${total}")

        confirmar = input("\n¿Desea confirmar la venta? (s/n): ").strip().lower()
        if confirmar != 's':
            print("❌ Venta cancelada. No se realizaron cambios.")
            return

        # Registrar paciente solo después de confirmar la venta
        registrar_paciente(nombre_paciente, direccion_paciente, telefono_paciente)

        # Registrar venta
        fecha_venta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        registro_venta = {
            "fechaVenta": fecha_venta,
            "paciente": {
                "nombre": nombre_paciente,
                "direccion": direccion_paciente
            },
            "empleado": {
                "nombre": nombre_empleado,
                "cargo": cargo
            },
            "medicamentosVendidos": {
                "nombreMedicamento": medicamento_encontrado["nombre"],
                "cantidadVendida": cantidad_medicamento,
                "precioUnitario": precio_unitario,
                "total": total
            }
        }

        # Actualizar el stock del medicamento vendido
        for medicamento in medicamentos:
            if medicamento["nombre"] == medicamento_encontrado["nombre"]:
                medicamento["stock"] -= cantidad_medicamento
                break

        guardar_json(PATH_MEDICAMENTOS, medicamentos)

        # Guardar la venta
        ventas.append(registro_venta)
        guardar_json(PATH_VENTAS, ventas)

        print("✅ Venta registrada correctamente y stock actualizado.")

        # Preguntar si desea continuar comprando otro medicamento
        continuar = input("\n¿Desea vender otro medicamento? (s/n): ").strip().lower()
        if continuar != 's':
            break
