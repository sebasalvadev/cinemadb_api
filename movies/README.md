# CinemaDB API

API REST para la gestión de películas y directores desarrollada con Django y Django REST Framework.

## Descripción del Proyecto

Sistema de gestión que permite administrar un catálogo de películas y sus directores mediante una API REST completa. Implementa operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para ambas entidades, con búsquedas avanzadas y relaciones entre modelos.

**Características principales:**
- Gestión completa de películas (título, género, año de estreno, director)
- Gestión completa de directores (nombre, nacionalidad)
- Relación entre películas y directores
- Búsqueda por título y género
- Respuestas personalizadas con información relacionada

## Tecnologías Usadas

- **Python 3.10+**
- **Django 4.2**
- **Django REST Framework 3.14**
- **django-filter 23.2**
- **SQLite**

## Instrucciones para Ejecutar el Servidor

### 1. Clonar el repositorio
```bash
git clone https://github.com/TU-USUARIO/cinemadb_api.git
cd cinemadb_api
```

### 2. Crear y activar entorno virtual
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Realizar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Poblar base de datos con datos de ejemplo
```bash
python manage.py populate_db
```

### 6. Ejecutar el servidor
```bash
python manage.py runserver
```

El servidor estará disponible en: **http://127.0.0.1:8000/**

## Endpoints Disponibles con Ejemplos de Uso

### Películas

#### GET `/api/peliculas/`
```bash
curl http://127.0.0.1:8000/api/peliculas/
```

#### POST `/api/peliculas/`
```bash
curl -X POST http://127.0.0.1:8000/api/peliculas/ \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Interstellar",
    "genero": "ciencia_ficcion",
    "anio_estreno": 2014,
    "director": 1,
    "duracion_minutos": 169
  }'
```

#### PUT `/api/peliculas/{id}/`
```bash
curl -X PUT http://127.0.0.1:8000/api/peliculas/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Inception - Director Cut",
    "genero": "ciencia_ficcion",
    "anio_estreno": 2010,
    "director": 1,
    "duracion_minutos": 160
  }'
```

#### PATCH `/api/peliculas/{id}/`
```bash
curl -X PATCH http://127.0.0.1:8000/api/peliculas/1/ \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Inception - ACTUALIZADO"}'
```

#### DELETE `/api/peliculas/{id}/`
```bash
curl -X DELETE http://127.0.0.1:8000/api/peliculas/1/
```

#### GET `/api/peliculas/?search=`
```bash
curl http://127.0.0.1:8000/api/peliculas/?search=inception
curl http://127.0.0.1:8000/api/peliculas/?search=drama
```

### Directores

#### GET `/api/directores/`
```bash
curl http://127.0.0.1:8000/api/directores/
```

#### POST `/api/directores/`
```bash
curl -X POST http://127.0.0.1:8000/api/directores/ \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Pedro Almodóvar",
    "nacionalidad": "Español",
    "fecha_nacimiento": "1949-09-25"
  }'
```

#### PATCH `/api/directores/{id}/`
```bash
curl -X PATCH http://127.0.0.1:8000/api/directores/1/ \
  -H "Content-Type: application/json" \
  -d '{"nacionalidad": "Británico-Estadounidense"}'
```

#### DELETE `/api/directores/{id}/`
```bash
curl -X DELETE http://127.0.0.1:8000/api/directores/1/
```

#### GET `/api/directores/{id}/peliculas/`
```bash
curl http://127.0.0.1:8000/api/directores/1/peliculas/
```