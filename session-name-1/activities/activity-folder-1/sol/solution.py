import sys
import requests

PORT = 8001

if len(sys.argv) == 1:
    print(f"Usage: {sys.argv[0]} [local|remote]\nor")
    print(f"Usage: {sys.argv[0]} <ip> <port>")
    exit(1)

if len(sys.argv) > 1 and sys.argv[1] == "local":
    HOST = "127.0.0.1"
elif len(sys.argv) > 1 and sys.argv[1] == "remote":
    HOST = "141.85.224.103"
else:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])

res = requests.get(f"http://{HOST}:{PORT}")
