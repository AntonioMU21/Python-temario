import socket

if __name__ == '__main__':

    ip = "10.10.20.4"
    inicio = 20
    final = 100

    with open("puertos.txt", "w", encoding="utf-8") as f:

        print("Escaneando puertos")

        for i in range(inicio, final + 1):

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.2)

            resultado = sock.connect_ex((ip, i))

            if resultado == 0:
                linea = "Puerto " + str(i) + " Abierto\n"
                f.write(linea)

            sock.close()

    print("Proceso terminado")
