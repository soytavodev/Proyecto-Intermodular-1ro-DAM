"""
Script: microservidor.py
Ubicación: Dentro de la carpeta '002-Leer JSON'
Descripción: Servidor Flask que lee el JSON de 'static' y usa 'templates'.
"""

from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route("/")
def inicio():
    # Construimos la ruta segura al archivo JSON
    # Esto busca 'static/curriculum.json' desde donde estamos ejecutando
    ruta_json = os.path.join("static", "curriculum.json")

    try:
        with open(ruta_json, 'r', encoding='utf-8') as f:
            datos = json.load(f)
            
        return render_template("index.html", 
                             nombre=datos['nombre'], 
                             apellidos=datos['apellidos'], 
                             correo=datos['correo'])
                             
    except FileNotFoundError:
        return f"<h1>Error</h1><p>No encuentro el archivo en: {ruta_json}</p>"

if __name__ == "__main__":
    app.run(debug=True)
