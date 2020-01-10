import time
import socket as s
import select as sel

HOST_PORT = HOST, PORT = "127.0.0.1", 4343

def status_sender(data):
    with s.socket(s.AF_INET, s.SOCK_STREAM) as sock:
        sock.connect(HOST_PORT)
        sock.sendall(new_status)


if __name__ == '__main__':
    status_listener()
