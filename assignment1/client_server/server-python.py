###############################################################################
# server-python.py
# Name: Kristin Yim
# NetId: kyim6
###############################################################################

import sys
import socket

RECV_BUFFER_SIZE = 2048
QUEUE_LENGTH = 10

def server(server_port):
    """TODO: Listen on socket and print received message to sys.stdout"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', server_port))
    s.listen(QUEUE_LENGTH)
    conn, addr = s.accept()
    
    total_size = int(conn.recv(RECV_BUFFER_SIZE))
    bytes_recd = 0
    chunks = []
    while bytes_recd < total_size:
        chunk = conn.recv(min(total_size - bytes_recd, RECV_BUFFER_SIZE))
        if chunk == '':
            break
        chunks.append(chunk)
        bytes_recd += len(chunk)
    sys.stdout.write(''.join(chunks))
    sys.stdout.flush()
    conn.close()

def main():
    """Parse command-line argument and call server function """
    if len(sys.argv) != 2:
        sys.exit("Usage: python server-python.py [Server Port]")
    server_port = int(sys.argv[1])
    server(server_port)

if __name__ == "__main__":
    main()
