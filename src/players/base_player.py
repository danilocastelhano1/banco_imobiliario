import random
from abc import ABC, abstractmethod
from ..match.properties import Property

INITIAL_BALANCE: int = 300


class BasePlayer(ABC):
    def __init__(self, behavior):
        self._balance: int = INITIAL_BALANCE
        self.behavior: str = behavior
        self._properties_covered: int = 0
        self._next_property: int = 0
        self.balance = self._balance

    def pay(self, property_value: int) -> None:
        self.balance = self.balance - property_value

    def receive(self, round_value: int) -> None:
        self.balance = self.balance + round_value

    def go_to_next_property(self, dice_result: int) -> int:
        self._next_property += dice_result
        if self._next_property > 20:
            self._next_property -= 20
        return self._next_property

    def check_board_completed(self, dice_result: int) -> None:
        self._properties_covered += dice_result
        if self._properties_covered >= 20:
            self._properties_covered = 0
            self.receive(round_value=100)

    def roll_the_six_side_dice(self) -> int:
        return random.randint(1, 6)

    @abstractmethod
    def should_or_not_do_the_payment(self, property: Property):
        raise NotImplementedError()
