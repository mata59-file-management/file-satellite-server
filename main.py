
import socket

IP = socket.gethostbyname(socket.gethostname())

SIZE = 1024
FORMAT = "utf-8"


def main():
    print("[STARTING] Satellite Server is starting.")
    """ Staring a TCP socket. """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 4456

    """ Bind the IP and closest available port number to the server. """
    while port < 4466:
        try:
            ADDRESS = (IP, port)
            server.bind(ADDRESS)
            break
        except Exception:
            print("Porta em uso:", port)
            print("Procurando proxima porta disponível...")
            port = port+1

    print("[*] Porta selecionada: ", port)

    """ Server is listening, i.e., server is now waiting for the client to connected. """
    server.listen()
    print("[LISTENING] Satellite Server is listening.")

    while True:
        """ Server has accepted the connection from the client. """
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")

        """ Receiving the filename from the client. """
        filename = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the filename: {filename}")

        if filename:
            file = open(filename, "w")
            conn.send("Filename received.".encode(FORMAT))

            """ Receiving the file data from the client. """
            data = conn.recv(SIZE).decode(FORMAT)
            print(f"[RECV] Receiving the file data.")
            file.write(data)
            conn.send("File data received".encode(FORMAT))

            """ Closing the file. """
            file.close()

        else:
            print("Arquivo inválido enviado pelo servidor!")

        """ Closing the connection from the client. """
        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")
        print("[LISTENING] Satellite Server is listening again.")


if __name__ == "__main__":
    main()
