import socket

# Definimos la base de la IP y el rango de hosts (del 4 al 100)
red = "10.10.20."
puerto = 80 # Usamos el puerto 80 como en tus apuntes de clase

print("Escaneando hosts desde el 20.4 al 20.100...")

# Abrimos el fichero puertos.txt (estilo OPCION 2)
with open("puertos.txt", "w", encoding="utf-8") as f:
    for i in range(4, 101):
        ip = red + str(i)

        # Configuracion del socket (estilo ESCANEAR HOSTS de tus apuntes)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.2)

        resultado = sock.connect_ex((ip, puerto))

        # Si el resultado es 0, el host tiene ese puerto abierto
        if resultado == 0:
            linea = f"El host {ip} tiene el puerto {puerto} abierto\n"
            f.write(linea)
            print(f"Host encontrado: {ip}")

        sock.close()

print("Escaneo finalizado y guardado en puertos.txt")