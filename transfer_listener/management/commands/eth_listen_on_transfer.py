import logging
import time

from django.core.management.base import BaseCommand
from django.conf import settings
from web3 import Web3
from requests.exceptions import RequestException

from transfer_listener.models import Transfer
from transfer_listener.constants import ETH_ADDRESS, ABI


LOGGER = logging.getLogger(__name__)
START_BLOCK = 20997447


class Command(BaseCommand):
    help = "Start listener for ETH transfer events"

    def handle(self, *args, **options) -> None:
        last_block = Transfer.objects.order_by('-block_number').values_list('block_number', flat=True).first()
        if not last_block:
            last_block = START_BLOCK

        LOGGER.info('Start from block %d', last_block)
        url_provider = f'https://mainnet.infura.io/v3/{settings.INFURA_API_KEY}' #{urllib.parse.quote_plus(settings.INFURA_API_KEY)}'
        while True:
            w3 = Web3(Web3.HTTPProvider(url_provider))
            try:
                while True:
                    contract = w3.eth.contract(address=Web3.to_checksum_address(ETH_ADDRESS), abi=ABI)
                    
                    events = contract.events.Transfer().create_filter(from_block=last_block).get_all_entries()
                    for e in events:
                        t, _ = Transfer.objects.get_or_create(
                                transaction_hash=e.transactionHash.hex(),
                                defaults={
                                    'token_id': e.args.tokenId,
                                    'from_address': e.args['from'],
                                    'to_address': e.args.to,
                                    'block_number': e.blockNumber,
                                    }
                                )
                        last_block = t.block_number
                        LOGGER.info('Saved %s', t.transaction_hash)
                    time.sleep(6)
            except RequestException:
                LOGGER.exception('An error occured while trying to retrieve transfers')
            time.sleep(6)
