from .base_player import BasePlayer
from .enum_player import KindOfPlayer


class ImpulsivePlayer(BasePlayer):
    def __init__(self):
        super(ImpulsivePlayer, self).__init__(behavior=KindOfPlayer.IMPULSIVE)

    def should_or_not_do_the_payment(self, property):
        property["owner"] = self
        self.pay(property["sell_cost"])
