from typing import Dict

from match.properties import CountResult

from src.players.enum_player import KindOfPlayer


def aggregate(statistics: Dict, count_result: CountResult) -> None:
    if statistics["timeout_ended"] is True:
        count_result["total_ended_by_timeout"] += 1

    if statistics["behavior_winner"] == KindOfPlayer.DEMANDING.value:
        count_result["demanding"] += 1

    if statistics["behavior_winner"] == KindOfPlayer.IMPULSIVE.value:
        count_result["impulsive"] += 1

    if statistics["behavior_winner"] == KindOfPlayer.CAUTIOUS.value:
        count_result["cautious"] += 1

    if statistics["behavior_winner"] == KindOfPlayer.RANDOM.value:
        count_result["random"] += 1

    if statistics["round_total"] < 1000:
        count_result["round_total"] += statistics["round_total"]
