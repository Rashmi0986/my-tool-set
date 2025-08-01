
#Reading from STDIN and receiving two parameters which was host and ports that I need to reach and print status 

import sys
import socket

def check_host_port(host, port):
    try:
        port = int(port)
        with socket.create_connection((host, port), timeout=3):
            print(f"{host}:{port} is reachable ✅")
    except (socket.timeout, socket.error):
        print(f"{host}:{port} is not reachable ❌")
    except ValueError:
        print("Invalid port. Must be an integer.")

if __name__ == "__main__":
    for line in sys.stdin:
        parts = line.strip().split()
        if len(parts) != 2:
            print("Please provide input in the format: <host> <port>")
            continue
        host, port = parts
        check_host_port(host, port)


✅ How to Run It:
You can run this script from the command line and provide input via STDIN, for example:


$ python check_port_status.py
example.com 80
example.com 9999

$ cat hosts.txt | python check_port_status.py
Where hosts.txt contains:

