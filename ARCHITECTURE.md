# 🏗️ Arquitectura del Proyecto - Heroes API Educativo

## 📝 Descripción
Esta aplicación FastAPI con SQLModel ha sido diseñada específicamente como **herramienta educativa** para enseñar desarrollo web moderno. La estructura sigue buenas prácticas profesionales mientras mantiene claridad pedagógica.

## 🗂️ Estructura de Carpetas

```
sqlmodel-practice/
├── main.py                           # 🚀 Punto de entrada de la aplicación
├── .env                             # ⚙️  Variables de entorno (NO en git)
├── .gitignore                       # 🚫 Archivos excluidos de git
├── pyproject.toml                   # 📦 Configuración del proyecto (uv/pip)
├── uv.lock                         # 🔒 Lock de dependencias (uv)
├── marvel.db                       # 🗄️  Base de datos SQLite
│
├── 📚 DOCUMENTACIÓN EDUCATIVA/
│   ├── README_EDUCATIVO.md         # 📖 Guía completa para estudiantes
│   ├── EJERCICIOS.md              # 📝 Ejercicios progresivos por niveles
│   ├── GUIA_PROFESOR.md           # 👨‍🏫 Plan de curso completo (8 sesiones)
│   └── ARCHITECTURE.md            # 🏗️  Este archivo
│
└── app/                           # 📁 Paquete principal de la aplicación
    ├── __init__.py
    ├── config.py                  # ⚙️  Configuración centralizada + variables de entorno
    │
    ├── database/                  # 🗄️  Gestión de base de datos
    │   ├── __init__.py
    │   ├── models.py             # 🏗️  Modelos de datos (Hero, HeroCreate, etc.)
    │   └── share_db_session.py   # 🔄 Sesiones de BD + dependency injection
    │
    └── routes/                   # 🛣️  Endpoints de la API
        ├── __init__.py
        ├── heroes.py            # 🦸‍♂️ CRUD con SQLModel ORM
        └── heroes_sql.py        # 🦸‍♂️ CRUD con SQL puro (comparación educativa)
```

## 🎯 Beneficios de la Arquitectura Educativa

### 1. **🔄 Comparación Directa ORM vs SQL**
- **`heroes.py`**: Implementación con SQLModel ORM (fácil de entender)
- **`heroes_sql.py`**: Implementación con SQL puro (control total)
- **Misma funcionalidad**: Ambos endpoints hacen exactamente lo mismo
- **Aprendizaje**: Los estudiantes ven las diferencias lado a lado

### 2. **📚 Documentación Integrada**
- **Comentarios educativos**: Cada línea de código explicada
- **Conceptos clave**: Explicaciones contextualizadas
- **Ejercicios progresivos**: De principiante a avanzado
- **Guía completa**: Para profesores con plan de 8 sesiones

### 3. **⚙️ Configuración Profesional**
- **Variables de entorno**: Configuración sin hardcoding
- **Patrón Singleton**: `@lru_cache()` para settings
- **Dependency Injection**: FastAPI con tipado fuerte
- **Seguridad**: `secret_name` no se expone en respuestas públicas

### 4. **🏗️ Separación de Responsabilidades**
- **`models.py`**: Estructura de datos con herencia educativa
- **`config.py`**: Configuración centralizada
- **`share_db_session.py`**: Gestión de sesiones de BD
- **`main.py`**: Punto de entrada limpio

### 5. **📈 Escalabilidad Educativa**
- Fácil agregar nuevos endpoints para ejercicios
- Estructura clara para estudiantes
- Patrones profesionales reales
- Base para proyectos más complejos

## 🚀 Comandos para Ejecutar

### 📱 Desarrollo Local (Recomendado)
```bash
# Con uv (gestor moderno de paquetes Python)
uv run fastapi dev main.py

# La aplicación estará disponible en:
# 🌐 http://localhost:8000
# 📖 http://localhost:8000/docs (documentación automática)
# 📚 http://localhost:8000/redoc (documentación alternativa)
```

### ⚙️ Con Uvicorn Directamente
```bash
# Si prefieres uvicorn tradicional
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### 🔧 Comandos de Desarrollo
```bash
# Instalar dependencias
uv install

# Verificar que la aplicación se importa correctamente
uv run python -c "import main; print('✅ Aplicación funciona')"

# Verificar configuración de base de datos
uv run python -c "from app.config import settings; print(f'BD: {settings.DATABASE_FILE}')"
```

## 📊 Endpoints Disponibles

### 🦸‍♂️ `/heroes` - Implementación ORM
- `GET /heroes/` - Listar héroes (con paginación)
- `POST /heroes/` - Crear héroe
- `GET /heroes/{id}` - Obtener héroe por ID
- `PATCH /heroes/{id}` - Actualizar héroe
- `DELETE /heroes/{id}` - Eliminar héroe

### 🦸‍♂️ `/heroes_sql` - Implementación SQL Puro
- `GET /heroes_sql/` - Listar héroes (con paginación)
- `POST /heroes_sql/` - Crear héroe
- `GET /heroes_sql/{id}` - Obtener héroe por ID
- `PATCH /heroes_sql/{id}` - Actualizar héroe
- `DELETE /heroes_sql/{id}` - Eliminar héroe

### ℹ️ Endpoints Informativos
- `GET /` - Información general de la API

## Próximos Pasos Sugeridos

1. **Agregar Tests**
   ```
   tests/
   ├── __init__.py
   ├── test_heroes.py
   └── conftest.py
   ```

2. **Agregar Configuración de Entorno**
   ```python
   # app/config/settings.py
   from pydantic_settings import BaseSettings
   
   class Settings(BaseSettings):
       database_url: str = "sqlite:///marvel.db"
       debug: bool = False
   ```

3. **Agregar Logging**
   ```python
   # app/config/logging.py
   import logging
   ```

4. **Agregar Middleware**
   ```python
   # app/middleware/
   ```

5. **Agregar Servicios (Business Logic)**
   ```python
   # app/services/hero_service.py
   ```

Esta estructura sigue las mejores prácticas de FastAPI y permite que tu aplicación crezca de manera organizada y mantenible.
