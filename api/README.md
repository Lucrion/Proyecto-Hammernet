# API de Hammernet

Esta es la API para el panel de administración de Hammernet, desarrollada con FastAPI, con soporte para base de datos MySQL y almacenamiento JSON como fallback.

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- MySQL (opcional, si se desea usar base de datos en lugar de JSON)

## Instalación

1. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Configuración de la base de datos

Por defecto, la API intentará conectarse a una base de datos MySQL en `localhost:3306` con el usuario `root` sin contraseña y la base de datos `ferreteria`. Si la conexión falla, se utilizará automáticamente el almacenamiento JSON como fallback.

Para modificar la configuración de la base de datos, edita la variable `DATABASE_URL` en el archivo `database.py`.

## Ejecución

Para iniciar el servidor de desarrollo:

```bash
python main.py
```

O alternativamente:

```bash
uvicorn main:app --reload
```

El servidor estará disponible en http://localhost:8000

## Documentación de la API

Una vez que el servidor esté en ejecución, puedes acceder a la documentación interactiva en:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Endpoints disponibles

### Productos

- `GET /productos` - Obtener todos los productos
- `GET /productos/{id}` - Obtener un producto por ID
- `POST /productos` - Crear un nuevo producto
- `PUT /productos/{id}` - Actualizar un producto existente
- `DELETE /productos/{id}` - Eliminar un producto

### Usuarios

- `GET /usuarios` - Obtener todos los usuarios
- `POST /usuarios` - Crear un nuevo usuario

### Autenticación

- `POST /login` - Iniciar sesión (devuelve un token JWT)

## Seguridad

- Autenticación mediante tokens JWT
- Contraseñas hasheadas con bcrypt
- Soporte para roles de usuario (admin, editor, viewer)
- Fallback a almacenamiento local si la base de datos no está disponible

Para acceder a los endpoints protegidos, debes incluir el token JWT en el encabezado de la solicitud:

```
Authorization: Bearer <token>
```