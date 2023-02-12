from .base_player import BasePlayer
from .enum_player import KindOfPlayer


class DemandingPlayer(BasePlayer):
    def __init__(self):
        super(DemandingPlayer, self).__init__(behavior=KindOfPlayer.DEMANDING)

    def should_or_not_do_the_payment(self, property):
        if property["rent_cost"] > 50:
            property["owner"] = self
            self.pay(property["sell_cost"])
