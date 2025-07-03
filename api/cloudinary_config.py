import cloudinary
import cloudinary.uploader
import cloudinary.api

# Configuración de Cloudinary
def configure_cloudinary():
    cloudinary.config(
        cloud_name="dnmzhpriq",  # Reemplazar con tu cloud_name
        api_key="134672837851277",        # Reemplazar con tu api_key
        api_secret="tpvjdMcBLOXWHf3bTeM5z4PMfMI",
        secure=True# Reemplazar con tu api_secret
    )

# Función para subir una imagen a Cloudinary
def upload_image(image_data, public_id=None):
    """Sube una imagen a Cloudinary y devuelve la URL"""
    try:
        # Configurar opciones de carga
        upload_options = {
            "folder": "hammernet",  # Carpeta donde se guardarán las imágenes
        }
        
        # Si se proporciona un public_id, usarlo
        if public_id:
            upload_options["public_id"] = public_id
        
        # Subir la imagen
        result = cloudinary.uploader.upload(image_data, **upload_options)
        
        # Devolver la URL segura de la imagen
        return result["secure_url"]
    except Exception as e:
        print(f"Error al subir imagen a Cloudinary: {e}")
        return None

# Función para eliminar una imagen de Cloudinary
def delete_image(public_id):
    """Elimina una imagen de Cloudinary por su public_id"""
    try:
        result = cloudinary.uploader.destroy(public_id)
        return result["result"] == "ok"
    except Exception as e:
        print(f"Error al eliminar imagen de Cloudinary: {e}")
        return False

# Extraer el public_id de una URL de Cloudinary
def get_public_id_from_url(url):
    """Extrae el public_id de una URL de Cloudinary"""
    if not url or "cloudinary.com" not in url:
        return None
    
    # La URL tiene el formato: https://res.cloudinary.com/cloud_name/image/upload/v1234567890/folder/public_id.ext
    try:
        # Dividir por '/upload/'
        parts = url.split("/upload/")
        if len(parts) < 2:
            return None
        
        # Obtener la parte después de /upload/vXXXXXXXXXX/
        path = parts[1]
        if "/" in path:
            # Eliminar la versión si existe
            if path.startswith("v") and "/" in path:
                path = path.split("/", 1)[1]
            
            # Eliminar la extensión
            public_id = path.rsplit(".", 1)[0]
            return public_id
    except Exception as e:
        print(f"Error al extraer public_id: {e}")
    
    return None