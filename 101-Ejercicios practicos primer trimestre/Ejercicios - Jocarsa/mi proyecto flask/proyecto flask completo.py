"""
flask Completo

Autor: Gustavo Delnardo

Aplicación básica de Flask que muestra HTML dinámico.
Genera un título rojo y una lista de los días del mes (1-30) de forma dinámica.
"""

from flask import Flask

# Crear la aplicación Flask
aplicacion = Flask(__name__)

# Ruta principal
@aplicacion.route("/")
def raiz():
    # Comenzamos la cadena HTML
    cadena = '''
    <!doctype html>
    <html>
      <head>
        <title>Mi Proyecto Flask</title>
        <style>
          body { font-family: Arial, sans-serif; margin: 20px; }
          h1 { color: red; }
          div { margin: 2px 0; }
        </style>
      </head>
      <body>
        <h1>Esto es HTML a tope de power</h1>
        <p>Lista de días del mes generada dinámicamente:</p>
    '''

    # Generar lista dinámica de días
    for dia in range(1, 31):
        cadena += f'<div>Día {dia}</div>'

    # Cerrar la etiqueta HTML
    cadena += '''
      </body>
    </html>
    '''
    return cadena

# Ejecutar la aplicación
if __name__ == "__main__":
    aplicacion.run(debug=True)
    
#En este ejercicio hemos aprendido a integrar Python con Flask para generar páginas web dinámicas utilizando HTML. Hemos realizado los siguientes puntos clave:

#Instalación y configuración de Flask: comprendimos cómo usar un entorno virtual (venv) para manejar dependencias y ejecutar aplicaciones web sin afectar el sistema.

#Servidor web básico: creamos un servidor Flask que responde a solicitudes HTTP en la ruta principal (/).

#HTML dinámico: aprendimos a generar contenido HTML desde Python de manera programática, en este caso una lista de días del mes, demostrando cómo el servidor puede producir contenido que cambia según la lógica de Python.

#Estilos CSS básicos: incorporamos estilos simples para dar formato a los elementos HTML, como el título rojo y los div de los días, mostrando la interacción entre Flask, HTML y CSS.

#Aprendizaje principal: este ejercicio demuestra cómo Python puede controlar completamente el contenido que se muestra en un navegador, formando la base para aplicaciones web más complejas, como blogs, portafolios o sistemas CRUD completos integrados con bases de datos.


