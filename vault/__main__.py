import socket
import os
import sys
import json
from vault.utils import recv_msg, send_msg
from vault.eth import sign_transfer

BUF_SIZE = 1024

if len(sys.argv) != 2:
    print('usage: {} PATH'.format(sys.argv[0]))
    sys.exit(1)

SOCK_PATH = sys.argv[1]

if os.path.exists(SOCK_PATH):
    os.remove(SOCK_PATH)


def process_msg(msg):
    # process msg and return response
    commands = [json.loads(json_str)
                for json_str in msg.split('\n') if json_str]

    for command in commands:
        print('Signing {}:'.format(command['id']), end=' ')
        address = command['from_address']
        try:
            filename = address.split('x')[1]
            with open(filename, 'rb') as f:
                private_key = f.read()

        except FileNotFoundError:
            print('Cannot find {} address key'.format(filename))
            return 'private key for address {} not found'.format(address).encode()

        try:
            signed = sign_transfer(private_key, address,
                                   command['to_address'], command['amount'])

            command['tx'] = signed.rawTransaction.hex()
            print('OK')

        except Exception as ex:
            print('Error: {}'.format(ex))
            continue

    return '\n'.join([
        json.dumps({
            'id': command['id'],
            'tx': command['tx']
        }) for command in commands
        if 'tx' in command
    ]).encode()

def main():
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as server:
        server.bind(SOCK_PATH)
        server.listen()
        print('Listening on {}'.format(SOCK_PATH))

        while True:
            try:
                conn, addr = server.accept()
                with conn:
                    data = recv_msg(conn)
                    msg = data.decode()
                    response = process_msg(msg)
                    send_msg(conn, response)

            except KeyboardInterrupt:
                print()
                break

    os.remove(SOCK_PATH)
