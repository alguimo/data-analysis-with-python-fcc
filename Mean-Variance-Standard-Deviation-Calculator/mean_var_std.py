import numpy as np

STATS = (
    ("mean", np.mean),
    ("variance", np.var),
    ("standard deviation", np.std),
    ("max", np.max),
    ("min", np.min),
    ("sum", np.sum),
)

AXES = (0, 1, None)


def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(numbers, dtype=float).reshape(3, 3)

    calculations = {}
    for name, function in STATS:
        calculations[name] = [
            _python_value(function(matrix) if axis is None else function(matrix, axis=axis))
            for axis in AXES
        ]

    return calculations


def _python_value(result):
    if np.ndim(result) == 0:
        return _number(result)
    return [_number(value) for value in result]


def _number(value):
    number = float(value)
    return int(number) if number.is_integer() else number
