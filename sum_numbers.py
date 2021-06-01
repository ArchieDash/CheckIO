from itertools import compress


def sum_numbers(text: str) -> int:
    words = text.split()  # Split the given sentence by words
    num_check = [word.isnumeric() for word in words]  # Check if word can be represent as int
    nums = list(compress(words, num_check))  # Filter words by conditions of the check
    return sum([int(n) for n in nums])  # Return sum of numbers


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi'))

    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0