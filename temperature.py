import random

from nameko.rpc import rpc


class Temperature(object):
    name: str = 'temperature_service'

    @rpc
    def get_temperature(self) -> int:
        return random.randrange(1, 100)
