import socket

from constants import IP, MAX_SATELLITE_INSTANCES, START_PORT


def start_satellite():
  """ Staring a TCP socket. """
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  current_port = START_PORT

  """ Bind the IP and closest available port number to the server. """
  while current_port < (START_PORT + MAX_SATELLITE_INSTANCES):
      try:
          ADDRESS = (IP, current_port)
          server.bind(ADDRESS)
          break
      except Exception:
          print("Porta em uso:", current_port)
          print("Procurando proxima porta disponível...")
          current_port = current_port+1

  print("[*] Porta selecionada: ", current_port)

  """ Satellite server is listening, i.e., satellite server is now waiting for the main server to connected. """
  server.listen()
  print("[LISTENING] Satellite Server is listening.")
  
  return server