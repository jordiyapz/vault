# Vault

Written by [Jordi Yaputra](https://github.com/jordiyapz)

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
- Run using `./vault PATH` where `PATH` is your unix connection file.

### From source code

- Move the private key to this project folder.
- Follow [prerequisite instruction](https://github.com/jordiyapz/vault#prerequisite).
- Run the following commands in terminal:
    ```
    pip install -r requirements.txt
    python main.py PATH
    ```
    where `PATH` is your unix connection file.

> ⚠️ **Warning**
>
> Running this program will automatically discard existing connection `PATH` and create a new one.
