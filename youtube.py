
from flask import Flask, render_template, request
import yt_dlp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener la URL del formulario
        url = request.form['url']

        try:
            # Opciones de descarga
            ydl_opts = {
                'outtmpl': '%(title)s.%(ext)s',  # nombre archivo = título del video
                'format': 'best'                 # mejor calidad disponible
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)

            mensaje = f"¡Descarga completa! Video guardado como {filename}"
            return render_template('youtube.html', mensaje=mensaje)

        except Exception as e:
            mensaje = f"Error: {e}"
            return render_template('youtube.html', mensaje=mensaje)

    return render_template('youtube.html')

if __name__ == '__main__':
    app.run(debug=True)