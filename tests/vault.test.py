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

messages = [
    json.dumps({
        "id": "12480743",
        "type": "sign_transfer",
        "from_address": "0x5ce9454909639D2D17A3F753ce7d93fa0b9aB12E",
        "to_address": "0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
        "amount": "2.3"
    }),
    json.dumps({
        "id": "12480744",
        "type": "sign_transfer",
        "from_address": "0x5ce9454909639D2D17A3F753ce7d93fa0b9aB12E",
        "to_address": "0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
        "amount": ".001"
    })
]

with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
    print(SOCK_PATH)
    s.connect(SOCK_PATH)
    send_msg(s, '\n'.join(messages).encode())

    data = recv_msg(s)
    print(data.decode())
