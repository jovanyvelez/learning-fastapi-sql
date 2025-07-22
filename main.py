"""
🚀 Heroes API - FastAPI Application Entry Point 🚀

📚 PROPÓSITO EDUCATIVO:
Este es el punto de entrada de la aplicación FastAPI. Aquí se configura
la aplicación principal y se registran todas las rutas (routers).

🎯 CONCEPTOS QUE APRENDERÁS:
- ✅ Creación de aplicación FastAPI
- ✅ Metadatos de API (título, descripción, versión)
- ✅ Registro de routers para organizar endpoints
- ✅ Documentación automática de API
- ✅ Arquitectura modular con separación de rutas

🌐 RUTAS DISPONIBLES:
- /heroes      - CRUD con SQLModel ORM
- /heroes_sql  - CRUD con SQL puro  
- /docs        - Documentación automática (Swagger UI)
- /redoc       - Documentación alternativa (ReDoc)

🚀 PARA EJECUTAR:
uvicorn main:app --reload
o
fastapi dev main.py
"""

from fastapi import FastAPI

# 📦 Importar routers desde módulos organizados
from app.routes.heroes import router as heroes_router      # 🦸‍♂️ Rutas ORM
from app.routes.heroes_sql import router as heroes_sql_router  # 🦸‍♂️ Rutas SQL

# 🏗️  CREAR APLICACIÓN FASTAPI: Configuración principal
app = FastAPI(
    title="Heroes API",  # 📋 Nombre que aparece en la documentación
    description="API para gestión de héroes con implementaciones ORM y SQL",  # 📝 Descripción detallada
    version="1.0.0"  # 🔢 Versión de la API (importante para versionado)
)

# 🛣️  REGISTRAR ROUTERS: Organización modular de endpoints
# 
# 💡 ¿Por qué usar routers?
# - Separación de responsabilidades
# - Código más organizado y mantenible  
# - Diferentes equipos pueden trabajar en diferentes routers
# - Facilita testing de módulos específicos

# 🦸‍♂️ Router ORM: /heroes/* - Demostración usando SQLModel ORM
app.include_router(heroes_router)

# 🦸‍♂️ Router SQL: /heroes_sql/* - Demostración usando SQL puro  
app.include_router(heroes_sql_router)


@app.get("/")
def read_root():
    """
    🏠 ENDPOINT RAÍZ: Punto de entrada de la API
    
    Conceptos que aprenderás:
    - Endpoint simple sin parámetros
    - Respuesta JSON básica
    - Uso de decoradores FastAPI
    - Documentación automática con docstrings
    
    📝 PRUEBA:
    GET http://localhost:8000/
    
    📊 RESPUESTA:
    {"message": "Welcome to Heroes API"}
    """
    return {
        "message": "🦸‍♂️ Welcome to Heroes API",
        "endpoints": {
            "heroes_orm": "/heroes",
            "heroes_sql": "/heroes_sql", 
            "documentation": "/docs",
            "alternative_docs": "/redoc"
        },
        "learning": "Compare /heroes vs /heroes_sql to see ORM vs SQL differences!"
    }
