def nearest_value(values: set, one: int) -> int:
    # Make a dict {[value]:[delta of value and given number]}
    deltas = dict(zip(values, [abs(one - value) for value in values]))
    # Find the min delta in dict
    min_delta = min(deltas.values())
    # Retrieve values with min delta
    min_deltas = {k: v for k, v in deltas.items() if v == min_delta}
    # Return min value with min delta
    return min(min_deltas.keys())


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1