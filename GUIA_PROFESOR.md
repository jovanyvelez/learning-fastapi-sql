# 👨‍🏫 Guía del Profesor - Heroes API

## 📋 **Información General del Curso**

### **🎯 Objetivos de Aprendizaje**
Al finalizar este curso, los estudiantes serán capaces de:
- ✅ Desarrollar APIs REST completas con FastAPI
- ✅ Diseñar y manejar bases de datos relacionales
- ✅ Comparar y contrastar ORM vs SQL puro
- ✅ Aplicar mejores prácticas de desarrollo web
- ✅ Estructurar proyectos de software profesionalmente

### **👥 Audiencia Objetivo**
- **Edad**: 15-18 años (educación secundaria)
- **Prerrequisitos**: Python básico, conceptos de programación
- **Nivel**: Intermedio a avanzado
- **Tamaño de clase**: 8-25 estudiantes

### **⏱️ Duración Total**
- **8 sesiones** de 90 minutos cada una
- **Total**: 12 horas académicas
- **Modalidad**: Presencial con práctica en computadora
- **El tiempo estimado puede ser superior debido a los conocimientos previos de los estudiantes y motivación de aprendizaje**
---

## 📅 **Plan de Sesiones Detallado**

### **🚀 SESIÓN 1: Fundamentos y Configuración**
**⏱️ Duración**: 90 minutos

#### **📚 Objetivos de la Sesión**
- Entender qué es una API REST
- Configurar el entorno de desarrollo
- Ejecutar la primera aplicación FastAPI

#### **🕐 Cronograma**
| Tiempo | Actividad | Método |
|--------|-----------|---------|
| 0-15 min | Introducción teórica: ¿Qué es una API? | Exposición + ejemplos |
| 15-30 min | Configuración del entorno (Python, uv, VS Code) | Práctica guiada |
| 30-45 min | Clonación y exploración del proyecto | Hands-on |
| 45-60 min | Primera ejecución de la aplicación | Práctica individual |
| 60-75 min | Exploración de la documentación automática | Descubrimiento guiado |
| 75-90 min | Reflexión y Q&A | Discusión grupal |

#### **🎯 Puntos Clave a Enfatizar**
- **API REST**: "Una forma de que aplicaciones se comuniquen por internet"
- **FastAPI**: "Python que genera documentación automáticamente"
- **Documentación**: "http://localhost:8000/docs es tu mejor amigo"

#### **📝 Actividades Prácticas**
1. **Configuración del entorno** (15 min)
   ```bash
   # Verificar instalaciones
   python --version
   uv --version
   ```

2. **Primera ejecución** (20 min)
   ```bash
   uv run fastapi dev main.py
   ```

3. **Exploración de endpoints** (15 min)
   - Probar GET / en el navegador
   - Explorar /docs
   - Identificar diferencias entre /heroes y /heroes_sql

#### **🏠 Tarea para Casa**
- Leer README_EDUCATIVO.md completo
- Completar Ejercicio 1 de EJERCICIOS.md
- Reflexionar: "¿Qué diferencias notas entre /heroes y /heroes_sql?"

#### **📊 Evaluación**
- **Formativa**: Observación durante la práctica
- **Criterios**: ¿Logró ejecutar la aplicación? ¿Entiende el concepto de API?

---

### **📊 SESIÓN 2: Anatomía de una API REST**
**⏱️ Duración**: 90 minutos

#### **📚 Objetivos de la Sesión**
- Comprender métodos HTTP (GET, POST, PATCH, DELETE)
- Entender códigos de estado HTTP
- Realizar operaciones CRUD básicas

#### **🕐 Cronograma**
| Tiempo | Actividad | Método |
|--------|-----------|---------|
| 0-20 min | Teoría: Métodos HTTP y códigos de estado | Exposición interactiva |
| 20-40 min | Práctica: Crear primer héroe (POST) | Demostración + práctica |
| 40-60 min | Práctica: Leer héroes (GET) | Práctica individual |
| 60-75 min | Práctica: Actualizar héroe (PATCH) | Trabajo en parejas |
| 75-90 min | Práctica: Eliminar héroe (DELETE) | Práctica individual |

#### **🎯 Puntos Clave a Enfatizar**
- **GET**: "Pedir información"
- **POST**: "Crear algo nuevo"
- **PATCH**: "Cambiar algo existente"
- **DELETE**: "Eliminar algo"
- **Status Codes**: "200 = éxito, 404 = no encontrado, 422 = datos incorretos"

#### **📝 Actividades Prácticas**
1. **Crear superhéroe favorito** (20 min)
   ```json
   {
     "name": "Tu Superhéroe",
     "age": 25,
     "secret_name": "Tu Identidad"
   }
   ```

2. **Operaciones CRUD completas** (30 min)
   - Crear 3 héroes diferentes
   - Listar todos los héroes
   - Actualizar la edad de uno
   - Eliminar uno

3. **Manejo de errores** (15 min)
   - Intentar obtener héroe con ID inexistente
   - Intentar crear héroe sin nombre

#### **🏠 Tarea para Casa**
- Completar Ejercicios 2-3 de EJERCICIOS.md
- Crear una "familia de superhéroes" (mínimo 4 miembros)

#### **📊 Evaluación**
- **Formativa**: Revisión de ejercicios en clase
- **Criterios**: ¿Completa CRUD exitosamente? ¿Entiende status codes?

---

### **🗄️ SESIÓN 3: Bases de Datos y Modelos**
**⏱️ Duración**: 90 minutos

#### **📚 Objetivos de la Sesión**
- Entender qué es una base de datos relacional
- Comprender el concepto de modelos y schemas
- Explorar la estructura de datos del proyecto

#### **🕐 Cronograma**
| Tiempo | Actividad | Método |
|--------|-----------|---------|
| 0-25 min | Teoría: Bases de datos relacionales | Exposición + diagramas |
| 25-45 min | Exploración: Archivo models.py | Lectura de código guiada |
| 45-65 min | Práctica: Diferencias entre schemas | Análisis comparativo |
| 65-80 min | Herencia en modelos (HeroBase) | Demostración conceptual |
| 80-90 min | Discusión: ¿Por qué separar modelos? | Reflexión grupal |

#### **🎯 Puntos Clave a Enfatizar**
- **Base de Datos**: "Como un Excel pero más poderoso y seguro"
- **Modelos**: "La estructura de nuestros datos"
- **Herencia**: "Compartir características comunes"
- **Schemas**: "Diferentes vistas del mismo dato según el contexto"

#### **📝 Actividades Prácticas**
1. **Exploración de models.py** (30 min)
   - Identificar campos en HeroBase
   - Comparar HeroPublic vs HeroCreate
   - Entender por qué HeroUpdate tiene campos opcionales

2. **Análisis de seguridad** (20 min)
   - ¿Por qué secret_name no está en HeroPublic?
   - ¿Qué información es segura exponer?

3. **Diseño de nuevos modelos** (15 min)
   - Brainstorm: "Si agregáramos una tabla Teams, ¿qué campos tendría?"

#### **🏠 Tarea para Casa**
- Leer todos los comentarios en models.py
- Completar Ejercicio 4 de EJERCICIOS.md
- Reflexionar: "¿Qué otros schemas necesitaríamos para una app real?"

#### **📊 Evaluación**
- **Formativa**: Participación en análisis de código
- **Criterios**: ¿Identifica diferencias entre schemas? ¿Entiende herencia?

---

### **🔍 SESIÓN 4: SQL Puro vs ORM - Introducción**
**⏱️ Duración**: 90 minutos

#### **📚 Objetivos de la Sesión**
- Entender qué es SQL y para qué sirve
- Comprender el concepto de ORM
- Comparar ventajas y desventajas de cada enfoque

#### **🕐 Cronograma**
| Tiempo | Actividad | Método |
|--------|-----------|---------|
| 0-20 min | Teoría: ¿Qué es SQL? | Exposición + ejemplos básicos |
| 20-40 min | Teoría: ¿Qué es un ORM? | Comparación visual |
| 40-60 min | Práctica: Comparar heroes.py vs heroes_sql.py | Análisis de código |
| 60-80 min | Actividad: Crear héroe en ambos endpoints | Práctica comparativa |
| 80-90 min | Discusión: Ventajas y desventajas | Mesa redonda |

#### **🎯 Puntos Clave a Enfatizar**
- **SQL**: "El idioma que entienden las bases de datos"
- **ORM**: "Un traductor entre Python y SQL"
- **Trade-offs**: "ORM es más fácil, SQL da más control"

#### **📝 Actividades Prácticas**
1. **Análisis comparativo** (30 min)
   - Contar líneas de código en cada función create_hero
   - Identificar dónde aparece SQL explícito
   - Observar manejo de transacciones

2. **Experimento práctico** (25 min)
   - Crear el mismo héroe usando ambos endpoints
   - Comparar respuestas
   - Habilitar SQL_ECHO para ver queries generadas

#### **🏠 Tarea para Casa**
- Completar Ejercicios 5-6 de EJERCICIOS.md
- Leer comentarios completos en heroes.py y heroes_sql.py

#### **📊 Evaluación**
- **Formativa**: Calidad del análisis comparativo
- **Criterios**: ¿Identifica diferencias clave? ¿Entiende trade-offs?

---

### **⚙️ SESIÓN 5: SQL en Profundidad**
**⏱️ Duración**: 90 minutos

#### **📚 Objetivos de la Sesión**
- Escribir consultas SQL básicas
- Entender parámetros seguros vs SQL injection
- Explorar conceptos avanzados como RETURNING

#### **🕐 Cronograma**
| Tiempo | Actividad | Método |
|--------|-----------|---------|
| 0-25 min | Teoría: SQL básico (SELECT, INSERT, UPDATE, DELETE) | Exposición interactiva |
| 25-45 min | Práctica: Escribir consultas SQL simples | Ejercicios guiados |
| 45-65 min | Seguridad: SQL injection y parámetros | Demostración + prevención |
| 65-80 min | Conceptos avanzados: RETURNING, transacciones | Análisis de código |
| 80-90 min | Práctica: Modificar una consulta SQL | Hands-on |

#### **🎯 Puntos Clave a Enfatizar**
- **SQL Injection**: "¡NUNCA concatenar strings en SQL!"
- **Parámetros**: ":name es seguro, '{name}' es peligroso"
- **RETURNING**: "Para obtener datos de lo que acabas de insertar"
- **Transacciones**: "Todo o nada"

#### **📝 Actividades Prácticas**
1. **SQL básico** (30 min)
   ```sql
   -- Ejercicios de escritura
   SELECT * FROM heroes WHERE age > 25;
   INSERT INTO heroes (name, age) VALUES ('Test', 30);
   UPDATE heroes SET age = 31 WHERE name = 'Test';
   DELETE FROM heroes WHERE name = 'Test';
   ```

2. **Análisis de seguridad** (20 min)
   - Comparar consulta segura vs insegura
   - Identificar parámetros en el código

3. **Modificación práctica** (15 min)
   - Cambiar una consulta para incluir un nuevo campo

#### **🏠 Tarea para Casa**
- Completar Ejercicio 9 de EJERCICIOS.md (SQL_ECHO)
- Investigar: "¿Qué otros tipos de inyección de código existen?"

#### **📊 Evaluación**
- **Formativa**: Ejercicios de SQL en clase
- **Criterios**: ¿Escribe SQL correcto? ¿Entiende conceptos de seguridad?

---

### **🔧 SESIÓN 6: Configuración y Arquitectura**
**⏱️ Duración**: 90 minutos

#### **📚 Objetivos de la Sesión**
- Entender variables de entorno y configuración
- Comprender dependency injection
- Explorar la arquitectura del proyecto

#### **🕐 Cronograma**
| Tiempo | Actividad | Método |
|--------|-----------|---------|
| 0-20 min | Teoría: Variables de entorno | Exposición + ejemplos |
| 20-40 min | Práctica: Modificar configuración (.env) | Experimentación |
| 40-60 min | Concepto: Dependency Injection | Demostración conceptual |
| 60-75 min | Arquitectura: Separación de responsabilidades | Tour del código |
| 75-90 min | Discusión: ¿Por qué esta estructura? | Análisis crítico |

#### **🎯 Puntos Clave a Enfatizar**
- **Variables de entorno**: "Configuración sin cambiar código"
- **Dependency Injection**: "FastAPI te da lo que necesitas automáticamente"
- **Separación**: "Cada archivo tiene una responsabilidad específica"
- **Escalabilidad**: "Esta estructura funciona para proyectos grandes"

#### **📝 Actividades Prácticas**
1. **Experimentar con configuración** (25 min)
   - Cambiar DATABASE_FILE en .env
   - Habilitar SQL_ECHO
   - Reiniciar y observar cambios

2. **Tour de arquitectura** (30 min)
   - main.py → punto de entrada
   - config.py → configuración centralizada
   - models.py → estructura de datos
   - routes/ → lógica de negocio
   - database/ → gestión de BD

#### **🏠 Tarea para Casa**
- Leer todos los comentarios en config.py y share_db_session.py
- Reflexionar: "¿Cómo agregarías autenticación a esta estructura?"

#### **📊 Evaluación**
- **Formativa**: Comprensión de la arquitectura
- **Criterios**: ¿Entiende la separación de responsabilidades?

---

### **🚀 SESIÓN 7: Conceptos Avanzados**
**⏱️ Duración**: 90 minutos

#### **📚 Objetivos de la Sesión**
- Implementar funcionalidad nueva
- Entender validación y manejo de errores
- Explorar conceptos de testing

#### **🕐 Cronograma**
| Tiempo | Actividad | Método |
|--------|-----------|---------|
| 0-25 min | Práctica: Implementar búsqueda por nombre | Desarrollo guiado |
| 25-45 min | Validación: Límites y restricciones | Experimentación |
| 45-65 min | Manejo de errores: Status codes apropiados | Análisis de casos |
| 65-80 min | Introducción al testing | Demostración básica |
| 80-90 min | Reflexión: Calidad de software | Discusión grupal |

#### **🎯 Puntos Clave a Enfatizar**
- **Extensibilidad**: "El código limpio es fácil de extender"
- **Validación**: "Nunca confíes en los datos del usuario"
- **Testing**: "Código que verifica que tu código funciona"
- **Calidad**: "Código que otros pueden entender y mantener"

#### **📝 Actividades Prácticas**
1. **Implementar búsqueda** (30 min)
   ```python
   @router.get("/search")
   def search_heroes(name: str, session: SessionDep):
       # Implementar juntos
   ```

2. **Testing básico** (20 min)
   - Probar con datos válidos e inválidos
   - Verificar códigos de estado

#### **🏠 Tarea para Casa**
- Completar Ejercicios 7-8 de EJERCICIOS.md
- Implementar una funcionalidad propia (creatividad libre)

#### **📊 Evaluación**
- **Formativa**: Calidad de la implementación
- **Criterios**: ¿Sigue patrones establecidos? ¿Maneja errores apropiadamente?

---

### **🎯 SESIÓN 8: Proyecto Final y Reflexión**
**⏱️ Duración**: 90 minutos

#### **📚 Objetivos de la Sesión**
- Consolidar aprendizajes
- Presentar extensiones del proyecto
- Reflexionar sobre el proceso de aprendizaje

#### **🕐 Cronograma**
| Tiempo | Actividad | Método |
|--------|-----------|---------|
| 0-30 min | Presentaciones: Funcionalidades implementadas | Exposiciones estudiantiles |
| 30-50 min | Code Review: Mejores prácticas | Análisis grupal |
| 50-70 min | Reflexión: ORM vs SQL, cuándo usar cada uno | Mesa redonda |
| 70-85 min | Evaluación del curso y feedback | Retroalimentación |
| 85-90 min | Próximos pasos y recursos | Orientación futura |

#### **🎯 Puntos Clave a Enfatizar**
- **Aprendizaje continuo**: "Este es solo el comienzo"
- **Mejores prácticas**: "Código limpio, comentarios útiles, estructura clara"
- **Toma de decisiones**: "Cuándo usar ORM, cuándo SQL, depende del contexto"

#### **📝 Actividades de Cierre**
1. **Presentaciones estudiantiles** (30 min)
   - 3-5 minutos por estudiante/equipo
   - Mostrar funcionalidad implementada
   - Explicar decisiones técnicas

2. **Evaluación grupal** (20 min)
   - ¿Qué fue lo más difícil?
   - ¿Qué les gustó más?
   - ¿Qué aplicarían en otros proyectos?

#### **📊 Evaluación Final**
- **Sumativa**: Proyecto completo + presentación
- **Criterios**: Funcionalidad, código limpio, comprensión conceptual

---

## 📊 **Sistema de Evaluación**

### **🎯 Criterios de Evaluación**

#### **Conocimientos Técnicos (40%)**
- Comprensión de API REST
- Diferencias ORM vs SQL
- Estructura de base de datos
- Configuración de aplicaciones

#### **Habilidades Prácticas (40%)**
- Implementación de CRUD
- Escritura de código limpio
- Debugging y resolución de problemas
- Uso de herramientas de desarrollo

#### **Competencias Transversales (20%)**
- Trabajo en equipo
- Comunicación técnica
- Pensamiento crítico
- Aprendizaje autónomo

### **📋 Instrumentos de Evaluación**

1. **Evaluación Formativa Continua** (30%)
   - Participación en clase
   - Ejercicios completados
   - Preguntas y reflexiones

2. **Tareas y Ejercicios** (30%)
   - Ejercicios del archivo EJERCICIOS.md
   - Implementaciones propias
   - Análisis de código

3. **Proyecto Final** (40%)
   - Funcionalidad implementada
   - Calidad del código
   - Presentación final

---

## 🛠️ **Recursos y Preparación**

### **📚 Materiales Necesarios**
- **Hardware**: Computadoras con Python 3.11+
- **Software**: VS Code, Git, navegador web
- **Archivos**: Proyecto completo descargado
- **Internet**: Para documentación y recursos

### **👨‍🏫 Preparación del Profesor**

#### **Antes del Curso**
1. **Dominar el contenido técnico**
   - Ejecutar todo el proyecto personalmente
   - Completar todos los ejercicios
   - Familiarizarse con errores comunes

2. **Preparar el entorno**
   - Instalar herramientas en todas las computadoras
   - Verificar conexión a internet
   - Preparar respaldos del proyecto

3. **Planificar adaptaciones**
   - Identificar estudiantes que necesiten apoyo extra
   - Preparar ejercicios adicionales para estudiantes avanzados
   - Planificar agrupaciones para trabajo colaborativo

#### **Durante las Sesiones**
- **Monitoreo activo**: Circular entre estudiantes
- **Apoyo individualizado**: Ayuda específica según necesidades
- **Gestión del tiempo**: Mantener ritmo apropiado
- **Documentación**: Anotar dificultades comunes para futuras mejoras

---

## 🎯 **Estrategias Pedagógicas**

### **🔄 Aprendizaje Constructivista**
- Los estudiantes construyen conocimiento comparando ORM vs SQL
- Experimentación guiada con código existente
- Reflexión sobre decisiones de diseño

### **👥 Aprendizaje Colaborativo**
- Trabajo en parejas para resolución de problemas
- Discusiones grupales sobre mejores prácticas
- Peer review de código

### **🎯 Aprendizaje Basado en Proyectos**
- Un proyecto real que evoluciona a lo largo del curso
- Aplicación práctica inmediata de conceptos
- Productos tangibles al final de cada sesión

### **🔍 Aprendizaje por Descubrimiento**
- Exploración de código con comentarios educativos
- Experimentación con configuraciones
- Análisis comparativo de enfoques

---

## 🆘 **Solución de Problemas Comunes**

### **🐛 Errores Técnicos Frecuentes**

1. **"ModuleNotFoundError"**
   - **Causa**: Entorno virtual no activado
   - **Solución**: `uv run` antes de comandos

2. **"Port already in use"**
   - **Causa**: Aplicación ya ejecutándose
   - **Solución**: Cerrar procesos o cambiar puerto

3. **"Table doesn't exist"**
   - **Causa**: Base de datos no inicializada
   - **Solución**: Verificar marvel.db existe

### **🎓 Desafíos Pedagógicos**

1. **Diferentes ritmos de aprendizaje**
   - **Estrategia**: Ejercicios opcionales avanzados
   - **Apoyo**: Tutorías entre pares

2. **Conceptos abstractos**
   - **Estrategia**: Analogías y ejemplos concretos
   - **Refuerzo**: Visualizaciones y diagramas

3. **Motivación variable**
   - **Estrategia**: Proyectos personalizables
   - **Engagement**: Competencias amigables

---

## 📈 **Extensiones y Mejoras**

### **🚀 Para Estudiantes Avanzados**
- Implementar autenticación JWT
- Añadir relaciones many-to-many (Teams)
- Crear frontend con React/Vue
- Implementar tests automatizados
- Deploy en la nube

### **📚 Cursos Siguientes**
- **Backend Avanzado**: Microservicios, Redis, Celery
- **Frontend**: React/Vue con esta API
- **DevOps**: Docker, CI/CD, deployment
- **Base de Datos**: PostgreSQL, optimización

### **🌐 Integración Curricular**
- **Matemáticas**: Análisis de performance, estadísticas
- **Inglés**: Documentación técnica, comunicación
- **Arte**: Diseño de interfaces, UX/UI

---

## 📝 **Plantillas de Evaluación**

### **📊 Rúbrica de Proyecto Final**

| Criterio | Excelente (4) | Bueno (3) | Satisfactorio (2) | Necesita Mejora (1) |
|----------|---------------|-----------|-------------------|---------------------|
| **Funcionalidad** | Implementa CRUD + funcionalidad extra | CRUD completo funciona | CRUD básico funciona | CRUD parcialmente funcional |
| **Código** | Limpio, comentado, sigue patrones | Mayormente limpio | Funcional pero desordenado | Difícil de entender |
| **Comprensión** | Explica conceptos claramente | Entiende la mayoría | Comprensión básica | Conceptos confusos |
| **Creatividad** | Implementación innovadora | Alguna personalización | Sigue ejemplos exactos | Sin personalización |

### **📋 Lista de Verificación por Sesión**

**Sesión 1: Fundamentos**
- [ ] Configura entorno correctamente
- [ ] Ejecuta aplicación exitosamente
- [ ] Explora documentación automática
- [ ] Identifica endpoints disponibles

**Sesión 2: CRUD**
- [ ] Crea héroe usando POST
- [ ] Lista héroes usando GET
- [ ] Actualiza héroe usando PATCH
- [ ] Elimina héroe usando DELETE
- [ ] Comprende códigos de estado

...*(continuar para todas las sesiones)*

---

## 🎯 **Consejos Finales para el Profesor**

### **💡 Claves del Éxito**
1. **Paciencia**: Conceptos nuevos requieren tiempo
2. **Práctica**: Más código, menos teoría
3. **Comparación**: ORM vs SQL es el differenciador
4. **Relevancia**: Conectar con intereses de estudiantes
5. **Celebración**: Reconocer logros pequeños

### **⚠️ Errores a Evitar**
1. **Demasiada teoría**: Los adolescentes necesitan práctica
2. **Ritmo muy rápido**: Verificar comprensión constantemente
3. **Ignorar errores**: Los errores son oportunidades de aprendizaje
4. **Código perfecto**: Permitir experimentación y "código feo"
5. **Evaluación punitiva**: Fomentar aprendizaje, no castigar errores

### **🎪 Mantener el Engagement**
- **Gamificación**: Competencias de velocidad de implementación
- **Personalización**: Permitir temas alternativos a superhéroes
- **Relevancia**: Conectar con apps que usan diariamente
- **Comunidad**: Crear ambiente de aprendizaje colaborativo

---

**¡Buena suerte con tu curso! 🚀 Recuerda: el mejor profesor es el que aprende junto con sus estudiantes.** 🎓✨
