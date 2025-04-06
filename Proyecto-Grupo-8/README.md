# Proyecto PPDA - Grupo 8

Descripción General

El Proyecto PPDA (Plan de Prevención y Descontaminación Atmosférica) es una aplicación web desarrollada con Django
 que tiene como objetivo gestionar medidas ambientales destinadas a la descontaminación atmosférica en diversas regiones.
  La plataforma permite la administración de planes, medidas, organismos sectoriales y reportes relacionados con el cumplimiento
   de objetivos ambientales.

Características Principales

    1. Gestión de Planes de Descontaminación:

        -   Registro y administración de planes ambientales.

        -   Asociación de medidas específicas a cada plan.

    2. Gestión de Medidas Ambientales:

        -   Registro y seguimiento de medidas implementadas por organismos sectoriales.

        -   Monitoreo del estado de las medidas (pendiente, en progreso, completado).

    3. Reportes:

        -   Generación y visualización de reportes técnicos sobre el avance de las medidas.

        -   Trazabilidad mediante registros históricos.

    4. Autenticación y Roles:

        -   Sistema de autenticación basado en JWT (JSON Web Tokens).

        -   Roles definidos para usuarios: Administrador del sistema, funcionario sectorial, analista SMA, entre otros.

    5. Documentación API:

        -   Documentación interactiva Swagger disponible en /api/docs/.

Estructura del Proyecto

    El proyecto está dividido en tres aplicaciones principales:

        -   Authentication: Gestión de usuarios y roles.

        -   Core: Administración de planes, medidas y reportes.

        -   PPDA: Configuración central del proyecto.

    Tecnologías Utilizadas
        -    Backend: Django, Django REST Framework.

        -    Base de Datos: SQLite (con opción para PostgreSQL).

    Dependencias Adicionales:

        -    Pandas y OpenPyxl para procesamiento de datos.

        -    DRF Spectacular para documentación API.

        -    SimpleJWT para autenticación.


## Instalacion del Proyecto


    1.-  Clonar el proyecto desde el repositorio de GitHub: 

    2 .- Instalar las dependencias del proyecto: 
                pip install pipenv
                pipenv install
    
    3.-  Crear un archivo .env con la siguiente estructura:
                pipenv shell

    4 .- Aplicar las migraciones de la base de datos:
                python manage.py makemigrations
                python manage.py migrate
    
    5 .- Cargar datos iniciales (fixture):
                python manage.py load_initial_data



## Endpoints Principales

    Autenticación:

        POST /api/authentication/login/: Iniciar sesión.

        POST /api/authentication/logout/: Cerrar sesión.

    Gestión de Planes:

        GET /api/plan_descontaminacion/: Listar planes.

        POST /api/plan_descontaminacion/: Crear un nuevo plan.

    Gestión de Medidas:

        GET /api/medida/: Listar medidas.

        POST /api/medida/: Crear una nueva medida.

    Reportes:

        GET /api/registro_medida/: Listar registros asociados a las medidas.

        La documentación completa está disponible en /api/docs/.