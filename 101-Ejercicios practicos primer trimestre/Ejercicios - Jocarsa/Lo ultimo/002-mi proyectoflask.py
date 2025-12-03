'''
Portafolio Flask v1.0

Autor: Gustavo Delnardo

Aplicación web desarrollada con Flask que se conecta a una base de datos MySQL.
Recupera los datos desde una vista (vista_piezasportafolio_categoriasportafolio)
y los muestra dinámicamente en una página HTML, utilizando estructura tipo MVC.
'''

from flask import Flask
import mysql.connector

# ---------------------------------------------------------
# CONEXIÓN A LA BASE DE DATOS
# ---------------------------------------------------------
try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="gustavo",              # Usuario MySQL creado anteriormente
        password="Hakaishin2.",      # Contraseña del usuario
        database="portafolioexamen"  # Nombre de la base de datos
    )
    cursor = conexion.cursor(dictionary=True)  # Para obtener resultados con nombres de columna
    print("Conexión exitosa a la base de datos")
except mysql.connector.Error as err:
    print("Error al conectar con la base de datos:", err)
    exit()

# ---------------------------------------------------------
# APLICACIÓN FLASK
# ---------------------------------------------------------
aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    '''
    Ruta principal del servidor Flask.
    Obtiene los datos de la vista MySQL y genera contenido HTML dinámico.
    '''

    #Consultamos la vista creada en MySQL
    cursor.execute("SELECT * FROM vista_piezasportafolio_categoriasportafolio;")
    resultados = cursor.fetchall()

    #Iniciamos la estructura básica HTML
    html = '''
    <!doctype html>
    <html lang="es">
      <head>
        <meta charset="utf-8">
        <title>Portafolio artístico</title>
        <style>
          body { background: #f0f0f0; font-family: Arial, sans-serif; color: #333; }
          header, footer { background: #1b4965; color: white; text-align: center; padding: 20px; }
          main { background: white; width: 70%; margin: 20px auto; padding: 20px; border-radius: 10px; }
          article { border-bottom: 1px solid #ccc; margin-bottom: 20px; padding-bottom: 10px; }
          h2 { color: #1b4965; }
          .categoria { font-style: italic; color: #777; }
        </style>
      </head>
      <body>
        <header><h1>Portafolio de Arte</h1></header>
        <main>
    '''

    #Recorremos los registros y generamos los artículos dinámicos
    for fila in resultados:
        html += f'''
        <article>
          <h2>{fila['piezasportafolio']}</h2>
          <p class="categoria">{fila['categoriasportafolio']}</p>
          <p>{fila['descripcion_piezasportafolio']}</p>
          <p><strong>Fecha:</strong> {fila.get('fecha_piezasportafolio', 'Sin fecha')}</p>
        </article>
        '''

    #Pie de página estático
    html += '''
        </main>
        <footer>© 2025 Gustavo Delnardo | Proyecto de integración Flask + MySQL</footer>
      </body>
    </html>
    '''

    return html


# ---------------------------------------------------------
# EJECUCIÓN PRINCIPAL
# ---------------------------------------------------------
if __name__ == "__main__":
    aplicacion.run(debug=True)

#En este ejercicio hemos aprendido a integrar Python con Flask para generar páginas web dinámicas utilizando HTML. Hemos realizado los siguientes puntos clave:

#Servidor web básico: creamos un servidor Flask que responde a solicitudes HTTP en la ruta principal (/).

#HTML dinámico: aprendimos a generar contenido HTML desde Python de manera programática.

#Estilos CSS básicos: incorporamos estilos simples para dar formato a los elementos HTML.

#Y demostramos cómo Python puede controlar completamente el contenido que se muestra en un navegador, formando la base para aplicaciones web más complejas, como blogs, portafolios o sistemas CRUD completos integrados con bases de datos.
