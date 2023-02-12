from .base_player import BasePlayer
from .enum_player import KindOfPlayer


class CautiousPlayer(BasePlayer):
    def __init__(self):
        super(CautiousPlayer, self).__init__(behavior=KindOfPlayer.CAUTIOUS)

    def should_or_not_do_the_payment(self, property):
        if self.balance - property["sell_cost"] >= 80:
            property["owner"] = self
            self.pay(property["sell_cost"])
