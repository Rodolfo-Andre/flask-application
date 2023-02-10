# Aplicación Flask

## Pasos para ejecutar la aplicación flask

1. Crear el entorno virtual que nos servirá para almacenar las librerías necesarias para la aplicación:

```shell
virtualenv env
```

2. Activar el entorno virtual:

```shell
env\Scripts\activate
```

3. Instalar los paquetes que utiliza la aplicación. Para ello contamos con el archivo requirements.txt la cual tiene todos los nombres y versiones de los paquetes que necesitamos. Ejecutamos lo siguiente:

```shell
pip install -r requirements.txt
```

4. Crear el archivo ".env". Una vez creado establecemos las siguientes variables de entorno:

```python
SECRET_KEY=my_secret_key
SQLALCHEMY_DATABASE_URI=mysql://root:root@localhost/app
SQLALCHEMY_TRACK_MODIFICATIONS=False
API_TITLE=Pet API
API_VERSION=v 0.0.1
OPENAPI_VERSION=3.0.2
OPENAPI_URL_PREFIX=/
OPENAPI_REDOC_PATH=/redoc
OPENAPI_REDOC_URL=https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js
OPENAPI_SWAGGER_UI_PATH=/swagger-ui
OPENAPI_SWAGGER_UI_URL=https://cdn.jsdelivr.net/npm/swagger-ui-dist/
OPENAPI_RAPIDOC_PATH=/rapidoc
OPENAPI_RAPIDOC_URL=https://unpkg.com/rapidoc/dist/rapidoc-min.js
```

5. Ejecutamos las migraciones para crear las tablas en la base de datos:

```shell
flask db init
flask db migrate -m "Mensaje de ejemplo"
flask db upgrade
```

6. Ejecutamos la aplicación flask:

- Primera forma:

```shell
flask run
```

- Segunda forma:

```shell
python main.py
```
