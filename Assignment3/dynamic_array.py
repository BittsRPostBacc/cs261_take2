# Name:  Randy Bitts
# OSU Email:  bittsr@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment:  Assignment 2 - Dynamic Array and Bag ADT
# Due Date:  7/18/2023
# Description:  Working with Dynamic Arrays, and Bags


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")
    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        Function resizes the array
        """
        # exit if new_capacity is not a positive integer or smaller than current size
        if new_capacity < self._size or new_capacity <= 0:
            return

        new_array = StaticArray(new_capacity)

        for i in range(self._size):
            new_array[i] = self._data[i]

        # update the underlying storage with the resized list, and update the capacity
        self._data = new_array
        self._capacity = new_capacity

    def append(self, value: object) -> None:
        """
        Function appends the value to the end of the array
        """
        if self._size + 1 > self._capacity:
            self.resize(self._capacity * 2)  # check and resize if needed
        self._data[self._size] = value  # add the new value at the end
        self._size += 1  # increment the size

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Function inserts a value at the specified index if possible
        """
        # Check to see if the index is possible, and check to see if the array needs to be resized
        if index < 0 or index > self._size:
            raise DynamicArrayException
        elif index > self._capacity - 1:
            self.resize(self._capacity * 2)

        # If the array is full, resize it
        if self._size == self._capacity:
            self.resize(self._capacity * 2)

        # iterate through the array and move the values so that we can insert into the requested index
        for item in range(self._size, index, -1):
            if self._data[item] is None and self._data[item - 1] is None:
                raise DynamicArrayException
            else:
                self._data[item] = self._data[item - 1]

        # Assign the value to the specified index and increment the size of the array
        self._data[index] = value
        self._size = self._size + 1

    def remove_at_index(self, index: int) -> None:
        """
        Function removes the value at the specified index if possible
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException

        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]

        self._size -= 1

        if self._size <= self._capacity // 4:
            self.resize(max(self._capacity // 2, 4))

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        Function slices an array from a specified index to a specified end
        """
        # Validate that the slice is possible
        if start_index < 0 or size > self._size or start_index + size > self._size or size < 0 or start_index >= self._size:
            raise DynamicArrayException

        # Create the new array and size it accordingly
        sliced_array = DynamicArray()
        if sliced_array._capacity < size:
            sliced_array.resize(sliced_array._capacity * 2)

        end_index = min(start_index + size, self._size)

        for i in range(start_index, end_index):
            sliced_array.append(self._data[i])

        return sliced_array

    def merge(self, second_da: "DynamicArray") -> None:
        """
        Function merges two arrays
        """
        for i in range(second_da._size):
            self.append(second_da._data[i])

    def map(self, map_func) -> "DynamicArray":
        """
        Function maps an array based ona second function
        """
        mapped_array = DynamicArray()
        if mapped_array._capacity < self._capacity:
            mapped_array.resize(self._capacity)

        for item in range(self.length()):
            mapped_value = map_func(self._data[item])
            mapped_array.insert_at_index(item, mapped_value)

        return mapped_array

    def filter(self, filter_func) -> "DynamicArray":
        """
        Function filters an array based on a second function
        """
        filtered_array = DynamicArray()

        for item in range(self.length()):
            if filter_func(self._data[item]) is True:
                filtered_array.append(self._data[item])

        return filtered_array

    def reduce(self, reduce_func, initializer=None) -> object:
        """
       Function reduces an array based on a second function
        """
        return_value = 0

        if self._size == 0:
            if initializer is not None:
                return initializer
            else:
                return None

        if self.length() == 1 and initializer is None:
            return self._data[0]

        if initializer is None:
            start_value = self._data[0]
            start_index = 1
        else:
            start_value = initializer
            start_index = 0

        if self._size == 1 and initializer is None:
            return_value = reduce_func(start_value, 0)
        else:
            for item in range(start_index, self.length()):
                return_value = reduce_func(start_value, self._data[item])
                start_value = return_value

        return return_value

def find_mode(arr: DynamicArray) -> (DynamicArray, int):
    """
    Finds the mode and frequency of an array
    """
    if arr.is_empty():
        raise DynamicArrayException

    modes = DynamicArray()
    max_frequency = 0

    for i in range(arr.length()):
        value = arr[i]
        frequency = 1

        # Check for duplicates from the current index onwards
        for j in range(i + 1, arr.length()):
            if arr[j] == value:
                frequency += 1

        # If we found a new maximum frequency, update the modes array
        if frequency > max_frequency:
            max_frequency = frequency
            modes = DynamicArray([value])
        elif frequency == max_frequency:
            modes.append(value)

    return modes, max_frequency


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    """
    Remove before submission
    """
    print("\n# reduce example from Gradescope")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: (x // 5) + (y ** 2)))

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")
