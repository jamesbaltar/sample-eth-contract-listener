.PHONY: start
start:
	python3 manage.py runserver

.PHONY: listen
listen:
	python3 manage.py eth_listen_on_transfer

.PHONY: req
req:
	curl localhost:8000/api/v1/transfers/?token_id=$$TOKEN_ID | jq

