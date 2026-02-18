import mysql.connector

# En lugar de sys.argv, usamos input para que tú escribas en la terminal
nombre_modulo = input("Pon el nombre del módulo: ")
nota_modulo = input("Añade la nota: ")

# Conexión a la base de datos ASIR [cite: 73]
micon = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ASIR"
)

micursor = micon.cursor()

sql = "INSERT INTO modulos (nombre, nota) VALUES (%s, %s)"
val = (nombre_modulo, nota_modulo)

micursor.execute(sql, val)
micon.commit()

print(micursor.rowcount, "Registro insertado correctamente en la tabla modulos")

micursor.close()
micon.close()