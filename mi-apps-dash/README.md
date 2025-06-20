# Proyecto de Aplicación Dash

Este proyecto es una aplicación web construida con Dash, un framework de Python para crear aplicaciones analíticas. A continuación se describen los archivos y su propósito.

## Estructura del Proyecto

```
mi-app-dash
├── src
│   ├── app.py
│   └── components
│       └── __init__.py
├── .devcontainer
│   ├── devcontainer.json
│   └── Dockerfile
├── requirements.txt
└── README.md
```

## Descripción de Archivos

- **src/app.py**: Este es el punto de entrada de la aplicación Dash. Contiene la lógica principal para inicializar la aplicación y definir los componentes de la interfaz de usuario.

- **src/components/__init__.py**: Este archivo se utiliza para definir componentes adicionales de la aplicación Dash. Puede contener funciones o clases que se utilizan en `app.py`.

- **.devcontainer/devcontainer.json**: Este archivo configura el entorno de desarrollo en contenedores. Especifica el nombre del contenedor, el archivo Docker, los puertos de la aplicación y las extensiones de VS Code que se deben instalar.

- **.devcontainer/Dockerfile**: Este archivo se utiliza para definir la imagen del contenedor que ejecutará la aplicación Dash.

- **requirements.txt**: Este archivo lista las dependencias de Python necesarias para la aplicación, incluyendo Dash y cualquier otra biblioteca que se requiera.

## Instrucciones para Ejecutar la Aplicación

1. Asegúrate de tener Docker instalado en tu máquina.
2. Abre el proyecto en un entorno de desarrollo compatible con contenedores.
3. Ejecuta el contenedor utilizando el archivo de configuración `.devcontainer/devcontainer.json`.
4. Accede a la aplicación en tu navegador en `http://localhost:8050`.

## Dependencias

Asegúrate de que el archivo `requirements.txt` contenga las siguientes dependencias:

```
dash
```

Agrega cualquier otra biblioteca que necesites para tu aplicación.