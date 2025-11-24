'''
Mi blog

Autor: Gustavo Delnardo

En este ejercicio crearemos un servidor web con Flask que muestra contenido dinámico extraído de un archivo JSON. Leeremos datos desde Python y generaremos HTML de manera programática. Esto simula el funcionamiento básico de un blog real.
'''

from flask import Flask
import json

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    cadena = '''
    <!doctype html>
    <html lang="es">
      <head>
        <title>TavBlog</title>
        <meta charset="utf-8">
        <style>
          body {background: steelblue; color: steelblue; font-family: sans-serif;}
          header, main, footer {background: white; padding: 20px; margin: auto; width: 600px;}
          header, footer {text-align: center;}
          main {color: black;}
        </style>
      </head>
      <body>
        <header><h1>TavBlog</h1></header>
        <main>
    '''
    with open("blog.json", 'r', encoding='utf-8') as archivo:
        contenido = json.load(archivo)
    for linea in contenido:
        cadena += f'''
        <article>
          <h3>{linea['titulo']}</h3>
          <time>{linea['fecha']}</time>
          <p>Autor: {linea['autor']}</p>
          <p>{linea['contenido']}</p>
        </article>
        '''
    cadena += '''
        </main>
        <footer>(c)2025 Gustavo Delnardo</footer>
      </body>
    </html>
    '''
    return cadena

if __name__ == "__main__":
    aplicacion.run(debug=True)

#El ejercicio permitió comprender la integración de Flask con archivos JSON para mostrar contenido dinámico. Practicamos la generación de HTML desde Python y la estructura de un servidor web básico. Sentó las bases para desarrollar aplicaciones web más completas.

