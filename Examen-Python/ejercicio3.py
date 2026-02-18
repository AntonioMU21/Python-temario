import sys
import mysql.connector

if __name__ == "__main__":

    nombre = sys.argv[1]
    nota = sys.argv[2]

    micon = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ASIR"
    )

    micursor = micon.cursor()

    sql = "INSERT INTO modulos(nombre,nota) VALUES (%s, %s)"
    val = (nombre, nota)

    micursor.execute(sql, val)
    micon.commit()

    print(micursor.rowcount, "Registro Insertado")

    micursor.close()
    micon.close()
