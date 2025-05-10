from datetime import datetime
import json


def formatear_fecha(fecha_str):
    return datetime.strptime(fecha_str, '%Y-%m-%d')


def cargar_json(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Archivo no encontrado: {ruta}")
        return []
    except json.JSONDecodeError as e:
        print(f"Error decodificando JSON: {e}")
        return []
    except Exception as e:
        print(f"Otro error leyendo {ruta}: {e}")
        return []


def guardar_json(ruta, datos):
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

# def obtener_medicamento(medicamentos):
#     while True:
#         nombre = input("Ingrese el nombre del medicamento (o 'cancelar' para salir): ").strip().title()
#         if nombre.lower() == "cancelar":
#             return None
#         medicamento = next((m for m in medicamentos if m["nombre"] == nombre), None)
#         if medicamento:
#             return medicamento
#         print(f"❌ El medicamento '{nombre}' no está en el inventario. Intente de nuevo.")
def obtener_medicamento(medicamentos, nombre_proveedor=None, contacto_proveedor=None):
    while True:
        nombre = input("Ingrese el nombre del medicamento (o 'cancelar' para salir): ").strip().title()
        if nombre.lower() == "cancelar":
            return None
        medicamento = next((m for m in medicamentos if m["nombre"] == nombre), None)
        
        if medicamento:
            # Si ya existe el medicamento, no necesitamos pedir proveedor y contacto
            return medicamento
        else:
            print(f"❌ El medicamento '{nombre}' no está en el inventario.")
            if nombre_proveedor and contacto_proveedor:
                # Si ya tenemos el proveedor y contacto, los usamos directamente
                respuesta = input(f"¿Desea agregar el medicamento '{nombre}' al inventario? (s/n): ").strip().lower()
                if respuesta == 's':
                    cantidad_comprada = int(input(f"Ingrese la cantidad de '{nombre}' a comprar: "))
                    precio_compra = float(input(f"Ingrese el precio de compra de '{nombre}': "))
                    fecha_expiracion = input(f"Ingrese la fecha de expiración de '{nombre}' (YYYY-MM-DD): ").strip()

                    nuevo_medicamento = {
                        "nombre": nombre,
                        "precio": precio_compra,
                        "stock": cantidad_comprada,
                        "fechaExpiracion": fecha_expiracion,
                        "proveedor": {
                            "nombre": nombre_proveedor,
                            "contacto": contacto_proveedor
                        }
                    }
                    medicamentos.append(nuevo_medicamento)
                    print(f"✅ Medicamento '{nombre}' agregado al inventario con {cantidad_comprada} unidades.")
                    return medicamento
            else:
                # Si no tenemos proveedor ni contacto, se pregunta al usuario
                respuesta = input(f"¿Desea agregar el medicamento '{nombre}' al inventario? (s/n): ").strip().lower()
                if respuesta == 's':
                    cantidad_comprada = int(input(f"Ingrese la cantidad de '{nombre}' a comprar: "))
                    precio_compra = float(input(f"Ingrese el precio de compra de '{nombre}': "))
                    fecha_expiracion = input(f"Ingrese la fecha de expiración de '{nombre}' (YYYY-MM-DD): ").strip()

                    # Pedir proveedor y contacto
                    nombre_proveedor = input("Ingrese el nombre del proveedor: ").strip()
                    contacto_proveedor = input("Ingrese el contacto del proveedor: ").strip()

                    nuevo_medicamento = {
                        "nombre": nombre,
                        "precio": precio_compra,
                        "stock": cantidad_comprada,
                        "fechaExpiracion": fecha_expiracion,
                        "proveedor": {
                            "nombre": nombre_proveedor,
                            "contacto": contacto_proveedor
                        }
                    }
                    medicamentos.append(nuevo_medicamento)
                    print(f"✅ Medicamento '{nombre}' agregado al inventario con {cantidad_comprada} unidades.")
                    return medicamento

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

