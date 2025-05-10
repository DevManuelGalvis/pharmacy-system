# pacientes.py
from services.utils import cargar_json, guardar_json

def registrar_paciente(nombre, direccion, telefono):
    PATH_PACIENTES = "data/Pacientes.json"
    pacientes = cargar_json(PATH_PACIENTES)
    
    for paciente in pacientes:
        if paciente['nombre'] == nombre and paciente['direccion'] == direccion and paciente['telefono'] == telefono:
            print("✅ El paciente ya está registrado.")
            return

    nuevo_paciente = {
        "nombre": nombre,
        "direccion": direccion,
        "telefono": telefono
    }
    pacientes.append(nuevo_paciente)
    guardar_json(PATH_PACIENTES, pacientes)
    print(f"✅ Paciente {nombre} registrado correctamente.")
