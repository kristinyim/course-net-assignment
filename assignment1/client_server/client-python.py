###############################################################################
# client-python.py
# Name: Kristin Yim
# NetId: kyim6
###############################################################################

import sys
import socket

SEND_BUFFER_SIZE = 2048

def client(server_ip, server_port, msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUFFER_SIZE)
    s.connect((server_ip, server_port))
    s.sendall(msg)
    s.close()

def main():
    """Parse command-line arguments and call client function """
    if len(sys.argv) != 3:
        sys.exit("Usage: python client-python.py [Server IP] [Server Port] < [message]")
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    msg = sys.stdin.read()
    client(server_ip, server_port, msg)

if __name__ == "__main__":
    main()
