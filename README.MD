# LRU Cache Implementation
Una implementación eficiente de una caché LRU (Least Recently Used) usando una lista doblemente ligada y un diccionario para lograr operaciones en **O(1)**.


## Descripción
Este proyecto implementa una caché LRU que permite almacenar un número limitado de elementos y eliminar automáticamente el **menos recientemente usado** cuando se alcanza la capacidad máxima.  
La implementación utiliza:  
- Una **lista doblemente ligada** para gestionar el orden de acceso.  
- Un **diccionario** para lograr búsqueda rápida en **O(1)**.  
- Pruebas unitarias que validan el comportamiento de la caché.  
- Integración con una **API externa** para demostrar el uso práctico de la caché.  


## Instalación
1. Clona el repositorio:  
```bash
git clone https://github.com/Pipe0001/LRU_Cache
```

2. Navega al directorio del proyecto:  
```bash
cd __pycache__
cd lru_cache
```


## Uso
### 1. Ejecutar la caché manualmente:
```bash
python app.py
```

Salida esperada:
```bash
Agregando A=1
Agregando B=2
Recuperando A: 1
Agregando C=3
Agregando D=4 (debe eliminar B)
Recuperando B: -1
Recuperando C: 3
```


---

## Pruebas
Para ejecutar las pruebas unitarias:  
```bash
python -m unittest lru_test.py
```

**Pruebas incluidas:**  
- Inserción y recuperación de datos (`put` y `get`)  
- Eliminación del valor menos usado  
- Actualización de valores existentes  
- Mejora en el tiempo de respuesta al usar la caché con una API externa  

---

### Operaciones clave
| Método | Descripción | Complejidad |
|--------|-------------|-------------|
| `get(key)` | Recupera el valor y lo mueve al frente (más recientemente usado) | `O(1)` |
| `put(key, value)` | Inserta o actualiza un valor, elimina el menos usado si se alcanza la capacidad máxima | `O(1)` |

### ¿Por qué es eficiente?
- El diccionario permite búsqueda rápida en `O(1)`.  
- La lista doblemente ligada permite reorganización rápida en `O(1)`.  
- El uso combinado de estas dos estructuras garantiza eficiencia constante.  

---

## Ejemplo de Código
```python
from lru_cache import lruCache

# Crear caché con capacidad de 2
cache = lruCache(2)

# Insertar valores
cache.put("A", 1)
cache.put("B", 2)

# Recuperar valores
print(cache.get("A"))  # Output: 1

# Insertar nuevo valor (debería eliminar "B")
cache.put("C", 3)
print(cache.get("B"))  # Output: -1 (eliminado)

# Actualizar valor existente
cache.put("A", 10)
print(cache.get("A"))  # Output: 10
```

---

## Integración con una API
La caché puede usarse para almacenar respuestas de una API y reducir llamadas redundantes:  
```python
from app import fetch_data
from lru_cache import lruCache

cache = lruCache(5)
url = "https://jsonplaceholder.typicode.com/todos/1"

# Primera solicitud → Se obtiene de la API
data = fetch_data(url, cache)

# Segunda solicitud → Se obtiene de la caché
data = fetch_data(url, cache)
```


