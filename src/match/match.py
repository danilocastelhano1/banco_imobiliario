import random
from typing import Optional
from typing import List
from typing import Dict

from .properties import generate_properties
from ..players.base_player import BasePlayer
from ..match.properties import Property


class Match:
    def __init__(self, players) -> None:
        self.players: List[BasePlayer] = players
        self.round_total: int = 0
        self.timeout_ended: bool = False
        self.proprietaries: list = generate_properties()
        self.winner_behavior: str = None
        self.board_result: List[BasePlayer] = None

    def play_the_game(self) -> None:
        players_order = random.sample(self.players, 4)
        match_end = False
        while not match_end:
            self.board_result = self.round_board(players_order)
            match_end, self.winner_behavior = self.check_match_end(self.board_result)

    def check_match_end(self, players: list) -> tuple[bool, Optional[str]]:
        players_eliminated: int = 0
        winner_behavior: Optional[str] = None
        if self.round_total == 1000:
            self.timeout_ended = True
            return True, "Ended by Timeout"

        for player in players:
            if player.balance <= 0:
                players_eliminated += 1
            else:
                winner_behavior = player.behavior.value

        if players_eliminated == len(players):
            return True, "No Winners"
        elif players_eliminated == len(players) - 1:
            return True, winner_behavior
        return False, None

    def generate_statistics(self) -> Dict:
        return {
            "players": self.board_result,
            "behavior_winner": self.winner_behavior,
            "timeout_ended": self.timeout_ended,
            "round_total": self.round_total
        }

    def round_board(self, players: list[BasePlayer]) -> list[BasePlayer]:
        self.round_total += 1
        for player in players:
            if player.balance > 0:
                self.board(player)
            else:
                for prop in self.proprietaries:
                    if prop["owner"]:
                        if prop["owner"] == player:
                            prop["owner"] = None

        return players

    def board(self, player):
        dice_return = player.roll_the_six_side_dice()
        selected_property: Property = self.proprietaries[player.go_to_next_property(dice_return) - 1]

        if not selected_property["owner"] and player.balance >= selected_property["sell_cost"]:
            player.should_or_not_do_the_payment(property=selected_property)
        else:
            if selected_property["owner"]:
                if selected_property["owner"] != player:
                    player.pay(selected_property["rent_cost"])
                    selected_property["owner"].receive(selected_property["rent_cost"])

        player.check_board_completed(dice_return)
