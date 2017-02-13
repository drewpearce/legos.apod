from Legobot.Lego import Lego
import requests
import logging
import json

logger = logging.getLogger(__name__)

class APOD(Lego):
    def listening_for(self, message):
        if message['text'] is not None:
            try:
                return message['text'].split()[0] == '!apod'
            except Exception as e:
                logger.error('APOD lego failed to check message text: %s' % e)
                return False

    def get_name(self):
    return 'apod'

    def get_help(self):
    return 'Fetch a NASA Astronomy Photo of the Day. Usage: !apod [r|random|date]'
