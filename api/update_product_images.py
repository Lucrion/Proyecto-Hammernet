import os
import json
import sys
from cloudinary_config import configure_cloudinary, upload_image

# Configurar Cloudinary
configure_cloudinary()

def update_product_images():
    """Actualiza las imágenes de productos con URLs de Cloudinary"""
    try:
        # Obtener los productos actuales
        json_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "productos.json")
        
        if not os.path.exists(json_file_path):
            print(f"Archivo de productos no encontrado en: {json_file_path}")
            return False
            
        with open(json_file_path, "r", encoding="utf-8") as f:
            productos = json.load(f)
            
        if not productos:
            print("No se encontraron productos para actualizar")
            return False
        
        print(f"Se encontraron {len(productos)} productos")
        
        # Directorio de imágenes locales
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        public_dir = os.path.join(base_dir, "public")
        
        # Contador de actualizaciones
        actualizados = 0
        
        # Procesar cada producto
        for producto in productos:
            # Verificar si la imagen es local (no de Cloudinary)
            imagen_actual = producto.get("imagen", "")
            
            if not imagen_actual:
                print(f"Producto {producto['id']} - {producto['nombre']} no tiene imagen")
                continue
                
            if "cloudinary.com" in imagen_actual:
                print(f"Producto {producto['id']} - {producto['nombre']} ya tiene imagen en Cloudinary: {imagen_actual}")
                continue
            
            # Ruta local de la imagen
            if imagen_actual.startswith("/"):
                imagen_actual = imagen_actual[1:]  # Quitar la barra inicial
            
            imagen_path = os.path.join(public_dir, imagen_actual)
            
            if not os.path.exists(imagen_path):
                print(f"⚠️ Imagen no encontrada: {imagen_path} para producto {producto['id']} - {producto['nombre']}")
                continue
            
            print(f"Procesando producto {producto['id']} - {producto['nombre']} con imagen {imagen_path}")
            
            # Subir la imagen a Cloudinary
            try:
                with open(imagen_path, "rb") as img_file:
                    image_data = img_file.read()
                    
                    # Generar un public_id basado en el nombre del producto
                    public_id = f"producto_{producto['id']}_{os.path.basename(imagen_actual).split('.')[0]}"
                    
                    # Subir la imagen
                    cloudinary_url = upload_image(image_data, public_id=public_id)
                    
                    if cloudinary_url:
                        # Actualizar la URL en el producto
                        producto["imagen"] = cloudinary_url
                        actualizados += 1
                        print(f"✅ Imagen actualizada para producto {producto['id']} - {producto['nombre']}")
                        print(f"   URL anterior: {imagen_actual}")
                        print(f"   Nueva URL: {cloudinary_url}")
                    else:
                        print(f"❌ Error al subir imagen para producto {producto['id']} - {producto['nombre']}")
            except Exception as e:
                print(f"❌ Error procesando imagen {imagen_path}: {str(e)}")
        
        # Guardar los cambios si se actualizó algún producto
        if actualizados > 0:
            with open(json_file_path, "w", encoding="utf-8") as f:
                json.dump(productos, f, ensure_ascii=False, indent=4)
            print(f"\n✅ Se actualizaron {actualizados} productos con imágenes de Cloudinary")
            return True
        else:
            print("\nℹ️ No se realizaron actualizaciones")
            return False
            
    except Exception as e:
        print(f"Error al actualizar imágenes: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("=== Actualización de imágenes de productos a Cloudinary ===")
    resultado = update_product_images()
    
    if resultado:
        print("\n✅ Proceso completado exitosamente")
        sys.exit(0)
    else:
        print("\n⚠️ El proceso finalizó sin actualizaciones")
        sys.exit(1)