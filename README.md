# CinemaDB API

API REST para la gestión y consulta de un catálogo de películas, construida con Python, Django y Django REST Framework.

## Descripción

Este proyecto implementa una arquitectura backend para registrar, listar y consultar información sobre películas. Incluye un comando personalizado (`populate_db`) para automatizar la carga inicial de datos en la base de datos relacional SQLite, facilitando las pruebas y la manipulación de registros.

## Tecnologías

- **Lenguaje:** Python
- **Framework Web:** Django / Django REST Framework
- **Base de datos:** SQLite 3

## Estructura del proyecto

- `cinemadb_api/`: Configuración principal del proyecto Django (settings, urls, wsgi).
- `movies/`: App donde se gestionan los modelos, serializadores, vistas y el comando personalizado `populate_db`.
- `db.sqlite3`: Base de datos local.
- `requirements.txt`: Lista de dependencias del entorno.

## Instalación y uso local

1. Clonar el repositorio:
```bash
git clone [https://github.com/sebasalvadev/cinemadb_api.git](https://github.com/sebasalvadev/cinemadb_api.git)
cd cinemadb_api
