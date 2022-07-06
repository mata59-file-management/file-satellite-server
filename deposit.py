from constants import FORMAT, SIZE


def handle_deposit(filename, conn):
  print("# Start deposit... #")

  file = open(filename, "wb")
  conn.send("# Filename received #".encode(FORMAT))

  # Receiving the file data from the main server. 
  data = conn.recv(SIZE)
  print(f"# Receiving the file data #")
  file.write(data)
  conn.send("# File data received #".encode(FORMAT))

  # Closing the file
  file.close()