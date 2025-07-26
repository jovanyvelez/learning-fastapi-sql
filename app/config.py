"""
⚙️  Settings and Configuration Management - Gestión de Configuración ⚙️

📚 PROPÓSITO EDUCATIVO:
Este archivo demuestra mejores prácticas para manejar configuración en aplicaciones web:
- Variables de entorno
- Separación de configuración del código
- Configuración centralizada y fácil de mantener

🎯 CONCEPTOS QUE APRENDERÁS:
- ✅ Variables de entorno con python-dotenv
- ✅ Constructor __init__() para inicialización
- ✅ Valores por defecto para configuración
- ✅ Configuración específica por base de datos
- ✅ Separación de configuración y código
- ✅ Instanciación simple y directa

📁 ARCHIVO .env:
Crea un archivo .env en la raíz del proyecto con:
DATABASE_FILE=marvel.db
CHECK_SAME_THREAD=false
SQL_ECHO=false

⚠️  NUNCA subas archivos .env a git (contienen secretos)
"""
import os

# 📦 python-dotenv carga variables del archivo .env
from dotenv import load_dotenv

# 🔄 Cargar variables de entorno desde .env al iniciar la aplicación
load_dotenv()


class Settings:
    """
    ⚙️  CLASE DE CONFIGURACIÓN: Centraliza toda la configuración de la app
    
    🎓 ENFOQUE EDUCATIVO SIMPLE:
    Usamos __init__() porque es:
    - Familiar para estudiantes que aprenden OOP
    - Más directo: todo se calcula una vez al crear la instancia
    - Sin complejidad adicional de patrones avanzados
    - Eficiente: los valores se calculan una sola vez
    
    Conceptos que aprenderás:
    - Variables de entorno con os.getenv()
    - Valores por defecto para desarrollo local
    - Configuración específica de base de datos
    - Constructor __init__() para inicialización
    
    🌍 VARIABLES DE ENTORNO:
    Permiten diferentes configuraciones sin cambiar código:
    - Desarrollo: DATABASE_FILE=dev.db
    - Testing: DATABASE_FILE=test.db  
    - Producción: DATABASE_FILE=prod.db
    """
    
    def __init__(self):
        """
        🏗️ CONSTRUCTOR: Inicializa toda la configuración al crear la instancia
        
        📝 ¿Por qué en __init__()?
        - Se ejecuta una sola vez al crear Settings()
        - Todos los valores se calculan inmediatamente
        - Más eficiente que calcular cada vez que se accede
        - Más fácil de entender para estudiantes principiantes
        """
        
        # 📁 Configuración de Base de Datos
        # os.getenv("VARIABLE", "default") busca la variable en .env o usa default
        self.DATABASE_FILE = os.getenv("DATABASE_FILE", "marvel.db")
        self.DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{self.DATABASE_FILE}")
        
        # 🔧 Configuración específica de SQLite
        # CHECK_SAME_THREAD=False permite usar SQLite desde múltiples threads
        # 
        # 🧵 ¿Qué es un thread (hilo)?
        # Un thread es como una "línea de ejecución" independiente en tu programa
        # Imagina que tu programa puede hacer varias tareas al mismo tiempo:
        # Thread 1: Procesar request del usuario A
        # Thread 2: Procesar request del usuario B  
        # Thread 3: Procesar request del usuario C
        # Cada uno trabaja en paralelo, como tener varios empleados atendiendo clientes
        # 
        # 🧵 ¿Qué es CHECK_SAME_THREAD?
        # Por defecto, SQLite solo permite acceso desde el thread que creó la conexión
        # En aplicaciones web (como FastAPI), diferentes requests pueden usar threads diferentes
        # Si CHECK_SAME_THREAD=True (default), obtendríamos errores como:
        # "SQLite objects created in a thread can only be used in that same thread"
        # 
        # 🔓 ¿Por qué False?
        # - FastAPI puede manejar requests en diferentes threads
        # - SQLModel/SQLAlchemy gestiona las conexiones de forma segura
        # - False permite que la misma conexión sea usada por múltiples threads
        # 
        # ⚠️  IMPORTANTE: Solo es seguro porque SQLModel maneja la sincronización
        self.CHECK_SAME_THREAD = os.getenv("CHECK_SAME_THREAD", "false").lower() == "true"
        
        # 🐛 SQL_ECHO=True muestra las consultas SQL en la consola (útil para debugging)
        self.SQL_ECHO = os.getenv("SQL_ECHO", "false").lower() == "true"
        
        # 🔌 Argumentos de conexión - se calcula una vez y se reutiliza
        # Más eficiente que calcular dinámicamente cada vez que se accede
        self.connect_args = {"check_same_thread": self.CHECK_SAME_THREAD}


# 🌍 INSTANCIA GLOBAL: Simple y directa
# Esta es la forma más clara para estudiantes principiantes
# Crear Settings() es rápido y no necesita optimización compleja
settings = Settings()

