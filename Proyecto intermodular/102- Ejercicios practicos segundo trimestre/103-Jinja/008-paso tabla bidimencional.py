from flask import Flask, render_template
import mysql.connector
############################# MYSQL #################################################
conexion = mysql.connector.connect(
host="localhost",user="yosoytavo",password="Hakaishin2.",database="portafolio")
cursor = conexion.cursor()			#creo un cursor mysql
#-----------------------ESTO ENVIA LAS TABLAS-------------------------------------#
cursor.execute("SHOW TABLES;")		#muestra las tablas de la base de datos
tablas = []							#creo una lista vacia
filas = cursor.fetchall()			#lo guardo en una lista
for fila in filas:					#recorro el resultado
	tablas.append(fila[0])			#lo añado a la lista de tablas
#----------------- ESTO ENVIA LAS CABECERAS DE LA TABLA-----------------------------#
cursor.execute("SHOW COLUMNS in pieza;")		#muestra las tablas de la base de datos
columnas = []									#creo una lista vacia
filas = cursor.fetchall()						#lo guardo en una lista
for fila in filas:								#recorro el resultado
	columnas.append(fila[0])					#lo añado a la lista de tablas
	#----------------- ESTO ENVIA LAS CABECERAS DE LA TABLA-----------------------------#
cursor.execute("SELECT * FROM pieza;")		#muestra las tablas de la base de datos
contenido_tabla = cursor.fetchall()						#lo guardo en una lista
############################### MYSQL ################################################
	
app = Flask(__name__)

@app.route("/")
def inicio():
	return render_template(
	"backoffice.html",
	mis_tablas = tablas,
	mis_columnas = columnas,
	mi_contenido_tabla = contenido_tabla
	)
	
if __name__ == "__main__":
	app.run(debug=True)
