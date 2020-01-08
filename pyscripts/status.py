import time
import socket as s
import select as sel

HOST_PORT = HOST, PORT = "127.0.0.1", 4343
status = "idle"

def status_listener():
    global status
    with s.socket(s.AF_INET, s.SOCK_STREAM) as sock:
        sock.bind(HOST_PORT)
        sock.listen()
        while True:
            ready = sel.select([sock], [], [], 2)
            if ready[0]:
                print("ready for new conn")
                conn, addr = sock.accept()
                status = conn.recv(1024)

            print(status)
            status = "idle"

if __name__ == '__main__':
    status_listener()
