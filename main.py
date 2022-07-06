from constants import DELETE_ID, DEPOSIT_ID, FORMAT, RETRIEVE_ID, SIZE
from delete import handle_delete
from deposit import handle_deposit
from retrieve import handle_retrieve
from socket_service import start_satellite


def main():
    print("# Satellite Server is starting #")

    server = start_satellite()

    while True:
        # Server has accepted the connection from the main server
        conn, addr = server.accept()
        print(f"# {addr} connected #")

        # Receiving the operation identifier from the main server
        operation_id = conn.recv(SIZE).decode(FORMAT)
        print(f"# Receiving the operation identifier #")
        conn.send("# Operation identifier received #".encode(FORMAT))

        # Receiving the filename from the main server
        filename = conn.recv(SIZE).decode(FORMAT)
        print(f"# Receiving the filename: {filename} #")
        conn.send("Filename received".encode(FORMAT))

        if operation_id == DEPOSIT_ID:
            handle_deposit(filename, conn)
        elif operation_id == RETRIEVE_ID:
            handle_retrieve(filename, conn)
        elif operation_id == DELETE_ID:
            handle_delete(filename, conn)

        # Closing the connection from the main server
        conn.close()
        print(f"# {addr} disconnected #")
        print("# Satellite Server is listening again #")


if __name__ == "__main__":
    main()
