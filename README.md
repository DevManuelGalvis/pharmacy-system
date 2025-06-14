# Sistema de Gestión de Farmacia

Este proyecto es un **Sistema de Gestión de Farmacia** desarrollado en Python. Actualmente, la aplicación funciona en modo consola y permite registrar ventas y compras de medicamentos, así como la gestión básica de usuarios, pacientes y proveedores.

## Estado del Proyecto

- [x] **Módulo de Ventas**
- [x] **Módulo de Compras**
- [ ] **Módulo de Reportes** (en desarrollo)

**Avance actual:** 2 de 3 módulos principales implementados (~66%).

## Características

- Registro de ventas de medicamentos.
- Registro de compras y actualización de inventario.
- Gestión de usuarios con roles (administrador, gerente, empleado).
- Registro automático de pacientes y proveedores.
- Persistencia de datos en archivos JSON.

## Uso

1. Clona este repositorio.
2. Ejecuta el archivo principal desde la terminal:

   ```sh
   python main.py
   ```

3. Inicia sesión con uno de los usuarios definidos en `data/Usuarios.json`.
4. Sigue las instrucciones del menú para registrar ventas o compras.

## Próximamente

- Implementación del módulo de reportes.
- Migración a una **aplicación web** para una mejor experiencia de usuario.

## Requisitos

- Python 3.10 o superior

## Estructura del Proyecto

- `main.py`: Archivo principal de la aplicación.
- `models/`: Lógica de negocio para ventas, compras y pacientes.
- `services/`: Utilidades y autenticación.
- `data/`: Archivos JSON con la información persistente.

---

**Nota:** Este proyecto está en desarrollo y actualmente solo funciona por consola. ¡Próximamente estará disponible