import cloudinary
import cloudinary.uploader
import os
from cloudinary_config import configure_cloudinary, upload_image

def test_cloudinary_config():
    """Prueba la configuración de Cloudinary"""
    # Configurar Cloudinary
    configure_cloudinary()
    
    # Verificar que la configuración se haya aplicado correctamente
    config = cloudinary.config()
    print("Configuración de Cloudinary:")
    print(f"  Cloud name: {config.cloud_name}")
    print(f"  API Key: {config.api_key}")
    print(f"  API Secret: {'*' * 10}")
    print(f"  Secure: {config.secure}")
    
    return config.cloud_name and config.api_key and config.api_secret

def test_upload_image():
    """Prueba la subida de una imagen a Cloudinary"""
    # Configurar Cloudinary
    configure_cloudinary()
    
    # Crear una imagen de prueba simple (un pixel rojo en formato PNG)
    test_image_path = "test_image.png"
    with open(test_image_path, "wb") as f:
        # Encabezado PNG mínimo + un pixel rojo
        f.write(bytes.fromhex(
            '89504e470d0a1a0a0000000d49484452000000010000000108060000001f15c4890000000d4944415478da636460200000000500010d0a2db40000000049454e44ae426082'
        ))
    
    try:
        # Subir la imagen
        print("\nProbando subida de imagen...")
        with open(test_image_path, "rb") as f:
            image_data = f.read()
            url = upload_image(image_data, public_id="test_pixel")
            
        if url:
            print(f"Imagen subida exitosamente: {url}")
            return True
        else:
            print("Error: No se pudo subir la imagen")
            return False
    finally:
        # Limpiar: eliminar la imagen de prueba
        if os.path.exists(test_image_path):
            os.remove(test_image_path)

if __name__ == "__main__":
    print("=== Prueba de configuración de Cloudinary ===")
    config_ok = test_cloudinary_config()
    
    if config_ok:
        print("\n✅ Configuración de Cloudinary correcta")
        
        # Probar subida de imagen
        upload_ok = test_upload_image()
        if upload_ok:
            print("\n✅ Subida de imagen exitosa")
            print("\n✅ TODO CORRECTO: La configuración de Cloudinary funciona correctamente")
        else:
            print("\n❌ Error en la subida de imagen")
    else:
        print("\n❌ Error en la configuración de Cloudinary")