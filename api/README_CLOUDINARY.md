# Integración con Cloudinary en Hammernet

Este documento explica cómo se ha implementado la integración con Cloudinary para el manejo de imágenes en la aplicación Hammernet.

## Configuración

La configuración de Cloudinary se encuentra en el archivo `cloudinary_config.py`. Este archivo contiene:

- Función `configure_cloudinary()`: Configura las credenciales de Cloudinary.
- Función `upload_image()`: Sube una imagen a Cloudinary y devuelve la URL.
- Función `delete_image()`: Elimina una imagen de Cloudinary por su public_id.
- Función `get_public_id_from_url()`: Extrae el public_id de una URL de Cloudinary.

## Endpoints de la API

La API proporciona dos endpoints para subir imágenes a Cloudinary:

1. `/upload-image`: Recibe un archivo de imagen y lo sube a Cloudinary.
2. `/upload-image-base64`: Recibe una imagen en formato base64 y la sube a Cloudinary.

## Scripts de utilidad

Se han creado varios scripts para facilitar el trabajo con Cloudinary:

1. `test_cloudinary.py`: Prueba la configuración de Cloudinary y la subida de imágenes.
2. `update_product_images.py`: Actualiza las imágenes de los productos existentes con URLs de Cloudinary.
3. `add_test_product.py`: Añade un producto de prueba con una imagen subida a Cloudinary.

## Uso en el frontend

Las imágenes de Cloudinary se utilizan en el frontend de la siguiente manera:

1. Las URLs de las imágenes se almacenan en la base de datos o en los archivos JSON.
2. El frontend carga estas URLs directamente desde Cloudinary.

## Dependencias

Para utilizar Cloudinary, se requieren las siguientes dependencias:

```
cloudinary>=1.33.0,<2.0.0
requests>=2.32.0,<3.0.0
```

Estas dependencias están incluidas en el archivo `requirements.txt`.

## Migración de imágenes locales a Cloudinary

Para migrar las imágenes locales a Cloudinary, se puede utilizar el script `update_product_images.py`. Este script:

1. Lee los productos desde el archivo JSON.
2. Para cada producto con una imagen local, sube la imagen a Cloudinary.
3. Actualiza la URL de la imagen en el archivo JSON.

## Pruebas

Para probar la integración con Cloudinary, se puede utilizar el script `test_cloudinary.py`. Este script:

1. Prueba la configuración de Cloudinary.
2. Crea una imagen de prueba y la sube a Cloudinary.

## Ventajas de usar Cloudinary

- Optimización automática de imágenes.
- Redimensionamiento y transformación de imágenes bajo demanda.
- CDN global para entrega rápida de imágenes.
- Respaldo y seguridad de las imágenes.

## Consideraciones de seguridad

- Las credenciales de Cloudinary deben mantenerse seguras y no deben incluirse en el código fuente público.
- Se recomienda utilizar variables de entorno para las credenciales en un entorno de producción.