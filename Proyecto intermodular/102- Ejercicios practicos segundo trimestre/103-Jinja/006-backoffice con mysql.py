from flask import Flask, render_template
import mysql.connector
############################# MYSQL #################################################
conexion = mysql.connector.connect(
host="localhost",user="gustavo",password="Hakaishin2.",database="portafolioexamen"
)									#datos de conexion a la base de datos
cursor = conexion.cursor()			#creo un cursor mysql
cursor.execute("SHOW TABLES;")		#muestra las tablas de la base de datos
tablas = []							#creo una lista vacia
filas = cursor.fetchall()			#lo guardo en una lista
for fila in filas:					#recorro el resultado
	tablas.append(fila[0])			#lo añado a la lista de tablas
############################### MYSQL ################################################
	
app = Flask(__name__)

@app.route("/")
def inicio():
	return render_template("backoffice.html")
	
if __name__ == "__main__":
	app.run(debug=True)
