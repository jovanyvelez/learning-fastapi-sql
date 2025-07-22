"""
🦸‍♂️ Hero Database Models - Modelos de Datos para Héroes 🦸‍♂️

📚 PROPÓSITO EDUCATIVO:
Este archivo demuestra cómo diseñar modelos de datos en SQLModel usando herencia
y separación de responsabilidades para crear APIs seguras y bien estructuradas.

🎯 CONCEPTOS QUE APRENDERÁS:
- ✅ Herencia de modelos con clases base
- ✅ Separación entre modelo de tabla y schemas de API
- ✅ Validación automática con Pydantic
- ✅ Campos opcionales vs obligatorios
- ✅ Índices de base de datos para performance
- ✅ Seguridad: qué campos exponer públicamente

🏗️  ARQUITECTURA DE MODELOS:
- HeroBase: Campos comunes compartidos
- Hero: Modelo de tabla (almacenado en BD)
- HeroPublic: Schema para respuestas (sin secret_name)
- HeroCreate: Schema para creación (con secret_name)
- HeroUpdate: Schema para actualización (todos opcionales)

⚠️  SEGURIDAD: secret_name NO se expone en HeroPublic
"""
from sqlmodel import Field, SQLModel

class HeroBase(SQLModel):
    """
    🏗️  CLASE BASE: Campos comunes para todos los schemas de Hero
    
    Conceptos que aprenderás:
    - Herencia en modelos de datos
    - Field() para configuración avanzada de campos
    - Índices de base de datos para búsquedas rápidas
    - Tipos opcionales con Union (int | None)
    
    💡 ¿Por qué una clase base?
    - Evita duplicación de código (DRY: Don't Repeat Yourself)
    - Garantiza consistencia entre todos los schemas
    - Facilita mantenimiento y cambios futuros
    """
    
    # 🏷️  Nombre del héroe (requerido, indexado para búsquedas rápidas)
    # index=True crea un índice en la BD para búsquedas por nombre eficientes
    name: str = Field(index=True)
    
    # 🎂 Edad del héroe (opcional, también indexado)
    # int | None significa que puede ser un entero O None (nulo)
    # default=None significa que si no se proporciona, será None
    age: int | None = Field(default=None, index=True)


class HeroPublic(HeroBase):
    """
    📊 SCHEMA PÚBLICO: Para respuestas de API que ven los usuarios
    
    Conceptos que aprenderás:
    - Hereda de HeroBase (name, age)
    - Añade ID para identificación única
    - NO incluye secret_name por seguridad
    - Se usa en response_model de endpoints
    
    🔒 SEGURIDAD:
    Este es el modelo que ven los clientes de la API.
    NUNCA incluye información sensible como secret_name.
    
    📝 EJEMPLO DE RESPUESTA:
    {
        "id": 1,
        "name": "Spider-Man", 
        "age": 25
        // ❌ secret_name NO aparece aquí
    }
    """

    # 🆔 ID único del héroe (generado automáticamente por la BD)
    id: int


class HeroCreate(HeroBase):
    """
    ➕ SCHEMA DE CREACIÓN: Para crear nuevos héroes
    
    Conceptos que aprenderás:
    - Hereda campos comunes de HeroBase (name, age)
    - Añade secret_name REQUERIDO para creación
    - NO incluye ID (se genera automáticamente)
    - Se usa en el parámetro body de POST
    
    📝 EJEMPLO DE REQUEST:
    POST /heroes/
    {
        "name": "Spider-Man",
        "age": 25,
        "secret_name": "Peter Parker"  // ✅ Requerido para crear
    }
    
    💡 ¿Por qué secret_name es requerido aquí?
    Porque cuando creas un héroe, DEBES proporcionar su identidad secreta.
    """
    
    # 🕵️‍♂️ Identidad secreta del héroe (REQUERIDO para creación)
    secret_name: str


class HeroUpdate(HeroBase):
    """
    ✏️  SCHEMA DE ACTUALIZACIÓN: Para modificar héroes existentes (PATCH)
    
    Conceptos que aprenderás:
    - TODOS los campos son opcionales (pueden ser None)
    - Permite actualización parcial (solo cambiar edad, por ejemplo)
    - type: ignore para evitar warnings de mypy
    - Se usa en PATCH endpoints
    
    📝 EJEMPLOS DE REQUEST:
    PATCH /heroes/1
    {"age": 26}  // Solo cambiar edad
    
    PATCH /heroes/1  
    {"name": "Amazing Spider-Man", "age": 26}  // Cambiar múltiples campos
    
    💡 ¿Por qué todos opcionales?
    PATCH permite actualización parcial. El usuario puede enviar solo
    los campos que quiere cambiar, no todos.
    """
    
    # 🏷️  Nombre (opcional para actualización)
    name: str | None = None  # type: ignore
    
    # 🎂 Edad (opcional para actualización)  
    age: int | None = None
    
    # 🕵️‍♂️ Identidad secreta (opcional para actualización)
    secret_name: str | None = None



class Hero(HeroBase, table=True):
    """
    🗄️  MODELO DE TABLA: Representación real de la tabla en la base de datos
    
    Conceptos que aprenderás:
    - table=True convierte la clase en una tabla de BD
    - Hereda campos comunes de HeroBase
    - Incluye TODOS los campos (incluyendo secret_name)
    - primary_key=True para la clave primaria
    - __tablename__ para especificar nombre de tabla
    
    📊 ESTRUCTURA DE TABLA EN BD:
    CREATE TABLE heroes (
        id INTEGER PRIMARY KEY,
        name VARCHAR(255),
        age INTEGER, 
        secret_name VARCHAR(255)
    );
    
    🔑 CARACTERÍSTICAS:
    - Este modelo se usa internamente por el ORM
    - Contiene TODA la información (incluido secret_name)
    - Se convierte automáticamente a HeroPublic en respuestas
    """

    # 📋 Nombre de la tabla en la base de datos
    __tablename__ = "heroes"  # type: ignore
    
    # 🆔 Clave primaria (auto-incrementa, puede ser None antes de insertar)
    id: int | None = Field(default=None, primary_key=True)
    
    # 🕵️‍♂️ Identidad secreta (almacenada en BD pero NO en respuestas públicas)
    secret_name: str

