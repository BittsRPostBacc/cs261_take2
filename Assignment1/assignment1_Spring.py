# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> (int, int):
    """
    Function takes an array and returns the minimum and maximum values inside
    """
    count = 0
    length = arr.length()

    while count < length:
        if count == 0:
            low_value = arr[count]
            high_value = arr[count]
            count += 1
        elif arr[count] < low_value:
            low_value = arr[count]
            count += 1
        elif arr[count] > high_value:
            high_value = arr[count]
            count += 1
        else:
            count += 1

    min_and_max = (low_value, high_value)
    return min_and_max


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    Takes an array and determines if the values are divisible:
        3 = fizz
        5 = buzz
        Both = fizzbuzz
    """
    index = 0
    length = arr.length()
    fizz_buzz_results = StaticArray(length)
    while index < length:
        if arr[index] % 5 == 0 and arr[index] % 3 == 0:
            fizz_buzz_results.set(index, "fizzbuzz")
            index += 1
        elif arr[index] % 5 == 0:
            fizz_buzz_results.set(index, "buzz")
            index += 1
        elif arr[index] % 3 == 0:
            fizz_buzz_results.set(index, "fizz")
            index += 1
        else:
            fizz_buzz_results.set(index, arr[index])
            index += 1

    return fizz_buzz_results


# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    Function takes an array and reverses the order of the elements in place
    """
    length = arr.length()

    for i in range(length // 2):
        arr[i], arr[length - i - 1] = arr[length - i - 1], arr[i]


# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    Function takes an array and a "step" integer
        Returns an array with the values migrated the step amount
    """
    length = arr.length()
    rotated_array = StaticArray(length)

    # Get Step changes that fit within the array correctly
    adjusted_steps = steps % length

    for i in range(length):
        if adjusted_steps >= 0:
            new_index = (i + adjusted_steps) % length
        else:
            new_index = i - abs(adjusted_steps)
            if new_index < 0:
                new_index += length

        rotated_array[new_index] = arr[i]

    return rotated_array


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """
    Function takes a start number and end number and returns an array
        that contains the numbers from start to end inclusive
    """
    if start < end:
        ranged_array = StaticArray(abs(end - start) + 1)
        length = ranged_array.length()
        curr = start
        for i in range(length):
            ranged_array[i] = curr
            curr += 1
    else:
        ranged_array = StaticArray(abs(start - end) + 1)
        length = ranged_array.length()
        curr = start
        for i in range(length):
            ranged_array[i] = curr
            curr -= 1

    return ranged_array


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    Function takes an array and determines if it is sorted in ascending, descending
        or not at all
    """
    length = arr.length()
    if length == 1:
        return 1

    return_val = None
    for item in range(1, length):
        if arr[item] < arr[item -1]:
            if return_val == 1:
                return 0
            else:
                return_val = -1
        elif arr[item] > arr[item -1]:
            if return_val == -1:
                return 0
            else:
                return_val = 1
        else:
            return 0

    return return_val


# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> (int, int):
    """
    TODO: Write this implementation
    """
    max_frequency = 0
    mode = None
    current_frequency = 0
    current_value = None
    length = arr.length()

    for value in range(length):
        if arr[value] != current_value:
            current_value = arr[value]
            current_frequency = 0

        current_frequency += 1

        if current_frequency > max_frequency:
            max_frequency = current_frequency
            mode = current_value

    return (mode, max_frequency)


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    if arr.length() == 1:
        return arr

    length = arr.length()
    num_unique = 1

    for i in range(1, length):
        if arr[i] != arr[i - 1]:
            num_unique += 1

    new_arr = StaticArray(num_unique)
    new_arr_index = 0
    new_arr[new_arr_index] = arr[0]
    new_arr_index += 1

    for i in range(1, length):
        if arr[i] != arr[i - 1]:
            new_arr[new_arr_index] = arr[i]
            new_arr_index += 1

    return new_arr


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    length = arr.length()
    # Find the minimum and maximum values in the array
    min_value = arr[0]
    max_value = arr[0]
    for num in range(1, length):
        if arr[num] < min_value:
            min_value = arr[num]
        if num > max_value:
            max_value = arr[num]

    # Calculate the range of values
    value_range = max_value - min_value + 1

    # Create a count array with length equal to the value range
    count = StaticArray(value_range)

    # Count the occurrences of each element in the input array
    for num in range(length):
        count[num - min_value] += 1

    # Calculate the cumulative sum of the count array
    total = 0
    for i in range(count.length()):
        count[i], total = total, total + count[i]

    # Create a new output array with the same length as the input array
    output = StaticArray(length)

    # Place the elements in the output array at the correct positions
    for num in range(length):
        output[count[arr[num] - min_value]] = arr[num]
        count[num - min_value] += 1

    return output


# ------------------- PROBLEM 10 - TRANSFORM_STRING ---------------------------

def transform_string(source: str, s1: str, s2: str) -> str:
    """
    TODO: Write this implementation
    """
    transformed_string = ''

    for character in source:
        index = s1.find(character)
        if index >= 0:
            transformed_string = transformed_string + s2[index]
        elif character.isupper():
            transformed_string = transformed_string + ' '
        elif character.islower():
            transformed_string = transformed_string + '#'
        elif character.isdigit():
            transformed_string = transformed_string + '!'
        else:
            transformed_string = transformed_string + '='

    return transformed_string


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# transform_string example 1\n')
    original = (
        '#     #  =====  !      =====  =====  #     #  =====',
        '#  #  #  !      !      !      !   !  ##   ##  !    ',
        '# # # #  !===   !      !      !   !  # # # #  !=== ',
        '##   ##  !      !      !      !   !  #  #  #  !    ',
        '#     #  =====  =====  =====  =====  #     #  =====',
        '                                                   ',
        '         TTTTT OOOOO      22222   66666    1       ',
        '           T   O   O          2   6       11       ',
        '           T   O   O       222    66666    1       ',
        '           T   O   O      2       6   6    1       ',
        '           T   OOOOO      22222   66666   111      ',
    )
    test_cases = ('eMKCPVkRI%~}+$GW9EOQNMI!_%{#ED}#=-~WJbFNWSQqDO-..@}',
                  'dGAqJLcNC0YFJQEB5JJKETQ0QOODKF8EYX7BGdzAACmrSL0PVKC',
                  'aLiAnVhSV9}_+QOD3YSIYPR4MCKYUF9QUV9TVvNdFuGqVU4$/%D',
                  'zmRJWfoKC5RDKVYO3PWMATC7BEIIVX9LJR7FKtDXxXLpFG7PESX',
                  'hFKGVErCS$**!<OS<_/.>NR*)<<+IR!,=%?OAiPQJILzMI_#[+}',
                  'EOQUQJLBQLDLAVQSWERAGGAOKUUKOPUWLQSKJNECCPRRXGAUABN',
                  'WGBKTQSGVHHHHHTZZZZZMQKBLC66666NNR11111OKUN2KTGYUIB',
                  'YFOWAOYLWGQHJQXZAUPZPNUCEJABRR6MYR1JASNOTF22MAAGTVA',
                  'GNLXFPEPMYGHQQGZGEPZXGJVEYE666UKNE11111WGNW2NVLCIOK',
                  'VTABNCKEFTJHXATZTYGZVLXLAB6JVGRATY1GEY1PGCO2QFPRUAP',
                  'UTCKYKGJBWMHPYGZZZZZWOKQTM66666GLA11111CPF222RUPCJT')

    for case in test_cases:
        print(transform_string(case, '612HZ', '261TO'))
