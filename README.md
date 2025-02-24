# ADRES Prueba Técnica: Carga y validacion de archivo TXT con Framework DJANGO

## Por: JUAN CARLOS CASTILLO G.

Este es un proyecto Django desarrollado como parte de una prueba técnica. La aplicación permite cargar un archivo `.txt` con datos separados por comas y realiza validaciones sobre los datos. Realice tambien TESTs de calidad.

![Logo del proyecto](https://iili.io/3JHevfI.md.png)

## Características

- Carga de archivos `.txt`.
- Validaciones personalizadas:
  - El archivo debe tener exactamente 5 columnas.
  - Columna 1: Solo números enteros entre 3 y 10 caracteres.
  - Columna 2: Solo correos electrónicos válidos.
  - Columna 3: Solo permite los valores "CC" o "TI".
  - Columna 4: Solo permite valores entre 500000 y 1500000.
  - Columna 5: Permite cualquier valor.
- Interfaz de usuario con Bootstrap.
- Pruebas automatizadas para validar la lógica de la aplicación.

## Requisitos

- Python 3.8 o superior.
- Django 4.2 o superior.

## Instalación

Configurar y ejecutar el proyecto en entorno local.

### 1. Clonar el repositorio

```bash
git clone https://github.com/juanchistosomk/adres-p1-django.git
cd prueba-tecnica-django
```

### 2. Comandos crear entorno virtual python:

```bash
python -m venv env
```

```bash
.\env\Scripts\activate
```

### 3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

### 4. Ejecutar el proyecto:

```bash
python manage.py runserver
```

### 5. Abrir URL:

http://localhost:8000

### 6. Ejecutar Tests:

```bash
python manage.py test file_uploader
```
