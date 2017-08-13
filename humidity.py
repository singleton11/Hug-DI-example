import random

from nameko.rpc import rpc


class Humidity(object):
    name: str = 'humidity_service'

    @rpc
    def get_humidity(self) -> int:
        return random.randrange(0, 100)
