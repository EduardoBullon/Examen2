# Videojuego Catalogo API

Este proyecto es una API REST construida con Django y Django REST Framework para gestionar un catálogo de videojuegos. Permite a los usuarios acceder a información sobre juegos, desarrolladores, plataformas y géneros de manera eficiente.

## Descripción

La API proporciona funcionalidades para consultar, crear, actualizar y eliminar información relacionada con videojuegos. Utiliza filtros avanzados para buscar juegos por nombre y permite la gestión de diferentes tipos de objetos (como desarrolladores, plataformas y géneros) a través de un sistema robusto basado en Django y Django REST Framework.

## Características

- Gestión de videojuegos, desarrolladores, plataformas y géneros.
- Filtros avanzados para búsqueda de juegos.
- CRUD (Crear, Leer, Actualizar, Eliminar) para cada modelo.
- Documentación detallada de la API para facilitar el uso.

## Tecnologías

- **Django** - Framework web para el desarrollo del backend.
- **Django REST Framework** - Para construir la API RESTful.
- **django-filter** - Para aplicar filtros personalizados en las consultas.
- **PostgreSQL** - Base de datos (opcional, puedes usar SQLite en desarrollo).
- **Python** - Lenguaje de programación.

## Requisitos

1. Python 3.8+.
2. Django 5.2+.
3. Django REST Framework.
4. django-filter.
5. PostgreSQL (opcional, si no se usa SQLite).

## Instalación

1. Clona el repositorio en tu máquina local:

    ```bash
    git clone https://github.com/tu-usuario/videojuego-catalogo.git
    cd videojuego-catalogo
    ```

2. Crea un entorno virtual e instálalo:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa: venv\Scripts\activate
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Realiza las migraciones para configurar la base de datos:

    ```bash
    python manage.py migrate
    ```

5. Crea un superusuario para acceder al panel de administración (opcional):

    ```bash
    python manage.py createsuperuser
    ```

6. Corre el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

7. Accede a la API en:

    ```
    http://127.0.0.1:8000/api/
    ```

    Y al panel de administración en:

    ```
    http://127.0.0.1:8000/admin/
    ```

## Endpoints

### Videojuegos
- `GET /api/juegos/` - Listar todos los videojuegos.
- `POST /api/juegos/` - Crear un nuevo videojuego.
- `GET /api/juegos/{id}/` - Obtener detalles de un videojuego por su ID.
- `PUT /api/juegos/{id}/` - Actualizar un videojuego por su ID.
- `DELETE /api/juegos/{id}/` - Eliminar un videojuego por su ID.

### Desarrolladores
- `GET /api/desarrolladores/` - Listar todos los desarrolladores.
- `POST /api/desarrolladores/` - Crear un nuevo desarrollador.
- `GET /api/desarrolladores/{id}/` - Obtener detalles de un desarrollador.
- `PUT /api/desarrolladores/{id}/` - Actualizar un desarrollador.
- `DELETE /api/desarrolladores/{id}/` - Eliminar un desarrollador.

### Plataformas
- `GET /api/plataformas/` - Listar todas las plataformas.
- `POST /api/plataformas/` - Crear una nueva plataforma.
- `GET /api/plataformas/{id}/` - Obtener detalles de una plataforma.
- `PUT /api/plataformas/{id}/` - Actualizar una plataforma.
- `DELETE /api/plataformas/{id}/` - Eliminar una plataforma.

### Géneros
- `GET /api/generos/` - Listar todos los géneros.
- `POST /api/generos/` - Crear un nuevo género.
- `GET /api/generos/{id}/` - Obtener detalles de un género.
- `PUT /api/generos/{id}/` - Actualizar un género.
- `DELETE /api/generos/{id}/` - Eliminar un género.

