import socket


IP = socket.gethostbyname(socket.gethostname())

SIZE = 262144 # 72 Kbs
FORMAT = "utf-8"
# FORMAT = "mbcs"

START_PORT = 4456
MAX_SATELLITE_INSTANCES = 5

DEPOSIT_ID = "deposit"
RETRIEVE_ID = "retrieve"