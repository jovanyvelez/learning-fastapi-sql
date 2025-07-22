"""
⚙️  Settings and Configuration Management - Gestión de Configuración ⚙️

📚 PROPÓSITO EDUCATIVO:
Este archivo demuestra mejores prácticas para manejar configuración en aplicaciones web:
- Variables de entorno para diferentes ambientes (dev, test, prod)
- Patrón Singleton para configuración global
- Separación de configuración del código

🎯 CONCEPTOS QUE APRENDERÁS:
- ✅ Variables de entorno con python-dotenv
- ✅ Patrón Singleton con @lru_cache()
- ✅ @property para valores computados
- ✅ Valores por defecto para configuración
- ✅ Configuración específica por base de datos
- ✅ Separación de configuración y código

📁 ARCHIVO .env:
Crea un archivo .env en la raíz del proyecto con:
DATABASE_FILE=marvel.db
CHECK_SAME_THREAD=false
SQL_ECHO=false

⚠️  NUNCA subas archivos .env a git (contienen secretos)
"""
import os
from functools import lru_cache

# 📦 python-dotenv carga variables del archivo .env
from dotenv import load_dotenv

# 🔄 Cargar variables de entorno desde .env al iniciar la aplicación
load_dotenv()


class Settings:
    """
    ⚙️  CLASE DE CONFIGURACIÓN: Centraliza toda la configuración de la app
    
    Conceptos que aprenderás:
    - Variables de entorno con os.getenv()
    - Valores por defecto para desarrollo local
    - Configuración específica de base de datos
    - @property para valores computados dinámicamente
    
    🌍 VARIABLES DE ENTORNO:
    Permiten diferentes configuraciones sin cambiar código:
    - Desarrollo: DATABASE_FILE=dev.db
    - Testing: DATABASE_FILE=test.db  
    - Producción: DATABASE_FILE=prod.db
    """
    
    # 📁 Configuración de Base de Datos
    # os.getenv("VARIABLE", "default") busca la variable en .env o usa default
    DATABASE_FILE: str = os.getenv("DATABASE_FILE", "marvel.db")
    DATABASE_URL: str = os.getenv("DATABASE_URL", f"sqlite:///{DATABASE_FILE}")
    
    # 🔧 Configuración específica de SQLite
    # CHECK_SAME_THREAD=False permite usar SQLite desde múltiples threads
    CHECK_SAME_THREAD: bool = os.getenv("CHECK_SAME_THREAD", "false").lower() == "true"
    
    # 🐛 SQL_ECHO=True muestra las consultas SQL en la consola (útil para debugging)
    SQL_ECHO: bool = os.getenv("SQL_ECHO", "false").lower() == "true"
        
    @property
    def connect_args(self) -> dict:
        """
        🔌 ARGUMENTOS DE CONEXIÓN: Configuración específica para SQLite
        
        @property convierte este método en un atributo computado.
        Se calcula dinámicamente cada vez que se accede.
        
        📝 USO: settings.connect_args
        📊 RETORNA: {"check_same_thread": False}
        """
        return {"check_same_thread": self.CHECK_SAME_THREAD}


@lru_cache()
def get_settings() -> Settings:
    """
    🎯 PATRÓN SINGLETON: Una sola instancia de configuración en toda la app
    
    Conceptos que aprenderás:
    - @lru_cache() cachea el resultado de la función
    - Singleton garantiza una sola instancia global
    - Mejora performance (no recrea Settings cada vez)
    - Consistencia en toda la aplicación
    
    💡 ¿Por qué Singleton para configuración?
    - Configuración no cambia durante la ejecución
    - Evita crear múltiples objetos Settings
    - Garantiza que toda la app use la misma configuración
    
    📝 USO: settings = get_settings()
    """
    return Settings()


# 🌍 INSTANCIA GLOBAL: Disponible en toda la aplicación
# Esta es la forma recomendada de acceder a la configuración
settings = get_settings()
