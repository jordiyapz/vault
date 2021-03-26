from vault.eth import sign_transfer
from hexbytes import HexBytes

PRIVATE_KEY = b"\xb2\\}\xb3\x1f\xee\xd9\x12''\xbf\t9\xdcv\x9a\x96VK-\xe4\xc4rm\x03[6\xec\xf1\xe5\xb3d"

FROM_ADDR = '0x5ce9454909639D2D17A3F753ce7d93fa0b9aB12E'


signed = sign_transfer(
    PRIVATE_KEY,
    FROM_ADDR, '0xd3CdA913deB6f67967B99D67aCDFa1712C293601', '10')
repr(signed.rawTransaction)
assert signed.rawTransaction == HexBytes('0xf86c8085202170e40082520894d3cda913deb6f67967b99d67acdfa1712c293601888abcd74d5558e000801ca074cd478946d0599179316473d9c9d04688b8a348b1ecb494509b25f7ba2a1a33a037fc6f9d9f8458c7965f083fdd8946ec9d360176a864c470a4ce9f63c3ef9331')
