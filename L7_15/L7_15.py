from collections import Counter
from typing import Dict, List, Tuple


def find_popular_routes(
    trips: List[Dict[str, str]],
) -> List[Tuple[Tuple[str, str], int]]:
    """
    doctests:
    >>> trips = [
    ...     {"start": "Київ", "end": "Львів"},
    ...     {"start": "Київ", "end": "Одеса"},
    ...     {"start": "Київ", "end": "Львів"}
    ... ]
    >>> find_popular_routes(trips)
    [(('Київ', 'Львів'), 2), (('Київ', 'Одеса'), 1)]

    >>> find_popular_routes([{"start": "А", "end": "Б"}, {"start": "А", "end": "Б"}])
    [(('А', 'Б'), 2)]

    >>> find_popular_routes([])
    []
    """
    if not trips:
        return []

    routes = [
        (trip["start"], trip["end"])
        for trip in trips
        if "start" in trip and "end" in trip
    ]

    route_counts = Counter(routes)

    return route_counts.most_common()


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
