# RopaUrbana

**RopaUrbana** es una aplicación de escritorio desarrollada en Python para la gestión de ventas y el manejo de inventario de productos de ropa. Utiliza `customtkinter` para proporcionar una interfaz gráfica moderna y `Pillow` para la manipulación de imágenes. La aplicación permite realizar ventas, agregar productos, y consultar el inventario y las ventas realizadas.

## Características

- **Interfaz Principal:** Pantalla de inicio con el título de la aplicación, imágenes de productos y botones de navegación.
- **Venta de Productos:** Ventana para registrar ventas, incluyendo campos para el producto, cantidad, precio y total.
- **Gestión de Inventario:** Sección destinada a la visualización y gestión del inventario (en desarrollo).
- **Agregar Productos:** Ventana para añadir nuevos productos al sistema (en desarrollo).
- **Historial de Ventas:** Visualización de ventas realizadas (en desarrollo).
- **Salir:** Opción para cerrar la aplicación.

## Requisitos

Para ejecutar la aplicación, debes tener instaladas las siguientes dependencias:

- **Python 3.6 o superior**
- **`customtkinter`:** Extensión moderna de `tkinter` para interfaces gráficas.
- **`Pillow`:** Librería para el manejo de imágenes.
- **`mysql-connector-python`:** Librería para la conexión de la base de datos.

Instala las dependencias necesarias utilizando pip:

```bash
pip install customtkinter
pip install mysql-connector-python
pip install pillow
```

## Instalación y Ejecución

1. **Clona el Repositorio:** Descarga el proyecto desde GitHub o clónalo usando git:

   ```bash
   git clone https://github.com/tu_usuario/ropaurbana.git
   ```

2. **Prepara las Imágenes:** Asegúrate de tener las siguientes imágenes en el mismo directorio que el archivo principal del proyecto:
   - `ves_verde.jpg`
   - `ves_negro.jpg`
   - `con_blan.jpg`
   - `car.jpg`

3. **Ejecuta el Proyecto:** Corre el archivo Python principal para iniciar la aplicación:

   ```bash
   python3 gestor_de_ventas.py
   ```

## Estructura del Código

El código está dividido en varias secciones clave:

- **Configuración Inicial:** 
  - Configuración del modo de apariencia y el tema de color de `customtkinter`.
  
- **Ventana Principal (`ventana_ini`):** 
  - **Título:** Marco con el título de la aplicación.
  - **Imágenes de Productos:** Muestra imágenes de productos en la interfaz principal.
  - **Botones de Navegación:** Botones para acceder a las funcionalidades de "Vender", "Inventario", "Agregar Producto", y "Ventas".
  - **Información del Autor:** Información sobre los autores de la aplicación.

- **Funcionalidades de los Botones:**
  - **Botón Vender:** Abre una ventana para registrar una venta de producto.
  - **Botón Inventario:** Abre una ventana para gestionar el inventario (en desarrollo).
  - **Botón Agregar Producto:** Abre una ventana para añadir nuevos productos (en desarrollo).
  - **Botón Ventas:** Abre una ventana para mostrar el historial de ventas (en desarrollo).
  - **Botón Salir:** Cierra la aplicación.

## Detalles de Implementación

- **Ventana de Venta (`boton_vender`):** Permite ingresar detalles de ventas y tiene opciones para añadir imágenes y botones de acción.
- **Ventana de Inventario (`boton_inventario`):** Espacio para la gestión del inventario, aún por desarrollar.
- **Ventana de Agregar Producto (`boton_agregar_prod`):** Espacio para añadir productos, aún por desarrollar.
- **Ventana de Ventas (`boton_ventas`):** Visualización de ventas, aún por desarrollar.

## Autores

- **Gabriel Tellez:** Desarrollador principal, encargado de la implementación y diseño de la interfaz.
- **Javier Murcia:** Co-desarrollador, colaborador en el diseño de la arquitectura y la funcionalidad del sistema.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir al proyecto:

1. Realiza un fork del repositorio.
2. Crea una rama para tus cambios (`git checkout -b mi-rama`).
3. Realiza los cambios y haz commit (`git commit -am 'Añadir una nueva funcionalidad'`).
4. Envía un pull request.

## Licencia

Este proyecto está licenciado bajo los términos de la [MIT License](https://opensource.org/licenses/MIT).

---

Para cualquier pregunta o soporte adicional, por favor contacta a los autores o abre un issue en el repositorio.

```

Este `README.md` proporciona una descripción completa del proyecto, detalla la estructura del código y las funcionalidades, e incluye información sobre los autores y cómo contribuir. Asegúrate de personalizar los enlaces y los nombres de archivo según sea necesario.

````
# Diagrama

![Clase UML(1)](https://github.com/user-attachments/assets/76172072-9a42-4c52-9211-b8c44ab9f883)


