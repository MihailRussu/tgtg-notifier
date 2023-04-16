import logging
import os

from tgtg import TgtgClient

from sentry import init_sentry, serverless_function

logger = logging.getLogger(__name__)

try:
    TGTG_ACCESS_TOKEN = os.environ['TGTG_ACCESS_TOKEN']
    TGTG_REFRESH_TOKEN = os.environ['TGTG_REFRESH_TOKEN']
    TGTG_USER_ID = os.environ['TGTG_USER_ID']
    TGTG_COOKIE = os.environ['TGTG_COOKIE']
    TGTG_ITEM_IDS = os.environ['TGTG_ITEM_IDS'].split(',')
except KeyError as k:
    logger.error(f'ERROR: Missing environment variable "{k}"')
    raise RuntimeError from k

client = TgtgClient(
    access_token=TGTG_ACCESS_TOKEN,
    refresh_token=TGTG_REFRESH_TOKEN,
    user_id=TGTG_USER_ID,
    cookie=TGTG_COOKIE,
)

init_sentry()


@serverless_function
def handle(event: dict, context: dict) -> str:
    """handle a request to the function
    Args:
        event (dict): request params
        context (dict): function call metadata
    """

    print(f'Event: {event}, context: {context}')

    for item_id in TGTG_ITEM_IDS:
        try:
            item = client.get_item(item_id)
            if item and item.get('items_available', 0) > 0:
                name = item['display_name']
                items = item['items_available']
                # image = item['item']['cover_picture']['current_url']
                address = item['pickup_location']['address']['address_line']
                print(f'#{items} of "{name}" available at "{address}"')
        except Exception as e:
            logger.error(e)
            return 'NOT OK'

    return 'OK'
