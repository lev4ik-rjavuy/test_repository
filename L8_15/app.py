from typing import List

import sentry_sdk

sentry_sdk.init(
    dsn="dsn",
    traces_sample_rate=1.0,
)


class InvalidDataError(ValueError):
    pass


def analyze_load(data_input: str) -> float:
    raw_values = data_input.split()

    if not raw_values:
        raise InvalidDataError("Не введено жодних даних. Будь ласка, введіть числа.")

    numeric_values: List[float] = []

    for val in raw_values:
        try:
            numeric_values.append(float(val))
        except ValueError:
            raise InvalidDataError(
                f"Некоректне значення: '{val}'. Всі показники мають бути числами."
            )

    average_load = sum(numeric_values) / len(numeric_values)
    return average_load


def main():
    user_input = input(
        "Введіть показники навантаження через пробіл (наприклад: 45.5 60 72.1): "
    )

    try:
        average = analyze_load(user_input)
        print(f"Успіх! Середнє навантаження: {average:.2f}")

    except Exception as error:
        print(f"Сталася помилка: {error}")

        sentry_sdk.capture_exception(error)
        print("Інформацію про помилку успішно відправлено в панель Sentry.")


if __name__ == "__main__":
    main()
