# Bot de Scraping de Empleos

Este proyecto es un bot que realiza scraping de sitios web de empleos como [Bumeran](https://www.bumeran.com.pe), [LinkedIn](https://www.linkedin.com), [Indeed](https://www.indeed.com), entre otros, para enviar los resultados a canales de texto en plataformas como Discord o Telegram.

## Características

- Scrapea múltiples sitios web de empleos.
- Envía los empleos encontrados a Discord o Telegram.
- Configurable para añadir más plataformas o tipos de empleos.

## Requisitos

Asegúrate de tener instalado lo siguiente antes de comenzar:

- Python 3.12.x 
- Git

## Instalación

### 1. Clonar el repositorio

Primero, clona este repositorio en tu máquina local:

```bash
git clone https://github.com/tu-usuario/bot-empleos.git
cd bot-empleos```

### 2. Crear un entorno virtual

Es recomendable crear un entorno virtual para manejar las dependencias del proyecto sin interferir con otros proyectos en tu sistema.

- En **Windows**:

```bash
python -m venv env
.\env\Scripts\activate```

- En **macOS\Linux**:
```bash
python3 -m venv env
source env/bin/activate```

### 3. Instalar las dependencias

Con el entorno virtual activado, instala las dependencias del proyecto utilizando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt```

### Explicación:

- **`pip install -r requirements.txt`**: Instala todas las dependencias listadas en `requirements.txt`.
- **`pip install <nueva-dependencia>`**: Instala una nueva dependencia específica (reemplaza `<nueva-dependencia>` con el nombre de la biblioteca).
- **`pip freeze > requirements.txt`**: Actualiza el archivo `requirements.txt` con las versiones exactas de todas las bibliotecas instaladas en el entorno virtual.

Este fragmento asegura que cualquier usuario pueda configurar las dependencias necesarias para ejecutar el proyecto correctamente.
