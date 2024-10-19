from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from web3 import Web3

from transfer_listener.models import Transfer
from transfer_listener.constants import ETH_ADDRESS, ABI


DEFAULT_START_BLOCK = 20997447
DEFAULT_END_BLOCK = 20999494 


class Command(BaseCommand):
    help = "Pull ETH transfer events"

    def add_arguments(self, parser):
        parser.add_argument("--start_block", nargs="+", type=int)
        parser.add_argument("--end_block", nargs="+", type=int)

    def handle(self, *args, **options) -> None:
        start_block = options.get('start_block')
        end_block = options.get('end_block')
        url_provider = f'https://mainnet.infura.io/v3/{settings.INFURA_API_KEY}' #{urllib.parse.quote_plus(settings.INFURA_API_KEY)}'

        if not start_block:
            start_block = DEFAULT_START_BLOCK
        if not end_block:
            end_block = DEFAULT_END_BLOCK
        if start_block > end_block:
            raise CommandError('start_block must be less than end_block')

        w3 = Web3(Web3.HTTPProvider(url_provider))

        contract = w3.eth.contract(address=Web3.to_checksum_address(ETH_ADDRESS), abi=ABI)

        events = contract.events.Transfer().create_filter(
            from_block=start_block, to_block=end_block
        ).get_all_entries()

        for e in events:
            Transfer.objects.get_or_create(
                    transaction_hash=e.transactionHash.hex(),
                    defaults={
                        'token_id': e.args.tokenId,
                        'from_address': e.args['from'],
                        'to_address': e.args.to,
                        'block_number': e.blockNumber,
                        }
                    )
