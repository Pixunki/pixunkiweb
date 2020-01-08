import socket as s
import select as sel

import threading
import time

import pixel

HOST_PORT = HOST, PORT = "127.0.0.1", 4343
status = ["idle"]
alive = True

def status_listener():
    with s.socket(s.AF_INET, s.SOCK_STREAM) as sock:
        sock.bind(HOST_PORT)
        sock.listen()
        while status[0] != "dead":
            ready = sel.select([sock], [], [], 2)  # 2 seconds
            if ready[0]:
                conn, addr = sock.accept()
                status[0] = conn.recv(1024).decode()

status_server = threading.Thread(target=status_listener)
status_server.start()

def my_led():
    try:
        my_board = pixel.Field(boards=2, size_board_x=8, size_board_y=8)

        while True:
            print(status)
            if status[0] == "green":
                my_board.paint(pixel.COLORS["green"])
            elif status[0] == "blue":
                my_board.paint(pixel.COLORS["darkblue"])
            else:
                my_board.paint(pixel.COLORS["black"])

            status[0] = "idle"

            time.sleep(1)
    except KeyboardInterrupt:
        status[0] = "dead"

if __name__ == '__main__':
    my_led()
