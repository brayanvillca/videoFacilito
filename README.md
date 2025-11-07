# VideoFacilito

Una herramienta web simple para **descargar videos de YouTube** usando `yt-dlp` y Flask.

---

## Características

- Interfaz limpia y moderna
- Descarga en mejor calidad disponible
- Nombre de archivo: título del video
- Mensaje de éxito o error

---

## Requisitos

- Python 3.7 o superior
- `pip` (gestor de paquetes de Python)

---

## Instalación

### 1. Clona o descarga el proyecto

```bash
git clone https://github.com/tuusuario/videofacilito.git
cd videofacilito
```

## 2. Crea un entorno virtual
### En Windows (CMD)
```cmd
cmdpython -m venv venv
venv\Scripts\activate
```

### En Linux / macOS (Bash)
```bash
bashpython3 -m venv venv
source venv/bin/activate
```


>Verás (venv) al inicio de la línea de comandos → entorno activado.

### 3. Instala las dependencias
``` bash
pip install flask yt-dlp
```
# Ejecutar la aplicación
``` bash
python app.py
```
>Abre en tu navegador: http://127.0.0.1:5000

## Desactivar entorno virtual

```cmd
deactivate
