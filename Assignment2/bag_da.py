# Name:  Randy Bitts
# OSU Email:  bittsr@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment:  Assignment 2 - Dynamic Array and Bag ADT
# Due Date:  7/18/2023
# Description:  Working with Dynamic Arrays, and Bags


from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------
    def add(self, value: object) -> None:
        """
        Adds a value to the Bag
        """
        self._da.append(value)

    def remove(self, value: object) -> bool:
        """
        Removes a value from the Bag
        """
        bag_length = self._da.length()

        for i in range(bag_length):
            if self._da[i] == value:
                self._da.remove_at_index(i)
                return True

        return False

    def count(self, value: object) -> int:
        """
        Counts the number of items in the Bag that match the passed in Value, if any
        """
        counter = 0
        length = self._da.length()

        for x in range(length):
            if self._da[x] == value:
                counter += 1

        return counter

    def clear(self) -> None:
        """
        Clears the Bag
        """
        length = self._da.length()
        count = 0

        while count < length:
            self._da.remove_at_index(0)
            count += 1

    def equal(self, second_bag: "Bag") -> bool:
        """
        Determines if two Bags are equal
        """
        bag1_length = self._da.length()
        bag2_length = second_bag._da.length()

        if bag1_length == 0 and bag2_length == 0:
            return True
        elif bag1_length != bag2_length:
            return False

        for i in range(bag1_length):
            element = self._da.get_at_index(i)
            if self.count(element) != second_bag.count(element):
                return False
        return True

    def __iter__(self):
        """
        Allows the bag to iterate across itself
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Gets the next value in the bag
        """
        if self._index < self._da.length():
            value = self._da.get_at_index(self._index)
            self._index += 1
        else:
            raise StopIteration

        return value
# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
