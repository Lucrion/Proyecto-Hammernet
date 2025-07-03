from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import json

# Configuración para usar MySQL si está disponible, o JSON como fallback
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/ferreteria"

# Intentar crear el motor de base de datos
try:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
    print("Conexión a MySQL establecida correctamente")
    USE_DB = True
except Exception as e:
    print(f"Error al conectar a MySQL: {e}")
    print("Usando almacenamiento JSON como fallback")
    USE_DB = False

# Función para obtener una sesión de base de datos
def get_db():
    if USE_DB:
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
    else:
        yield None

# Funciones para trabajar con JSON como fallback
def get_json_data(file_name):
    """Obtiene datos desde un archivo JSON"""
    file_path = os.path.join("data", file_name)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_json_data(file_name, data):
    """Guarda datos en un archivo JSON"""
    os.makedirs("data", exist_ok=True)
    file_path = os.path.join("data", file_name)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)