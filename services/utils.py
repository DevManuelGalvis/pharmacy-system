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
