import sentry_sdk

sentry_sdk.init(
    dsn="dsn",
    traces_sample_rate=1.0,
)


class InvalidDimensionError(ValueError):
    pass


def calculate_area(length: float, width: float) -> float:
    """
    doctests:
    >>> calculate_area(5.0, 4.0)
    20.0
    >>> calculate_area(2.5, 4.0)
    10.0
    """
    if length <= 0 or width <= 0:
        raise InvalidDimensionError(
            f"Сторона повинна бути більшою за нуль. Отримано: довжина={length}, ширина={width}"
        )

    return length * width


def main():
    try:
        length_str = input("Введіть довжину: ")
        width_str = input("Введіть ширину: ")

        length = float(length_str)
        width = float(width_str)

        area = calculate_area(length, width)
        print(f"Площа прямокутника: {area:.2f}")

    except ValueError as e:
        print(f"Помилка: {e}")
        sentry_sdk.capture_exception(e)
        print("ℹІнформацію про помилку відправлено до Sentry.")
    except Exception as e:
        print(f"Невідома помилка: {e}")
        sentry_sdk.capture_exception(e)


if __name__ == "__main__":
    main()
