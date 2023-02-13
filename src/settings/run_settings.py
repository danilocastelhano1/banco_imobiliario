from src.players.impulsive_player import ImpulsivePlayer
from src.players.demanding_player import DemandingPlayer
from src.players.cautious_player import CautiousPlayer
from src.players.random_player import RandomPlayer

from src.match.match import Match

from src.match.properties import CountResult
from src.settings.aggregate import aggregate


def run_and_display_statistics():
    total_run: int = 300

    count_result = CountResult(
        impulsive=0,
        demanding=0,
        cautious=0,
        random=0,
        total_ended_by_timeout=0,
        round_total=0,
    )

    for index in range(0, total_run):
        players = [
            ImpulsivePlayer(),
            DemandingPlayer(),
            RandomPlayer(),
            CautiousPlayer(),
        ]

        match = Match(players)
        match.play_the_game()
        aggregate(
            statistics=match.generate_statistics(),
            count_result=count_result
        )

    print("=" * 150)
    print(f"Total matches ended by timeout {count_result['total_ended_by_timeout']}")
    print(f"Average round match without Timeout {count_result['round_total'] / total_run:.0f}")
    print("-" * 150)
    print(f"Winner % DEMANDING {(count_result['demanding'] / total_run) * 100:.2f}%")
    print(f"Winner % IMPULSIVE {(count_result['impulsive'] / total_run) * 100:.2f}%")
    print(f"Winner % CAUTIOUS {(count_result['cautious'] / total_run) * 100:.2f}%")
    print(f"Winner % RANDOM {(count_result['random'] / total_run) * 100:.2f}%")
    print("-" * 150)
    champion_behavior = [
        count_result['demanding'],
        count_result['impulsive'],
        count_result['cautious'],
        count_result['random'],
    ]
    champion_behavior.sort()

    champion_value = champion_behavior[-1]
    name = [key.upper() for key, value in count_result.items() if value == champion_value]
    print(f"Most winner behavior is: {name[0]} with {champion_behavior[-1]} winners")
    print("=" * 150)
