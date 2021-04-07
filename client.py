# -*- coding: utf-8 -*-
import socket
import os
import sys
import json
from vault.utils import send_msg, recv_msg

BUF_SIZE = 1024
SOCK_PATH = sys.argv[1]
if not os.path.exists(SOCK_PATH):
    print('could not connect')
    sys.exit(1)

with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
    s.connect(SOCK_PATH)
    print('Connected to', SOCK_PATH)

    s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

    print('\nEnter ctrl+c or press ENTER to quit.')
    while True:
        try:
            msg = input("> ")
            send_msg(s, msg.encode())
            data = recv_msg(s).decode()
            print(data)
            if data == 'disconnected':
                break

        except KeyboardInterrupt:
            send_msg(s, ''.encode())
            print('\n' + recv_msg(s).decode())
            break
