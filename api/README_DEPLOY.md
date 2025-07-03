# Despliegue en Render

Este documento contiene las instrucciones para desplegar la API de Hammernet en Render.

## Requisitos previos

1. Cuenta en [Render](https://render.com/)
2. Cuenta en [Cloudinary](https://cloudinary.com/) (para almacenamiento de imágenes)
3. Base de datos PostgreSQL (puedes usar el servicio de Render)

## Pasos para el despliegue

### 1. Crear una base de datos PostgreSQL en Render

1. Inicia sesión en tu cuenta de Render
2. Ve a la sección "PostgreSQL" y haz clic en "New PostgreSQL"
3. Configura tu base de datos:
   - Nombre: `hammernet-db` (o el nombre que prefieras)
   - Usuario: Render generará uno automáticamente
   - Contraseña: Render generará una automáticamente
   - Región: Selecciona la más cercana a tus usuarios
4. Haz clic en "Create Database"
5. Una vez creada, guarda la URL de conexión (Internal Database URL) para usarla más adelante

### 2. Desplegar la API en Render

1. Ve a la sección "Web Services" y haz clic en "New Web Service"
2. Conecta tu repositorio de GitHub o sube el código directamente
3. Configura el servicio:
   - Nombre: `hammernet-api` (o el nombre que prefieras)
   - Runtime: Python
   - Build Command: `pip install -r api/requirements.txt`
   - Start Command: `cd api && uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Región: Selecciona la misma que usaste para la base de datos

4. En la sección "Environment Variables", agrega las siguientes variables:
   - `DATABASE_URL`: La URL de conexión de tu base de datos PostgreSQL
   - `JWT_SECRET_KEY`: Una clave secreta para firmar los tokens JWT
   - `ACCESS_TOKEN_EXPIRE_MINUTES`: Tiempo de expiración de los tokens (por ejemplo, 30)
   - `CLOUDINARY_CLOUD_NAME`: Tu cloud name de Cloudinary
   - `CLOUDINARY_API_KEY`: Tu API key de Cloudinary
   - `CLOUDINARY_API_SECRET`: Tu API secret de Cloudinary

5. Haz clic en "Create Web Service"

### 3. Verificar el despliegue

1. Una vez que el servicio esté desplegado, Render te proporcionará una URL para acceder a tu API
2. Accede a `https://tu-servicio.onrender.com/docs` para ver la documentación de la API y probar los endpoints

## Notas adicionales

- La API está configurada para usar PostgreSQL en producción, pero si hay algún problema con la conexión, usará archivos JSON como fallback
- Asegúrate de que las variables de entorno estén correctamente configuradas
- Si necesitas hacer cambios en la configuración, puedes hacerlo desde el panel de control de Render