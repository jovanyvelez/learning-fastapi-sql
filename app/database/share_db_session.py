"""
🗄️  Database Session Management - Gestión de Sesiones de Base de Datos 🗄️

📚 PROPÓSITO EDUCATIVO:
Este archivo demuestra cómo configurar y gestionar conexiones a base de datos
de forma segura y eficiente en FastAPI usando el patrón de Dependency Injection.

🎯 CONCEPTOS QUE APRENDERÁS:
- ✅ Engine de SQLAlchemy para conexiones de BD
- ✅ Dependency Injection en FastAPI  
- ✅ Context Managers para gestión automática de recursos
- ✅ Anotaciones de tipo para mejor desarrollo
- ✅ Configuración centralizada de base de datos
- ✅ Patrón de sesiones por request

💡 PATRÓN:
Cada request HTTP obtiene su propia sesión de BD que se cierra automáticamente
al terminar el request, garantizando no memory leaks ni conexiones colgadas.
"""

from typing import Annotated
from fastapi import Depends

from sqlmodel import Session, create_engine

# Importar configuración centralizada
from app.config import settings

# 🐛 Log para verificar configuración (útil en desarrollo)
print("🔧 Comprobación de mismo hilo:", settings.CHECK_SAME_THREAD)

# 🏗️  CREAR ENGINE: Configuración de conexión a la base de datos
# Engine es el "motor" que maneja todas las conexiones a la BD
engine = create_engine(
    settings.DATABASE_URL,        # 📍 URL de conexión (ej: sqlite:///marvel.db)
    connect_args=settings.connect_args,  # 🔧 Argumentos específicos de SQLite  
    echo=settings.SQL_ECHO        # 🐛 Mostrar SQL en consola si está habilitado
)


def get_session():
    """
    🔄 GENERADOR DE SESIONES: Dependency Injection para FastAPI
    
    Conceptos que aprenderás:
    - Context manager (with statement) para manejo automático de recursos
    - yield en lugar de return para crear un generador
    - FastAPI cierra automáticamente la sesión al terminar el request
    - Transacciones automáticas con auto-commit/rollback
    
    📝 FLUJO:
    1. Request HTTP llega a un endpoint
    2. FastAPI llama a get_session()  
    3. Se crea nueva sesión para este request
    4. yield sesión al endpoint
    5. Endpoint usa la sesión
    6. Al terminar endpoint, sesión se cierra automáticamente
    
    💡 ¿Por qué yield en lugar de return?
    - yield convierte la función en un generador
    - Permite ejecutar código DESPUÉS de que el endpoint termine
    - FastAPI maneja automáticamente el cleanup
    """
    with Session(engine) as session:
        # 🎯 yield entrega la sesión al endpoint que la requiere
        # Cuando el endpoint termina, continúa aquí y cierra la sesión
        yield session


# 📝 ANOTACIÓN DE TIPO: Simplifica el uso de dependency injection
# SessionDep = Annotated[Session, Depends(get_session)]
# 
# ✨ MAGIA DE FASTAPI:
# En lugar de escribir: def create_hero(hero: HeroCreate, session: Session = Depends(get_session))
# Puedes escribir:      def create_hero(hero: HeroCreate, session: SessionDep)
#
# 🎯 BENEFICIOS:
# - Código más limpio y legible
# - Reutilizable en todos los endpoints
# - Tipado fuerte para autocompletado
# - Menos propenso a errores
SessionDep = Annotated[Session, Depends(get_session)]
