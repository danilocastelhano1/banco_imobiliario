from random import randint

from typing import List
from typing import TypedDict
from typing import Optional
from typing import Any


class Property(TypedDict):
    name: str
    sell_cost: int
    rent_cost: int
    owner: Optional[Any]


class CountResult(TypedDict):
    impulsive: int
    demanding: int
    cautious: int
    random: int
    total_ended_by_timeout: int
    round_total: int


def generate_properties():
    properties_list: List = []

    for i in range(1, 21):
        properties_list.append(
            Property(
                name=f"property_{i}",
                sell_cost=randint(50, 300),
                rent_cost=randint(50, 150),
                owner=None
            )
        )

    return properties_list
