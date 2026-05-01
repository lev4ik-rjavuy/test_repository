from typing import List, Tuple


def calculate_average_pressure(measurements: List[Tuple[int, int]]) -> Tuple[int, int]:
    """
    doctests:
    >>> calculate_average_pressure([(120, 80), (110, 70)])
    (115, 75)
    >>> calculate_average_pressure([(120, 80), (120, 80), (120, 80)])
    (120, 80)
    >>> calculate_average_pressure([(135, 85)])
    (135, 85)
    >>> calculate_average_pressure([])
    (0, 0)
    """
    if not measurements:
        return 0, 0

    total_systolic = sum(sys for sys, dia in measurements)
    total_diastolic = sum(dia for sys, dia in measurements)
    count = len(measurements)

    return total_systolic // count, total_diastolic // count


def is_pressure_normal(systolic: int, diastolic: int) -> bool:
    """
    doctests:
    >>> is_pressure_normal(115, 75)
    True
    >>> is_pressure_normal(120, 80)
    True
    >>> is_pressure_normal(90, 60)
    True
    >>> is_pressure_normal(130, 80)
    False
    >>> is_pressure_normal(110, 85)
    False
    """
    is_sys_normal = 90 <= systolic <= 120
    is_dia_normal = 60 <= diastolic <= 80

    return is_sys_normal and is_dia_normal


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
