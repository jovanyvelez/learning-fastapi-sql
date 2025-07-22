"""
🦸‍♂️ Heroes API routes using RAW SQL 🦸‍♂️

📚 PROPÓSITO EDUCATIVO:
Este archivo demuestra cómo crear una API REST usando SQL puro en lugar de un ORM.
Compara este archivo con heroes.py para ver las diferencias entre ORM y SQL.

🎯 CONCEPTOS QUE APRENDERÁS:
- ✅ Consultas SQL parametrizadas (previenen SQL injection)
- ✅ Transacciones automáticas vs manuales
- ✅ RETURNING clause para obtener datos insertados
- ✅ Construcción dinámica de queries
- ✅ Manejo de errores en bases de datos
- ✅ Paginación con LIMIT/OFFSET

⚠️  IMPORTANTE: Siempre usa parámetros (:name) en lugar de concatenación de strings
"""
from typing import Annotated

# FastAPI imports - Framework web para crear APIs REST
from fastapi import APIRouter, HTTPException, Query

# SQLModel imports - ORM y utilidades SQL
from sqlmodel import select, text  # text() convierte strings en SQL ejecutable

# Imports locales - Nuestros modelos y configuración
from app.database.share_db_session import SessionDep  # Dependencia de sesión DB
from app.database.models import Hero, HeroCreate, HeroPublic, HeroUpdate

# 🛣️  Router: Agrupa endpoints relacionados con héroes (versión SQL)
# prefix="/heroes_sql" significa que todas las rutas empiezan con /heroes_sql
router = APIRouter(prefix="/heroes_sql", tags=["heroes_sql"])


@router.post("/", response_model=HeroPublic)
def create_hero(hero: HeroCreate, session: SessionDep):
    """
    🎯 LECCIÓN 1: CREAR un nuevo héroe usando SQL puro
    
    Conceptos que aprenderás aquí:
    - INSERT con parámetros seguros (:name, :age, :secret_name)
    - RETURNING para obtener el ID auto-generado por la base de datos
    - Cómo evitar SQL injection usando parámetros
    - Transacciones automáticas con result.first()
    
    📝 FLUJO:
    1. Definir SQL con parámetros seguros
    2. Ejecutar con datos validados por Pydantic
    3. Obtener resultado (activa auto-commit)
    4. Convertir a formato de respuesta
    """
    
    # PASO 1: Definir la consulta SQL con parámetros seguros
    # ⚠️  NUNCA uses f"INSERT ... VALUES ('{hero.name}')" - Es vulnerable a SQL injection
    # ✅ SIEMPRE usa :name - SQLAlchemy escapa automáticamente los valores
    sql = text("""
        INSERT INTO heroes (name, age, secret_name) 
        VALUES (:name, :age, :secret_name)
        RETURNING id, name, age
    """)
    
    # PASO 2: Ejecutar la consulta con datos del objeto hero
    # Los datos vienen del JSON enviado por el cliente y son validados por Pydantic
    result = session.execute(sql, {
        "name": hero.name,        # ✅ Validado por HeroCreate schema
        "age": hero.age,          # ✅ Debe ser un entero positivo  
        "secret_name": hero.secret_name  # ✅ Campo privado, no se devuelve en la respuesta
    })
    
    # PASO 3: Obtener el resultado (esto activa el auto-commit)
    # 💡 result.first() consume el resultado y activa la transacción automática
    row = result.first()
    if not row:
        # Si no hay resultado, algo salió mal en la inserción
        raise HTTPException(status_code=500, detail="Failed to create hero")
    
    # PASO 4: Convertir el resultado a formato de respuesta
    # 📊 HeroPublic NO incluye secret_name por seguridad
    return HeroPublic(
        id=row.id,      # 🆔 ID generado automáticamente por SQLite (autoincrement)
        name=row.name,  # 📝 Nombre del héroe (público)
        age=row.age     # 🎂 Edad del héroe (público)
        # ❌ secret_name NO se incluye - información privada
    )


@router.get("/", response_model=list[HeroPublic])
def read_heroes(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    """
    🎯 LECCIÓN 2: OBTENER todos los héroes con paginación usando SQL puro
    
    Conceptos que aprenderás aquí:
    - SELECT con ORDER BY para resultados consistentes
    - LIMIT y OFFSET para paginación eficiente
    - Query parameters opcionales en FastAPI
    - Conversión de múltiples resultados a lista de objetos
    
    📝 PARÁMETROS:
    - offset: Cuántos registros saltar (para paginación)
    - limit: Máximo de registros a devolver (máx. 100)
    
    📊 EJEMPLOS DE USO:
    - GET /heroes_sql/ → Primeros 100 héroes
    - GET /heroes_sql/?limit=10 → Primeros 10 héroes  
    - GET /heroes_sql/?offset=10&limit=10 → Héroes 11-20
    """
    
    # PASO 1: Definir consulta con paginación
    # 🔄 ORDER BY id asegura resultados consistentes en cada página
    # 📄 LIMIT controla cuántos registros devolver
    # ⏭️  OFFSET controla desde qué registro empezar
    sql = text("""
        SELECT id, name, age 
        FROM heroes 
        ORDER BY id 
        LIMIT :limit OFFSET :offset
    """)
    
    # PASO 2: Ejecutar consulta con parámetros de paginación
    result = session.execute(sql, {"limit": limit, "offset": offset})
    
    # PASO 3: Obtener TODOS los resultados como lista
    # 💡 fetchall() devuelve una lista de Row objects
    rows = result.fetchall()
    
    # PASO 4: Convertir cada Row a HeroPublic usando list comprehension
    # 🔄 Esto es más eficiente que un bucle for tradicional
    heroes = [
        HeroPublic(id=row.id, name=row.name, age=row.age)
        for row in rows
    ]
    
    print(f"🦸‍♂️ Heroes retornados con SQL: {len(heroes)}")  # Log para debugging
    return heroes


@router.get("/{hero_id}", response_model=HeroPublic)
def read_hero(hero_id: int, session: SessionDep):
    """
    🎯 LECCIÓN 3: OBTENER un héroe específico por ID usando SQL puro
    
    Conceptos que aprenderás aquí:
    - Path parameters en FastAPI ({hero_id})
    - SELECT con WHERE clause para filtrar
    - Manejo de casos donde no se encuentra el registro
    - Diferencia entre fetchone() y fetchall()
    
    📝 FLUJO:
    1. Recibir hero_id desde la URL (ej: /heroes_sql/123)
    2. Buscar el héroe en la base de datos
    3. Devolver error 404 si no existe
    4. Devolver el héroe si existe
    """
    
    # PASO 1: Definir consulta para buscar UN héroe específico
    # 🎯 WHERE id = :hero_id filtra por el ID recibido en la URL
    sql = text("""
        SELECT id, name, age 
        FROM heroes 
        WHERE id = :hero_id
    """)
    
    # PASO 2: Ejecutar consulta con el ID específico
    result = session.execute(sql, {"hero_id": hero_id})
    
    # PASO 3: Obtener UNA fila (fetchone vs fetchall)
    # 💡 fetchone() devuelve solo la primera fila o None si no hay resultados
    # 🆚 fetchall() devolvería una lista (innecesario aquí)
    row = result.fetchone()
    
    # PASO 4: Validar que el héroe existe
    if not row:
        # 🚫 HTTP 404 = "Not Found" - El recurso solicitado no existe
        raise HTTPException(status_code=404, detail="Hero not found")
    
    # PASO 5: Convertir el resultado a HeroPublic
    return HeroPublic(
        id=row.id,
        name=row.name,
        age=row.age
    )


@router.patch("/{hero_id}", response_model=HeroPublic)
def update_hero(hero_id: int, hero: HeroUpdate, session: SessionDep):
    """
    🎯 LECCIÓN 4: ACTUALIZAR un héroe usando SQL dinámico (AVANZADO)
    
    Conceptos AVANZADOS que aprenderás aquí:
    - PATCH vs PUT (actualización parcial vs completa)
    - Construcción dinámica de consultas SQL
    - exclude_unset=True para campos opcionales
    - Múltiples consultas en una transacción
    - Commit manual necesario (sin RETURNING)
    
    📝 DIFERENCIAS:
    - PATCH: Solo actualiza campos enviados (ej: solo "age": 26)
    - PUT: Requiere todos los campos (reemplaza completo)
    
    ⚡ RETO: ¿Puedes entender por qué necesitamos session.commit() aquí?
    """
    
    # PASO 1: Verificar que el héroe existe antes de actualizar
    # 💡 Siempre validar existencia antes de modificar
    sql_check = text("SELECT COUNT(*) as count FROM heroes WHERE id = :hero_id")
    result = session.execute(sql_check, {"hero_id": hero_id})
    count_row = result.fetchone()
    if not count_row or count_row.count == 0:
        raise HTTPException(status_code=404, detail="Hero not found")
    
    # PASO 2: Extraer solo los campos que fueron enviados
    # 🎯 exclude_unset=True ignora campos no enviados en el JSON
    # Ejemplo: Si solo envías {"age": 26}, hero_data = {"age": 26}
    hero_data = hero.model_dump(exclude_unset=True)
    if not hero_data:
        # Si no hay datos para actualizar, devolver el héroe actual sin cambios
        sql_select = text("SELECT id, name, age FROM heroes WHERE id = :hero_id")
        result = session.execute(sql_select, {"hero_id": hero_id})
        row = result.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Hero not found")
        return HeroPublic(id=row.id, name=row.name, age=row.age)
    
    # PASO 3: Construir UPDATE dinámicamente
    # 🔧 Creamos la cláusula SET solo para campos enviados
    set_clauses = []  # Lista de "campo = :valor"
    params = {"hero_id": hero_id}  # Parámetros para la consulta
    
    # 🔄 Por cada campo enviado, añadir a SET clause
    if "name" in hero_data:
        set_clauses.append("name = :name")
        params["name"] = hero_data["name"]
    if "age" in hero_data:
        set_clauses.append("age = :age")
        params["age"] = hero_data["age"]
    if "secret_name" in hero_data:
        set_clauses.append("secret_name = :secret_name")
        params["secret_name"] = hero_data["secret_name"]
    
    # PASO 4: Ejecutar UPDATE con campos dinámicos
    # 💡 ', '.join(set_clauses) convierte lista en "name = :name, age = :age"
    sql_update = text(f"""
        UPDATE heroes 
        SET {', '.join(set_clauses)}
        WHERE id = :hero_id
    """)
    
    # ⚠️  Aquí SÍ necesitamos commit manual porque no usamos RETURNING
    session.execute(sql_update, params)
    session.commit()  # 🔑 IMPORTANTE: Sin esto los cambios se pierden
    
    # PASO 5: Obtener el héroe actualizado para devolver
    sql_select = text("SELECT id, name, age FROM heroes WHERE id = :hero_id")
    result = session.execute(sql_select, {"hero_id": hero_id})
    row = result.fetchone()
    
    if not row:
        raise HTTPException(status_code=404, detail="Hero not found after update")
    
    return HeroPublic(
        id=row.id,
        name=row.name,
        age=row.age
    )


@router.delete("/{hero_id}")
def delete_hero(hero_id: int, session: SessionDep):
    """
    🎯 LECCIÓN 5: ELIMINAR un héroe usando SQL puro
    
    Conceptos que aprenderás aquí:
    - DELETE statement con WHERE clause
    - Validación antes de eliminar (buena práctica)
    - Transacciones manuales (sin RETURNING)
    - Respuestas sin modelo específico
    
    📝 FLUJO:
    1. Verificar que el héroe existe
    2. Eliminar el registro
    3. Confirmar la transacción
    4. Devolver confirmación de éxito
    
    ⚠️  CUIDADO: DELETE es irreversible - siempre validar antes
    """
    
    # PASO 1: Verificar que el héroe existe antes de eliminar
    # 🛡️  NUNCA elimines sin verificar - es una buena práctica de seguridad
    sql_check = text("SELECT COUNT(*) as count FROM heroes WHERE id = :hero_id")
    result = session.execute(sql_check, {"hero_id": hero_id})
    count_row = result.fetchone()
    
    if not count_row or count_row.count == 0:
        # 🚫 HTTP 404 si el héroe no existe
        raise HTTPException(status_code=404, detail="Hero not found")
    
    # PASO 2: Eliminar el héroe de la base de datos
    # 🗑️  DELETE FROM tabla WHERE condicion
    sql_delete = text("DELETE FROM heroes WHERE id = :hero_id")
    session.execute(sql_delete, {"hero_id": hero_id})
    
    # PASO 3: Confirmar la transacción manualmente
    # ⚠️  SIN session.commit() los cambios NO se guardan permanentemente
    session.commit()
    
    # PASO 4: Devolver confirmación de éxito
    # 💡 No hay response_model porque devolvemos un dict simple
    # ✅ HTTP 200 con mensaje de confirmación
    return {"ok": True}