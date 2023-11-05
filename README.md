# Laboratorio Remoto de Rotobica

Sistema para manejar el acceso de los estudiantes a los laboratorios remotos.

El objetivo de esta aplicacion es permitir a los estudiantes de la FIME el poder acceder a un laboratorio remoto de robotica y realizar de sus practicas.


## Pre requisitos para desarrollar el proyecto

- Python 3.12
- Base de datos MySQL (para produccion) o SQLite (para desarrollo)


## Tecnologías usadas

- Python 3.12
- Django 4.2
- MySQL 


## Iniciar el Proyecto

Antes de iniciar con el setup del proyecto, revisar que las variables de entorno (archivo .env) este bien configurado.

### Configuracion de las variables de entorno

Simplemente hay que cambiar el nombre del archivo `example.env` a `.env`

Dentro del archivo hay que descomentar las lineas y establecer tus configuraciones necesarias para el proyecto y la base de datos.

### Setup del proyecto
```bash

    # Clonamos el proyecto desde el repositorio
    git clone https://github.com/MARCACACAHUATE/project-adb.git    
    
    # Creamos un ambiente virutal para instalar los paquetes
    python -m venv .venv

    # Instalamos los paquetes necesarios
    pip install -r requirement.txt

    # Corremos las migraciones para crear la base de datos.
    # Nota: Debemos tener desplegada la base de datos antes de ejecutar este comando.
    python manage.py migrate

    # Iniciamos el servidor
    python manage.py runserver

```

