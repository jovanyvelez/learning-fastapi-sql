# 🦸‍♂️ Heroes API - Proyecto Educativo

## 📚 **Propósito Educativo**

Este proyecto está diseñado específicamente para **enseñar FastAPI y bases de datos** a estudiantes adolescentes. Compara dos enfoques diferentes para el mismo CRUD: **ORM vs SQL puro**.

## 🎯 **¿Qué aprenderás?**

### **Conceptos Fundamentales**
- ✅ **API REST** con FastAPI
- ✅ **CRUD** completo (Create, Read, Update, Delete)
- ✅ **Base de datos** SQLite
- ✅ **ORM vs SQL puro** - comparación directa
- ✅ **Validación de datos** con Pydantic
- ✅ **Configuración** con variables de entorno
- ✅ **Dependency Injection** en FastAPI

### **Habilidades Técnicas**
- ✅ Escribir consultas SQL
- ✅ Usar SQLModel ORM
- ✅ Manejar transacciones de base de datos
- ✅ Crear APIs documentadas automáticamente
- ✅ Estructurar proyectos profesionalmente

## 🏗️ **Arquitectura del Proyecto**

```
📁 proyecto/
├── 📄 main.py                 # Punto de entrada de la aplicación
├── 📁 app/
│   ├── 📄 config.py          # Configuración centralizada
│   ├── 📁 database/
│   │   ├── 📄 models.py      # Modelos de datos
│   │   └── 📄 share_db_session.py  # Gestión de sesiones BD
│   └── 📁 routes/
│       ├── 📄 heroes.py      # 🔵 CRUD con ORM
│       └── 📄 heroes_sql.py  # 🟡 CRUD con SQL puro
├── 📄 .env                   # Variables de entorno
└── 📄 marvel.db             # Base de datos SQLite
```

## 🚀 **Cómo empezar**

### **1. Instalar dependencias**
```bash
# Con uv (recomendado)
uv install

# O con pip
pip install fastapi sqlmodel uvicorn python-dotenv
```

### **2. Ejecutar la aplicación**
```bash
# Con uv
uv run fastapi dev main.py

# O con uvicorn
uvicorn main:app --reload
```

### **3. Explorar la API**
- 🌐 **Aplicación**: http://localhost:8000
- 📖 **Documentación**: http://localhost:8000/docs
- 📚 **Docs alternativas**: http://localhost:8000/redoc

## 🔄 **Comparación: ORM vs SQL**

| Aspecto | ORM (`/heroes`) | SQL Puro (`/heroes_sql`) |
|---------|-----------------|--------------------------|
| **Facilidad** | ✅ Muy fácil | ⚡ Requiere conocer SQL |
| **Código** | ✅ Menos líneas | 📝 Más explícito |
| **Control** | ⚖️ Limitado | ✅ Control total |
| **Performance** | ⚡ Buena | ✅ Optimizable |
| **Portabilidad** | ✅ Multi-BD | ⚖️ Específico de BD |

## 📝 **Ejercicios Progresivos**

### **Nivel Principiante**
1. **Explorar endpoints**: Prueba todos los endpoints en `/docs`
2. **Crear héroe**: Usa POST para crear tu superhéroe favorito
3. **Comparar respuestas**: ¿Notas diferencias entre `/heroes` y `/heroes_sql`?

### **Nivel Intermedio**
4. **Leer código**: Compara `heroes.py` vs `heroes_sql.py`
5. **Modificar edad**: Usa PATCH para cambiar la edad de un héroe
6. **Buscar por ID**: Prueba GET con IDs que existen y que no existen

### **Nivel Avanzado**
7. **Agregar validación**: ¿Qué pasa si envías edad negativa?
8. **Nuevo campo**: Añade `powers: list[str]` a los modelos
9. **Búsqueda**: Implementa endpoint para buscar por nombre

## 🧪 **Ejemplos de Uso**

### **Crear un héroe**
```bash
curl -X POST "http://localhost:8000/heroes/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Spider-Man",
    "age": 25,
    "secret_name": "Peter Parker"
  }'
```

### **Obtener todos los héroes**
```bash
curl "http://localhost:8000/heroes/"
```

### **Actualizar edad**
```bash
curl -X PATCH "http://localhost:8000/heroes/1" \
  -H "Content-Type: application/json" \
  -d '{"age": 26}'
```

## 🔧 **Configuración Avanzada**

### **Variables de entorno (.env)**
```env
# Configuración de base de datos
DATABASE_FILE=marvel.db
DATABASE_URL=sqlite:///marvel.db
CHECK_SAME_THREAD=false

# Debugging
SQL_ECHO=false  # Cambiar a 'true' para ver SQL en consola
```

## 🎓 **Plan de Aprendizaje Sugerido**

### **Semana 1-2: Fundamentos**
- Entender qué es una API REST
- Probar endpoints con la documentación automática
- Comprender JSON y HTTP status codes

### **Semana 3-4: CRUD Básico**
- Implementar CREATE (POST)
- Implementar READ (GET)
- Implementar UPDATE (PATCH)
- Implementar DELETE

### **Semana 5-6: Base de Datos**
- Entender diferencias ORM vs SQL
- Escribir consultas SQL básicas
- Comprender transacciones

### **Semana 7-8: Conceptos Avanzados**
- Validación de datos
- Manejo de errores
- Paginación
- Variables de entorno

## 🔍 **Conceptos Clave Explicados**

### **¿Qué es un ORM?**
Un **Object-Relational Mapping** traduce automáticamente entre objetos Python y tablas de base de datos. Es como un traductor que convierte:
```python
# Código Python (ORM)
hero = Hero(name="Spider-Man", age=25)
session.add(hero)

# Se convierte automáticamente en SQL
# INSERT INTO heroes (name, age) VALUES ('Spider-Man', 25)
```

### **¿Por qué comparar ORM vs SQL?**
- **ORM**: Más fácil, menos código, mejor para principiantes
- **SQL**: Más control, mejor performance, mejor para casos complejos

### **¿Qué es Dependency Injection?**
Un patrón donde FastAPI automáticamente "inyecta" dependencias (como sesiones de BD) en tus funciones:
```python
def create_hero(hero: HeroCreate, session: SessionDep):
    # FastAPI automáticamente crea y pasa 'session'
```

## 🐛 **Debugging y Troubleshooting**

### **Ver SQL generado**
Cambia `SQL_ECHO=true` en `.env` para ver todas las consultas SQL en la consola.

### **Errores comunes**
1. **"Table doesn't exist"**: Asegúrate de que `marvel.db` existe
2. **"Module not found"**: Verifica que estás en el directorio correcto
3. **"Port already in use"**: Otro proceso usa el puerto 8000

## 🎮 **Desafíos Extra**

1. **🏆 Nivel Héroe**: Añade un campo `powers` como lista de strings
2. **🏆 Nivel Súper**: Implementa búsqueda por nombre con LIKE
3. **🏆 Nivel Leyenda**: Añade una tabla `Teams` con relación many-to-many

## 💡 **Tips para Estudiantes**

1. **Experimenta**: No tengas miedo de romper cosas
2. **Lee los errores**: Los mensajes de error son tus amigos
3. **Usa la documentación**: `/docs` es increíblemente útil
4. **Compara código**: Mira las diferencias entre archivos
5. **Pregunta**: Si no entiendes algo, ¡pregunta!

## 🤝 **Contribuir**

¿Tienes ideas para mejorar este proyecto educativo?
- Añade más comentarios explicativos
- Crea ejercicios adicionales
- Mejora los ejemplos
- Reporta errores o confusiones

---

**¡Feliz aprendizaje! 🚀 Recuerda: el mejor código es el que entiendes.** 🧠✨
