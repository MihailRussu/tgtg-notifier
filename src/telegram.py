import logging
import os

import requests

logger = logging.getLogger(__name__)

try:
    TELEGRAM_CHAT_ID = os.environ['TELEGRAM_CHAT_ID']
    TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
except KeyError as k:
    logger.error(f'ERROR: Missing Telegram env var "{k}"')
    raise RuntimeError from k


def send_notification(caption: str, photo: str) -> None:
    """Send a photo to Telegram"""

    url = f'https://api.telegram.org/{TELEGRAM_BOT_TOKEN}/sendPhoto'
    data = {'chat_id': TELEGRAM_CHAT_ID, 'caption': caption, 'photo': photo}
    response = requests.post(url, data=data, timeout=10)
    response.raise_for_status()
