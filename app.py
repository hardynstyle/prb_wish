from flask import Flask, render_template,send_file
import subprocess
import os
import shutil
app = Flask(__name__)

@app.route('/')
def index():
    message = "Hello, Flask!"
    return render_template('index.html', message=message)

@app.route('/backend', methods=['POST'])
def backend_function():
    # Código para la función del backend
    # Se ejecutará cuando se haga clic en el botón
    # Ejecutar el comando "whisper justin.wav"
    subprocess.run(["whisper", "static/justin.wav"])
    return "Backend function executed"


@app.route('/obtener_ruta_archivo')
def obtener_ruta_archivo():
    ruta_archivo ='static/justin.wav' # Lógica para obtener la ruta del archivo desde el backend
     # Ruta del archivo a mover
    nombre_archivo = os.path.basename(ruta_archivo)
    archivo_origen = nombre_archivo+'.txt'

    # Ruta de la carpeta 'static'
    carpeta_destino = os.path.join(app.root_path, 'static')

    # Mover el archivo a la carpeta destino
    shutil.copy(archivo_origen, carpeta_destino)
    
    return 'static/'+archivo_origen
if __name__ == '__main__':
    app.run()
