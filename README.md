
# Biblioteca - Sistema de Gestión de Préstamos

## Descripción

Este proyecto es una aplicación para gestionar una biblioteca. Permite registrar y dar de baja socios, añadir y eliminar libros, y gestionar los préstamos de libros. Está construido en Python utilizando SQLAlchemy para la base de datos y un modelo de objetos para representar las entidades de la biblioteca como Socios, Libros y Préstamos.

## Requisitos

- Python 3.7 o superior
- **pytest**: para realizar pruebas unitarias
- **setuptools**: para la distribución del proyecto
- **SQLAlchemy**: para la gestión de la base de datos

Instala las dependencias utilizando el siguiente comando:

```bash
pip install -r requirements.txt
```

**requirements.txt**

```
pytest>=8.3.4
setuptools>=44.1.1
SQLAlchemy>=1.4.0
```

## Estructura del Proyecto

```
biblioteca/
│
├── Biblioteca/
│   ├── __init__.py
│   ├── libro.py
│   ├── socio.py
│   └── prestamo.py
│
│── Test/
│   │── __init__.py
│   └── test_biblioteca.py
│
├── database.py
├── main.py
└── requirements.txt
```

### Archivos principales

- `Biblioteca/libro.py`: Define la clase `Libro` que representa un libro en la biblioteca.
- `Biblioteca/socio.py`: Define la clase `Socio` que representa a un socio de la biblioteca.
- `Biblioteca/prestamo.py`: Define la clase `Prestamo` que registra los préstamos de los libros.
- `database.py`: Configura la conexión a la base de datos usando SQLAlchemy.
- `main.py`: Contiene la clase `biblioteca` que maneja la lógica de alta, baja, préstamo y devolución de libros y socios. También incluye la clase `menu` que implementa la interfaz de usuario.

## Uso

### Interfaz de Línea de Comandos (CLI)

1. **Alta de Socio**
2. **Baja de Socio**
3. **Alta de Libro**
4. **Baja de Libro**
5. **Préstamo de Libro**
6. **Devolución de Libro**
7. **Consultar Libros**
8. **Consultar Usuarios**
9. **Consultar Préstamos**
10. **Salir**

### Ejemplo de Uso:

1. Inicia la aplicación desde la línea de comandos:

```bash
python main.py
```

2. Aparecerá un menú con las opciones disponibles. Puedes ingresar el número correspondiente a la acción que deseas realizar.

## Base de Datos

La base de datos se gestiona utilizando **SQLAlchemy** y se almacena en un archivo SQLite llamado `bibloteca.db`.

### Configuración de la base de datos:

- La base de datos está configurada con SQLite, pero puedes cambiar la URL de la base de datos en el archivo `database.py` si prefieres usar otro sistema de gestión de bases de datos (como PostgreSQL o MySQL).
  
  ```python
  DATABASE_URL = "sqlite:///./bibloteca.db"
  ```

## Clases

### Clase `biblioteca`

La clase principal que contiene las funcionalidades para:

- **Alta y baja de socios y libros.**
- **Prestamos y devoluciones de libros.**
- **Consultar información sobre socios, libros y préstamos.**

### Clase `menu`

Gestiona la interfaz de línea de comandos, interactuando con el usuario y solicitando entradas para las acciones disponibles.

### Clases de Modelo (`Libro`, `Socio`, `Prestamo`)

- **Libro**: Representa un libro en la biblioteca.
- **Socio**: Representa un socio de la biblioteca.
- **Prestamo**: Representa un préstamo de un libro a un socio.

## Pruebas

Para realizar pruebas unitarias de la aplicación, puedes utilizar `pytest`.

Ejecuta las pruebas con el siguiente comando:

```bash
pytest
```

## Contribuciones

Si deseas contribuir a este proyecto, por favor crea un *fork* y envía un *pull request*.

1. Haz un *fork* del repositorio.
2. Crea una rama con tu cambio (`git checkout -b mi-cambio`).
3. Realiza el commit de tus cambios (`git commit -am 'Añadí una nueva característica'`).
4. Sube tus cambios a tu repositorio (`git push origin mi-cambio`).
5. Crea un *pull request*.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

Este es un proyecto simple para gestionar una biblioteca, pero puedes extenderlo para agregar funcionalidades adicionales como reservas, historial de préstamos, o más detalles sobre los libros.
