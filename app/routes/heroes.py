"""
🦸‍♂️ Heroes API routes using SQLModel ORM 🦸‍♂️

📚 PROPÓSITO EDUCATIVO:
Este archivo demuestra cómo crear una API REST usando SQLModel ORM.
Compara este archivo con heroes_sql.py para ver las diferencias entre ORM y SQL puro.

🎯 CONCEPTOS QUE APRENDERÁS:
- ✅ ORM (Object-Relational Mapping) - Mapeo de objetos a tablas
- ✅ SQLModel como abstracción sobre SQL
- ✅ Operaciones CRUD sin escribir SQL manualmente  
- ✅ Relaciones automáticas entre modelos
- ✅ Transacciones automáticas con session.commit()
- ✅ Validación automática con Pydantic

💡 VENTAJAS del ORM:
- Menos código SQL manual
- Prevención automática de SQL injection
- Tipado fuerte con autocompletado
- Portabilidad entre diferentes bases de datos

⚖️  DESVENTAJAS del ORM:
- Menos control sobre el SQL generado
- Puede ser más lento en consultas complejas
- Curva de aprendizaje adicional
"""
from typing import Annotated

# FastAPI imports - Framework web para crear APIs REST
from fastapi import APIRouter, HTTPException, Query

# SQLModel imports - ORM que combina SQLAlchemy + Pydantic
from sqlmodel import select  # Constructor de consultas SQL de forma pythónica

# Imports locales - Nuestros modelos y configuración
from app.database.share_db_session import SessionDep  # Dependencia de sesión DB
from app.database.models import Hero, HeroCreate, HeroPublic, HeroUpdate

# 🛣️  Router: Agrupa endpoints relacionados con héroes (versión ORM)
# prefix="/heroes" significa que todas las rutas empiezan con /heroes
router = APIRouter(prefix="/heroes", tags=["heroes"])


@router.post("/", response_model=HeroPublic)
def create_hero(hero: HeroCreate, session: SessionDep):
    """
    🎯 LECCIÓN 1: CREAR un nuevo héroe usando SQLModel ORM
    
    Conceptos que aprenderás aquí:
    - ORM maneja automáticamente el SQL INSERT
    - model_validate() convierte schemas a modelos de tabla
    - session.add() añade objeto a la sesión (no a la BD aún)
    - session.commit() guarda cambios en la base de datos
    - session.refresh() actualiza objeto con datos de la BD (como el ID)
    
    📝 COMPARACIÓN con SQL puro:
    ORM: 4 líneas de código
    SQL: ~15 líneas con manejo manual de RETURNING
    
    🔄 FLUJO:
    1. Convertir HeroCreate a modelo Hero
    2. Añadir a sesión (en memoria)
    3. Confirmar transacción (guardar en BD)
    4. Refrescar para obtener ID generado
    """
    
    # PASO 1: Convertir schema HeroCreate a modelo de tabla Hero
    # 💡 model_validate() toma los datos de HeroCreate y crea un objeto Hero
    # 🔄 Equivale a: Hero(name=hero.name, age=hero.age, secret_name=hero.secret_name)
    db_hero = Hero.model_validate(hero)
    
    # PASO 2: Añadir el objeto a la sesión (aún no está en la BD)
    # 📝 session.add() marca el objeto para ser insertado
    session.add(db_hero)
    
    # PASO 3: Confirmar la transacción (guardar en base de datos)
    # 💾 session.commit() ejecuta el INSERT automáticamente
    session.commit()
    
    # PASO 4: Refrescar el objeto para obtener datos generados por la BD
    # 🆔 session.refresh() ejecuta un SELECT para obtener el ID auto-generado
    # 🔄 Equivale al RETURNING en la versión SQL
    session.refresh(db_hero)
    
    # PASO 5: Devolver el objeto (automáticamente se convierte a HeroPublic)
    return db_hero


@router.get("/", response_model=list[HeroPublic])
def read_heroes(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    """
    🎯 LECCIÓN 2: OBTENER todos los héroes con paginación usando ORM
    
    Conceptos que aprenderás aquí:
    - select() constructor de consultas pythónico
    - Métodos .offset() y .limit() para paginación
    - session.exec() ejecuta la consulta construida
    - .all() obtiene todos los resultados como lista
    
    📝 COMPARACIÓN con SQL puro:
    ORM: select(Hero).offset(offset).limit(limit)
    SQL: "SELECT id, name, age FROM heroes ORDER BY id LIMIT :limit OFFSET :offset"
    
    💡 VENTAJA: El ORM genera automáticamente el SQL óptimo
    """
    
    # PASO 1: Construir consulta usando el constructor select()
    # 🏗️  select(Hero) equivale a "SELECT * FROM heroes"
    # 📄 .offset() y .limit() añaden paginación automáticamente
    # 🔄 SQLModel genera el ORDER BY automáticamente para consistencia
    query = select(Hero).offset(offset).limit(limit)
    
    # PASO 2: Ejecutar la consulta y obtener todos los resultados
    # 🚀 session.exec() ejecuta la consulta construida
    # 📊 .all() devuelve lista de objetos Hero (no Row objects como en SQL puro)
    heroes = session.exec(query).all()
    
    print(f"🦸‍♂️ Heroes retornados con ORM: {len(heroes)}")  # Log para debugging
    
    # PASO 3: Devolver lista (conversión automática a HeroPublic)
    # ✨ SQLModel convierte automáticamente Hero -> HeroPublic
    return heroes


@router.get("/{hero_id}", response_model=HeroPublic)
def read_hero(hero_id: int, session: SessionDep):
    """
    🎯 LECCIÓN 3: OBTENER un héroe específico por ID usando ORM
    
    Conceptos que aprenderás aquí:
    - session.get() método directo para buscar por clave primaria
    - Simplicidad del ORM vs consultas SQL manuales
    - Manejo automático de tipos de datos
    
    📝 COMPARACIÓN con SQL puro:
    ORM: session.get(Hero, hero_id)
    SQL: "SELECT id, name, age FROM heroes WHERE id = :hero_id" + fetchone()
    
    💡 VENTAJA: Una sola línea de código para operación común
    """
    
    # PASO 1: Buscar héroe por ID usando session.get()
    # 🎯 session.get(Modelo, id) es el método más eficiente para buscar por clave primaria
    # 🔍 Automáticamente ejecuta "SELECT * FROM heroes WHERE id = ?"
    hero = session.get(Hero, hero_id)
    
    # PASO 2: Validar que el héroe existe
    if not hero:
        # 🚫 HTTP 404 = "Not Found" - El recurso solicitado no existe
        raise HTTPException(status_code=404, detail="Hero not found")
    
    # PASO 3: Devolver el héroe (conversión automática a HeroPublic)
    return hero


@router.patch("/{hero_id}", response_model=HeroPublic)
def update_hero(hero_id: int, hero: HeroUpdate, session: SessionDep):
    """
    🎯 LECCIÓN 4: ACTUALIZAR un héroe usando ORM (SIMPLE vs SQL)
    
    Conceptos que aprenderás aquí:
    - session.get() para obtener el objeto a modificar
    - sqlmodel_update() para actualización parcial automática
    - ORM maneja automáticamente campos opcionales
    - Transacciones automáticas más simples
    
    📝 COMPARACIÓN con SQL puro:
    ORM: 6 líneas simples
    SQL: ~30 líneas con construcción dinámica de queries
    
    💡 VENTAJA: ORM maneja automáticamente la lógica de actualización parcial
    """
    
    # PASO 1: Obtener el héroe existente de la base de datos
    hero_db = session.get(Hero, hero_id)
    if not hero_db:
        raise HTTPException(status_code=404, detail="Hero not found")
    
    # PASO 2: Extraer solo los campos que fueron enviados
    # 🎯 exclude_unset=True ignora campos no enviados (igual que en SQL)
    hero_data = hero.model_dump(exclude_unset=True)
    
    # PASO 3: Actualizar el objeto con los nuevos datos
    # ✨ sqlmodel_update() es un método mágico que actualiza solo campos enviados
    # 🔄 Equivale a hero_db.name = hero_data["name"] para cada campo
    hero_db.sqlmodel_update(hero_data)
    
    # PASO 4: Guardar cambios en la base de datos
    session.add(hero_db)  # Marcar objeto como modificado
    session.commit()      # Ejecutar UPDATE automáticamente
    session.refresh(hero_db)  # Refrescar objeto con datos actualizados
    
    return hero_db


@router.delete("/{hero_id}")
def delete_hero(hero_id: int, session: SessionDep):
    """
    🎯 LECCIÓN 5: ELIMINAR un héroe usando ORM
    
    Conceptos que aprenderás aquí:
    - session.delete() marca objeto para eliminación
    - ORM maneja automáticamente el SQL DELETE
    - Validación y transacciones simplificadas
    
    📝 COMPARACIÓN con SQL puro:
    ORM: 4 líneas simples
    SQL: ~10 líneas con validación manual y DELETE
    
    💡 VENTAJA: Menos posibilidad de errores, código más legible
    """
    
    # PASO 1: Obtener el héroe a eliminar
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    
    # PASO 2: Marcar objeto para eliminación
    # 🗑️  session.delete() marca el objeto para ser eliminado
    session.delete(hero)
    
    # PASO 3: Confirmar la eliminación
    # 💾 session.commit() ejecuta el DELETE automáticamente
    session.commit()
    
    # PASO 4: Devolver confirmación
    return {"ok": True}
