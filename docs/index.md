# Документація по репозиторію

Тут є лабораторні роботи з дисципліни "Інструментальні засоби програмування"

## Перелік лаб

- lab1
- lab2
- lab3
- lab4
- lab5
- lab6
- lab7
- lab8
- idz

### Якийсь код

```python
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
```
