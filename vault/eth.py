from web3.exceptions import InfuraKeyNotFound

try:
    from web3.auto.infura import w3
    '''export WEB3_INFURA_PROJECT_ID=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'''
except InfuraKeyNotFound as err:
    print(err)
    print("Run `export WEB3_INFURA_PROJECT_ID=xxxxxxxx` where xxxxxxxx is your infura project id.", 'For more information visit: https://web3py.readthedocs.io/en/latest/providers.html#infura-mainnet')

if not w3.isConnected():
    print('Connection failed')

from decimal import Decimal
from web3 import Web3


def sign_transfer(private_key, from_address, to_address, amount):
    gas = 21000     # minimum
    gas_price = w3.eth.gas_price
    amount_wei = Web3.toWei(Decimal(amount), 'ether')
    value = amount_wei - gas*gas_price
    if value < 0:
        raise Exception('amount is too small')

    return w3.eth.account.sign_transaction({
        'nonce': 0,
        'gasPrice': gas_price,
        'gas': gas,
        'from': from_address,
        'to': to_address,
        'value': value
    }, private_key=private_key)
