# A sample transfer listener

## Requirements
- Python 3
- PIP 3
- Python venv
- Make (Optional, to use make Makefile)
- jq (Optional, to format API response)

## Setup

### Easy Setup

To setup local env run `./setup.sh`

### Manual Setup

1. Create venv using `python3 -m venv env`
2. Activate venv with `source env/bin/activate`
3. Install requirements from requirements.txt with `pip install -r requirements.txt`
4. Run db migration with `python manage.py migrate`

### Set config

- Set API key with `TRANSFER_LISTENER_SECRET_KEY_INFURA_API_KEY=<API_KEY>` or use dotenv by adding this in a file `<project_root>/eth_transfer_listener/.env`

# Usage

## Start Django Server

Start django server with `python manage.py runserver` . API endpoint will be at `/api/v1/transfers/`

## Start Listener

Start listener on management command using `python manage.py eth_listen_on_transfer`

## Sync transfer history

Sync transfer history with `python manage.py eth_pull_transfers` . To specify specific start and block use `--start_block` and `--end_block` command line args

## To make a request for specific token_id

### Using makefile

To use the make file command, run `TOKEN_ID=<id> make req`

### Using curl

`curl` can be used to retrieve specific transfer with token_id using. `curl localhost:8000/api/v1/transfers/?token_id=<id>`

