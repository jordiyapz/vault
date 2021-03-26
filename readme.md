# Vault

> Written by [Jordi Yaputra](https://github.com/jordiyapz)

A piece of software used to sign valid ethereum transactions.

This is for linux only.

## Prerequisite

- Get an account on [https://infura.io](https://infura.io)
- Create a project and copy the project id.
- Run `export WEB3_INFURA_PROJECT_ID=xxxxxxxx` where `xxxxxxxx` is your infura project id.
- For more information visit [here](https://web3py.readthedocs.io/en/latest/providers.html#infura-mainnet).

## Build

- Clone this repository and cd into this folder (named `vault` by default).
- Run `pip install -r requirements.txt`
- Build using `pyinstaller main.py --onefile --name vault`
- The execute file can be found in `dist/` with name `vault`

## Usage

### Using builded executable

- Move the executable file to the same directory as where you save your private key.
- Follow [prerequisite instruction](https://github.com/jordiyapz/vault#prerequisite).
- Run the server using `./vault PATH` where `PATH` is your unix connection file.

### From source code

- Move the private key to this project folder.
- Follow [prerequisite instruction](https://github.com/jordiyapz/vault#prerequisite).
- Run the server with following commands in terminal:
  ```
  pip install -r requirements.txt
  python main.py PATH
  ```
  where `PATH` is your unix connection file.

> ⚠️ **Warning**
>
> Running this program will automatically discard existing connection `PATH` and create a new one.

Make sure the server file is on the same directory as your private key. Copy your private key and name it with your eth address. For example your eth address is `0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe`, then your private key should be named `de0B295669a9FD93d5F28D9Ec85E40f4cb697BAe`.

After the server has been started, you can communicate to the server via unix socket on `PATH` connection. Send a valid transactions in oneline json string format separated by newlines `\n` in this format:

```js
{
	"id": "some id",
	"type": "sign_transfer",
	"from_address": "your private key file name",
    "to_address": "ETH address",
	"amount": "Amount as string in ether unit"
}
```

> **Note:** this multiline format is just for easier representation. You can just use oneline compact json string format.

for example:

```js
{ "id": "122", "type": "sign_transfer", "from_address": "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe", "to_address": "0x55e02616a249f9653fae5ff9e9cafc1a2a497e9f", "amount": "0.12301" }
{ "id": "123", "type": "sign_transfer", "from_address": "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe", "to_address": "0x48c6ff9094b529b7b525b8ff00455e66b7b58734", "amount": "0.4" }
```

If nothing goes wrong, you will receive response in this format:

```js
{
	"id": "some id",
	"tx": "your raw signed transaction cipher" 
}
```

for example:

```js
{ "id": "122", "tx": "0x07e6cc08efcc3550b00a40561df9e7e9af90e8e417ddd8b6f70454fe2912938e" }
{ "id": "123", "tx": "0x34ffbe2bdf8a2bae4caf459e86d9ebc206609cae9260cd13e8bdfec665eb7b92" }
```
