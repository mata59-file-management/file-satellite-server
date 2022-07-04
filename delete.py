from constants import FORMAT, SIZE
import os

def handle_delete(filename, conn):
  print("Began deletion...")
  try:
    os.remove(filename)

    conn.send("Deleted".encode(FORMAT))
    msg = conn.recv(SIZE).decode(FORMAT)
    print(f"Main server: {msg}")

  except FileNotFoundError:
    print(f"# Arquivo {filename} não existe no servidor #")
    conn.send("NOT_FOUND".encode(FORMAT))
    msg = conn.recv(SIZE).decode(FORMAT)
    print(f"Main server: {msg}")