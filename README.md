# Google Drive File Renamer

Este script de Python utiliza la API de Google Drive para renombrar archivos en una carpeta específica que comienzan con un patrón dado.

## Requisitos previos

Antes de ejecutar este script, asegúrate de tener instalado Python en tu sistema.

Clona este repositorio en tu máquina local:

```bash
   git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
```

Se recomienda crear un virtualenv para instalar las dependencias necesarias

```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
```

Luego, instalar las dependencias con

```bash
pip install -r requirements.txt
```

Además, necesitarás crear un proyecto en la [Consola de Desarrolladores de Google](https://console.developers.google.com/) y habilitar la API de Google Drive. Luego, descarga el archivo `credentials.json` de OAuth 2.0 de tu proyecto, para luego colocarlo en la carpeta `env\Include\` en el directorio de tu proyecto.

## Uso

- Ejecuta el script G_Drive_File_Renamer.py desde la terminal en el directorio donde se encuentra

```bash
python G_Drive_File_Renamer.py
```

- Sigue las instrucciones en pantalla para autenticarte con tu cuenta de Google y proporcionar el ID de la carpeta de destino y el patrón de los archivos que deseas renombrar.
- El script buscará los archivos que coincidan con el patrón dado en la carpeta especificada y los renombrará.
- Una vez que el proceso haya terminado, el script mostrará el número total de archivos encontrados en la carpeta, el número de archivos que coinciden con el patrón y el número de archivos que se han renombrado correctamente.
