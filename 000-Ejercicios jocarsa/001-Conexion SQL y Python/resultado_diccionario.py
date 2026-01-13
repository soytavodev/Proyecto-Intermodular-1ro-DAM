"""
Nombre: resultado_diccionario.py
Descripción: Consulta a MySQL obteniendo resultados como diccionario.
Asignatura: Proyecto Intermodular - 1º DAM
"""

import mysql.connector

try:
    # Conexión
    conexion = mysql.connector.connect(
        host="localhost",
        user="Gustavo",
        password="Hakaishin2.",
        database="clientes"
    )

    if conexion.is_connected():
        # IMPORTANTE: dictionary=True devuelve diccionarios en vez de tuplas
        cursor = conexion.cursor(dictionary=True)

        sql = '''
          SELECT nombre AS "Nombre del cliente", 
                 apellidos AS "Apellidos del cliente", 
                 edad AS "Edad del cliente"
          FROM clientes ORDER BY edad DESC;
        '''
        
        cursor.execute(sql)
        filas = cursor.fetchall()
        
        # Imprimimos la lista de diccionarios resultante
        print("Resultados recuperados:")
        print(filas)

except mysql.connector.Error as e:
    print(f"Error al conectar o consultar: {e}")

finally:
    # Cerramos recursos si se llegaron a abrir
    if 'conexion' in locals() and conexion.is_connected():
        cursor.close()
        conexion.close()
        print("Conexión cerrada.")

#En este script hemos conectado Python con la base de datos clientes para mostrar información. Lo más destacado del código es:

#Resultados como Diccionarios: Al poner cursor(dictionary=True), las filas de la base de datos se convierten en diccionarios de Python en lugar de tuplas. Esto es muy útil porque podemos ver el nombre del campo junto al dato (ej. 'Edad': 25) en lugar de solo ver números y textos sueltos.

#Nombres personalizados: En la sentencia SQL hemos usado AS (alias) para cambiar el nombre de las columnas. Así, las claves del diccionario salen limpias y legibles (ej. "Nombre del cliente") directamente desde la consulta.

#Buenas prácticas: Todo el código está dentro de un bloque try-except-finally. Esto sirve para que, si falla la conexión, el programa nos avise del error y, pase lo que pase, cierre siempre la conexión al terminar para no dejarla abierta.
