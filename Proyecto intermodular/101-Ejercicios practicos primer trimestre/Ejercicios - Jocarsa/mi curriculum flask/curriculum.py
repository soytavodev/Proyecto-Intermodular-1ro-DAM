'''
mi curriculum v0.1

Gustavo Delnardo

En este ejercicio implementamos el patrón MVC usando Flask, separando los datos (JSON), la lógica (Python) y la presentación (HTML). Esto nos permite actualizar el curriculum fácilmente sin modificar el código.
'''

from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def mostrar_curriculum():
    with open("curriculum.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    return render_template("curriculum.html", **datos)

if __name__ == "__main__":
    app.run(debug=True)


#El ejercicio demuestra cómo Flask puede leer datos de un modelo JSON y renderizarlos dinámicamente en una vista HTML. Se entiende la ventaja de separar datos, lógica y presentación para mantener el código organizado y escalable.
