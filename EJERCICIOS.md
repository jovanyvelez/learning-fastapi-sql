# 📝 Ejercicios Prácticos - Heroes API

## 🎯 **Instrucciones Generales**

1. **Ejecuta la aplicación**: `uv run fastapi dev main.py`
2. **Abre la documentación**: http://localhost:8000/docs
3. **Completa los ejercicios** en orden
4. **Compara** tus resultados con las soluciones

---

## 📚 **EJERCICIOS NIVEL PRINCIPIANTE**

### **🏅 Ejercicio 1: Exploración de API**
**Objetivo**: Familiarizarte con la documentación automática

**Tareas**:
1. Ve a http://localhost:8000/docs
2. Explora todos los endpoints disponibles
3. Identifica las diferencias entre `/heroes` y `/heroes_sql`

**Preguntas**:
- ¿Cuántos endpoints tiene cada router?
- ¿Qué métodos HTTP están disponibles?
- ¿Qué schemas de datos se usan?

---

### **🏅 Ejercicio 2: Tu Primer Héroe**
**Objetivo**: Crear tu superhéroe favorito

**Tareas**:
1. Usa el endpoint `POST /heroes/` 
2. Crea un héroe con estos datos:
   ```json
   {
     "name": "Tu Héroe Favorito",
     "age": 25,
     "secret_name": "Tu Nombre Real"
   }
   ```
3. Anota el ID que se devuelve

**Resultado esperado**: Respuesta con status 200 y el héroe creado con ID

---

### **🏅 Ejercicio 3: Comparación ORM vs SQL**
**Objetivo**: Ver las diferencias en la práctica

**Tareas**:
1. Crea el mismo héroe usando `POST /heroes_sql/`
2. Compara las respuestas de ambos endpoints
3. Lista todos los héroes con `GET /heroes/` y `GET /heroes_sql/`

**Preguntas**:
- ¿Son idénticas las respuestas?
- ¿Qué IDs tienen los héroes creados?
- ¿Notas alguna diferencia en velocidad?

---

## 📖 **EJERCICIOS NIVEL INTERMEDIO**

### **🏅 Ejercicio 4: Lectura de Código**
**Objetivo**: Entender las diferencias en el código

**Tareas**:
1. Abre `app/routes/heroes.py`
2. Abre `app/routes/heroes_sql.py`
3. Compara la función `create_hero` en ambos archivos

**Preguntas**:
- ¿Cuántas líneas tiene cada función?
- ¿Cuál usa SQL explícito?
- ¿Cuál manejas transacciones manualmente?

---

### **🏅 Ejercicio 5: Actualización Parcial**
**Objetivo**: Practicar PATCH requests

**Tareas**:
1. Crea un héroe con edad 20
2. Usa `PATCH /heroes/{id}` para cambiar solo la edad a 25
3. Verifica que el nombre NO cambió
4. Repite con `/heroes_sql/{id}`

**Datos de prueba**:
```json
// Creación
{
  "name": "Young Hero",
  "age": 20,
  "secret_name": "Student Name"
}

// Actualización
{
  "age": 25
}
```

---

### **🏅 Ejercicio 6: Manejo de Errores**
**Objetivo**: Entender códigos de error HTTP

**Tareas**:
1. Intenta obtener un héroe con ID 999999
2. Intenta actualizar un héroe inexistente
3. Intenta eliminar un héroe inexistente

**Preguntas**:
- ¿Qué status code devuelve cada caso?
- ¿Son consistentes entre ORM y SQL?
- ¿Qué mensaje de error aparece?

---

## 🚀 **EJERCICIOS NIVEL AVANZADO**

### **🏅 Ejercicio 7: Paginación**
**Objetivo**: Entender la paginación de resultados

**Tareas**:
1. Crea 5 héroes diferentes
2. Obtén héroes con `limit=2` y `offset=0`
3. Obtén la siguiente página con `offset=2`
4. Experimenta con diferentes valores

**URLs de prueba**:
- `GET /heroes/?limit=2&offset=0`
- `GET /heroes/?limit=2&offset=2`
- `GET /heroes/?limit=10&offset=0`

---

### **🏅 Ejercicio 8: Validación de Datos**
**Objetivo**: Probar los límites de validación

**Tareas**:
1. Intenta crear un héroe sin nombre
2. Intenta crear un héroe con edad negativa
3. Intenta crear un héroe con campos extra

**Datos de prueba problemáticos**:
```json
// Sin nombre
{
  "age": 25,
  "secret_name": "Secret"
}

// Edad negativa
{
  "name": "Hero",
  "age": -5,
  "secret_name": "Secret"
}

// Campo extra
{
  "name": "Hero",
  "age": 25,
  "secret_name": "Secret",
  "power_level": 9000
}
```

---

### **🏅 Ejercicio 9: Investigación SQL**
**Objetivo**: Ver el SQL generado por el ORM

**Tareas**:
1. Cambia `SQL_ECHO=true` en el archivo `.env`
2. Reinicia la aplicación
3. Ejecuta operaciones en `/heroes/`
4. Observa el SQL en la consola

**Preguntas**:
- ¿Qué SQL genera `session.add()` + `session.commit()`?
- ¿Qué SQL genera `session.get(Hero, id)`?
- ¿Es diferente del SQL manual en `/heroes_sql/`?

---

## 🎯 **DESAFÍOS CREATIVOS**

### **🏆 Desafío 1: Superhéroe Completo**
Crea un superhéroe con una historia completa:
- Nombre interesante
- Edad lógica
- Identidad secreta creativa
- Prueba TODAS las operaciones CRUD con él

### **🏆 Desafío 2: Familia de Héroes**
Crea una familia de superhéroes:
- Al menos 4 miembros
- Edades coherentes
- Usa paginación para verlos
- Elimina y recrea algunos

### **🏆 Desafío 3: Comparación de Performance**
- Crea 10 héroes usando ORM
- Crea 10 héroes usando SQL
- Compara los tiempos de respuesta
- ¿Notas diferencias significativas?

---

## 🧠 **PREGUNTAS DE REFLEXIÓN**

### **Sobre ORM vs SQL**
1. ¿Cuándo usarías ORM en un proyecto real?
2. ¿Cuándo preferirías SQL puro?
3. ¿Cuál es más fácil de mantener a largo plazo?

### **Sobre FastAPI**
1. ¿Por qué crees que FastAPI genera documentación automática?
2. ¿Qué ventajas tiene el sistema de dependencias?
3. ¿Cómo mejora la validación automática la seguridad?

### **Sobre Arquitectura**
1. ¿Por qué separar modelos, rutas y configuración?
2. ¿Qué ventajas tiene usar variables de entorno?
3. ¿Cómo facilita el testing esta estructura?

---

## 💡 **EXTENSIONES OPCIONALES**

### **🎨 Para los Creativos**
- Cambia el tema de superhéroes por otro (animales, plantas, etc.)
- Modifica los mensajes de respuesta
- Añade más campos a los modelos

### **🔧 Para los Técnicos**
- Añade logging a las operaciones
- Implementa un endpoint de estadísticas
- Crea tests automatizados

### **📊 Para los Analíticos**
- Añade un endpoint de búsqueda por nombre
- Implementa filtros por edad
- Crea un endpoint que devuelva estadísticas

---

## 📋 **Soluciones**

<details>
<summary>🔍 Click para ver las soluciones</summary>

### **Ejercicio 2 - Respuesta esperada**:
```json
{
  "id": 1,
  "name": "Tu Héroe Favorito",
  "age": 25
}
```

### **Ejercicio 6 - Status codes esperados**:
- Héroe inexistente: `404 Not Found`
- Datos inválidos: `422 Unprocessable Entity`
- Éxito: `200 OK` o `201 Created`

### **Ejercicio 8 - Comportamientos esperados**:
- Sin nombre: Error 422 (campo requerido)
- Edad negativa: Depende de validación (puede aceptarse)
- Campo extra: Se ignora automáticamente

</details>

---

**¡Diviértete aprendiendo! 🚀 Recuerda que cada error es una oportunidad de aprender algo nuevo.** 🧠✨
