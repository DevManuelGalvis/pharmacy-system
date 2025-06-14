# services/auth.py
import json
import os
from getpass import getpass

RUTA_USUARIOS = "data/Usuarios.json"

def cargar_usuarios():
    if not os.path.exists(RUTA_USUARIOS):
        return []
    with open(RUTA_USUARIOS, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

def iniciar_sesion():
    usuarios = cargar_usuarios()
    print("\n🔐 Iniciar sesión")

    intentos = 3
    while intentos > 0:
        usuario = input("👤 Usuario: ").strip()
        contraseña = getpass("🔑 contrasena: ").strip()  # ← OCULTA al escribir

        for u in usuarios:
            if u["usuario"] == usuario and u["contrasena"] == contraseña:
                print(f"✅ Bienvenido {usuario} (Rol: {u['rol']})")
                return u["rol"]

        intentos -= 1
        print(f"❌ Credenciales incorrectas. Intentos restantes: {intentos}")

    print("🚫 Se agotaron los intentos.")
    return None
