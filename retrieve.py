from constants import FORMAT, SIZE


def handle_retrieve(filename, conn):
  print("Start retrieval...")
  try:
    file = open(f"{filename}", "rb")
    data = file.read()

    conn.send("OK".encode(FORMAT))
    msg = conn.recv(SIZE).decode(FORMAT)
    print(f"# Satellite server: {msg} #")

    conn.send(data)
    msg = conn.recv(SIZE).decode(FORMAT)
    print(f"# Satellite server: {msg} #")

  except FileNotFoundError:
        print(f"# Arquivo {filename} não existe no servidor #")
        conn.send("NOT_FOUND".encode(FORMAT))
        msg = conn.recv(SIZE).decode(FORMAT)
        print(f"Satellite server: {msg}")