import random
from .base_player import BasePlayer
from .enum_player import KindOfPlayer


class RandomPlayer(BasePlayer):
    def __init__(self):
        super(RandomPlayer, self).__init__(behavior=KindOfPlayer.RANDOM)

    def should_or_not_do_the_payment(self, property):
        if random.choice([0, 1]) == 1:
            property["owner"] = self
            self.pay(property["sell_cost"])
