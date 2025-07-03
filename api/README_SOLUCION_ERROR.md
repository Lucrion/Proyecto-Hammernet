# Solución al Error "Could not import module 'main'"

Este documento explica cómo se ha resuelto el error "Could not import module 'main'" que ocurría al intentar iniciar el servidor API de Hammernet.

## Problema

El error "Could not import module 'main'" ocurre cuando el servidor ASGI (como Uvicorn) no puede importar correctamente el módulo principal de la aplicación. Esto puede deberse a varias razones:

1. El directorio no está reconocido como un paquete Python
2. La forma en que se está ejecutando la aplicación no es correcta
3. Problemas con la estructura del proyecto

## Solución Implementada

Se han realizado los siguientes cambios para resolver el problema:

1. **Creación de archivo `__init__.py`**: Se ha añadido un archivo `__init__.py` vacío en el directorio principal para que Python lo reconozca como un paquete.

2. **Creación de punto de entrada alternativo**: Se ha creado un archivo `run.py` que sirve como punto de entrada alternativo para ejecutar la aplicación. Este archivo utiliza la sintaxis correcta para iniciar Uvicorn:

   ```python
   # run.py
   if __name__ == "__main__":
       import uvicorn
       uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
   ```

3. **Actualización del script de inicio**: Se ha actualizado el archivo `start_server.bat` para usar el nuevo punto de entrada:

   ```batch
   cd %~dp0
   python run.py
   ```

4. **Archivos adicionales para compatibilidad**: Se han creado archivos `wsgi.py` y `asgi.py` para mejorar la compatibilidad con diferentes servidores web.

## Cómo Iniciar el Servidor

Para iniciar el servidor API, simplemente ejecute el archivo `start_server.bat`. Esto iniciará el servidor en `http://localhost:8000`.

Alternativamente, puede ejecutar directamente:

```
python run.py
```

## Verificación

Para verificar que el servidor está funcionando correctamente, abra un navegador y vaya a `http://localhost:8000/docs`. Debería ver la documentación interactiva de la API de Hammernet.