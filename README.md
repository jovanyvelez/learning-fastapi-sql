# 🦸‍♂️ SQLModel Practice - API de Héroes Marvel

## 📖 Introducción

Bienvenido al **SQLModel Practice**, un proyecto educativo diseñado para enseñar desarrollo de APIs web modernas utilizando **FastAPI** y **SQLModel**. Este proyecto está especialmente creado como herramienta pedagógica para estudiantes que quieren aprender desarrollo backend con Python.

## 🎯 ¿Qué es este proyecto?

Este es un **API REST completo** que gestiona una base de datos de héroes de Marvel, implementado con las mejores prácticas de desarrollo web moderno. El proyecto incluye:

- 🔥 **FastAPI**: Framework web rápido y moderno para crear APIs
- 🗄️ **SQLModel**: ORM moderno que combina SQLAlchemy con Pydantic
- 📊 **Doble implementación**: ORM vs SQL puro para fines educativos
- 📚 **Documentación automática**: Swagger UI y ReDoc integrados
- 🦸‍♂️ **Datos de ejemplo**: Base de datos pre-poblada con héroes Marvel

## 🚀 Características Principales

### ✨ Funcionalidades
- **CRUD completo**: Crear, leer, actualizar y eliminar héroes
- **Validación de datos**: Validaciones automáticas con Pydantic
- **Paginación**: Listado eficiente de grandes conjuntos de datos
- **Documentación interactiva**: Prueba la API directamente desde el navegador
- **Manejo de errores**: Respuestas HTTP apropiadas y mensajes claros

### 🏗️ Arquitectura Educativa
- **Separación clara de responsabilidades**: Modelos, rutas y configuración separados
- **Comentarios exhaustivos**: Cada línea explicada para facilitar el aprendizaje
- **Patrones de diseño**: Implementación de mejores prácticas de desarrollo
- **Comparación ORM vs SQL**: Dos implementaciones para entender diferencias

## 🛠️ Tecnologías Utilizadas

```python
# Stack tecnológico principal
FastAPI >= 0.116.1      # Framework web moderno
SQLModel >= 0.0.21      # ORM con Pydantic integrado
SQLite                  # Base de datos ligera y portátil
python-dotenv           # Gestión de variables de entorno
Uvicorn                 # Servidor ASGI para desarrollo
```

## 📁 Estructura del Proyecto

```
sqlmodel-practice/
├── 📄 main.py                    # Punto de entrada de la aplicación
├── 🗄️ marvel.db                 # Base de datos SQLite con datos
├── ⚙️ pyproject.toml             # Configuración del proyecto
├── 
├── 📂 app/                       # Código principal de la aplicación
│   ├── 🔧 config.py             # Configuración y variables de entorno
│   ├── 📂 database/             # Modelos y gestión de base de datos
│   │   ├── 🏛️ models.py         # Definición de modelos SQLModel
│   │   └── 🔗 share_db_session.py # Gestión de sesiones de BD
│   └── 📂 routes/               # Endpoints de la API
│       ├── 🦸‍♂️ heroes.py        # Rutas con implementación ORM
│       └── 🦸‍♂️ heroes_sql.py    # Rutas con implementación SQL pura
│
├── 📚 README_EDUCATIVO.md        # Guía completa para estudiantes
├── 📝 EJERCICIOS.md             # Ejercicios prácticos progresivos
├── 👨‍🏫 GUIA_PROFESOR.md          # Curriculum completo para profesores
└── 🏗️ ARCHITECTURE.md           # Documentación técnica detallada
```

## 🎓 ¿Para Quién es Este Proyecto?

### 👨‍🎓 Estudiantes
- **Principiantes** en desarrollo web con Python
- **Intermedios** que quieren aprender FastAPI y SQLModel
- **Cualquiera** interesado en APIs REST modernas

### 👨‍🏫 Profesores
- Curriculum completo de **8 sesiones** incluido
- Material didáctico listo para usar
- Ejercicios progresivos con soluciones

### 💻 Desarrolladores
- Ejemplo de **mejores prácticas** en FastAPI
- Patrón de **arquitectura limpia** para APIs
- Implementación de **testing** y **documentación**

## 🚀 Inicio Rápido

### 1️⃣ Clonar y Configurar
```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd sqlmodel-practice

# Instalar dependencias con uv (recomendado)
uv install
```

### 2️⃣ Ejecutar la Aplicación
```bash
# Ejecutar en modo desarrollo
uv run fastapi dev main.py

# ¡Listo! La API estará disponible en:
# 🌐 http://localhost:8000
```

### 3️⃣ Explorar la Documentación
```bash
# Documentación interactiva Swagger UI
# 📖 http://localhost:8000/docs

# Documentación alternativa ReDoc
# 📚 http://localhost:8000/redoc
```

## 🦸‍♂️ Ejemplos de Uso

### Obtener todos los héroes
```bash
curl http://localhost:8000/heroes/
```

### Crear un nuevo héroe
```bash
curl -X POST http://localhost:8000/heroes/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Spider-Man", "secret_name": "Peter Parker", "age": 23}'
```

### Buscar un héroe específico
```bash
curl http://localhost:8000/heroes/1
```

## 📚 Recursos Educativos

| 📄 Archivo | 🎯 Propósito | 👥 Audiencia |
|-------------|--------------|---------------|
| `README_EDUCATIVO.md` | Guía completa del estudiante | 👨‍🎓 Estudiantes |
| `EJERCICIOS.md` | Ejercicios prácticos progresivos | 👨‍🎓 Estudiantes |
| `GUIA_PROFESOR.md` | Curriculum de 8 sesiones | 👨‍🏫 Profesores |
| `ARCHITECTURE.md` | Documentación técnica | 💻 Desarrolladores |

## 🔄 Doble Implementación: ORM vs SQL

Este proyecto incluye **dos implementaciones** de la misma funcionalidad:

### 🔧 `/heroes` - Implementación ORM (SQLModel)
```python
# Ejemplo: Crear héroe con ORM
hero = Hero.model_validate(hero_create, update={"id": hero_id})
session.add(hero)
session.commit()
session.refresh(hero)
```

### 🔧 `/heroes_sql` - Implementación SQL Pura
```python
# Ejemplo: Crear héroe con SQL
cursor.execute(
    "INSERT INTO hero (name, secret_name, age) VALUES (?, ?, ?) RETURNING *",
    (hero_create.name, hero_create.secret_name, hero_create.age)
)
```

## 🎯 Objetivos de Aprendizaje

Al completar este proyecto, los estudiantes aprenderán:

- ✅ **Desarrollo de APIs REST** con FastAPI
- ✅ **Modelado de datos** con SQLModel
- ✅ **Operaciones CRUD** completas
- ✅ **Validación de datos** con Pydantic
- ✅ **Gestión de base de datos** SQLite
- ✅ **Documentación automática** de APIs
- ✅ **Mejores prácticas** de desarrollo Python
- ✅ **Comparación ORM vs SQL** puro

## 🙏 Reconocimientos

Este proyecto es una **adaptación educativa** del excelente tutorial oficial de FastAPI:

📖 **Tutorial Original**: [SQL (Relational) Databases - FastAPI](https://fastapi.tiangolo.com/es/tutorial/sql-databases/)

**Adaptaciones realizadas para fines educativos:**
- ✨ **Comentarios exhaustivos** en español para facilitar el aprendizaje
- 🔄 **Doble implementación** (ORM vs SQL puro) para comparación educativa
- 📚 **Materiales pedagógicos** completos (guías, ejercicios, curriculum)
- 🦸‍♂️ **Temática Marvel** para hacer el aprendizaje más atractivo
- 🏗️ **Estructura modular** optimizada para enseñanza progresiva

**Agradecimientos especiales a:**
- 👨‍💻 **Sebastián Ramírez (tiangolo)** - Creador de FastAPI y SQLModel
- 🌟 **Comunidad FastAPI** - Por la documentación y ejemplos excepcionales

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Este es un proyecto educativo y cualquier mejora que ayude al aprendizaje será apreciada.

## 📝 Licencia

Este proyecto está diseñado con fines educativos. Siéntete libre de usarlo, modificarlo y compartirlo para enseñar desarrollo web con Python.

---

## 🚀 ¡Comienza Ahora!

```bash
# Un solo comando para empezar
uv run fastapi dev main.py
```

**¡Visita http://localhost:8000/docs y comienza a explorar! 🦸‍♂️**