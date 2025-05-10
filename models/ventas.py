import os
import json
from datetime import date, time, datetime
from services.utils import cargar_json, guardar_json
# from services import utils

def ventas():
    PATH_MEDICAMENTOS = "data/Medicamentos.json"
    PATH_VENTAS = "data/Ventas.json"

    medicamentos = cargar_json(PATH_MEDICAMENTOS)
    ventas = cargar_json(PATH_VENTAS)
    print(medicamentos)
    if not medicamentos:
        print("⚠️ No hay medicamentos registrados en el inventario.")
        return

    # Datos del paciente y empleado
    nombre_paciente = input("Ingrese el nombre del paciente: ").strip()
    direccion_paciente = input("Ingrese la dirección del paciente: ").strip()
    nombre_empleado = input("Ingrese el nombre del empleado: ").strip()
    cargo = input("Ingrese el cargo del empleado: ").strip()

    # Buscar medicamento
    nombre_medicamento = input("Ingrese el nombre del medicamento: ").strip().title()
    medicamento_encontrado = next((m for m in medicamentos if m["nombre"] == nombre_medicamento), None)

    if not medicamento_encontrado:
        print(f"❌ El medicamento '{nombre_medicamento}' no está en el inventario.")
        return

    # Validar cantidad
    try:
        cantidad_medicamento = int(input("Ingrese la cantidad del medicamento: "))
        if cantidad_medicamento <= 0:
            print("❌ La cantidad debe ser mayor a cero.")
            return
    except ValueError:
        print("❌ Ingrese un número válido para la cantidad.")
        return

    stock_disponible = medicamento_encontrado.get("stock", 0)

    if cantidad_medicamento > stock_disponible:
        print(f"❌ Solo hay {stock_disponible} unidades disponibles de '{nombre_medicamento}'.")
        return

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
            "nombreMedicamento": nombre_medicamento,
            "cantidadVendida": cantidad_medicamento,
            "precioUnitario": medicamento_encontrado["precio"],
            # "total": round(cantidad_medicamento * medicamento_encontrado["precio"], 2)
        }
    }

    # Actualizar inventario
    medicamento_encontrado["stock"] -= cantidad_medicamento
    guardar_json(PATH_MEDICAMENTOS, medicamentos)

    # Agregar la venta al archivo
    ventas.append(registro_venta)
    guardar_json(PATH_VENTAS, ventas)

    print("✅ Venta registrada correctamente y stock actualizado.")
def registrar_ventas(registro_ventas):
    with open("ventas.json", "w") as f:
        json.dump(registro_ventas, f, indent=4)


def mostrar_pacientes():
    if os.path.exists("Pacientes.json"):
        with open("Pacientes.json", "r") as f:
            return json.load(f)
    return {}

def mostrar_medicamentos():
    if os.path.exists("Medicamentos.json"):
        with open("Medicamentos.json", "r") as f:
            return json.load(f)
    return {}

