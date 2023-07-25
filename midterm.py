# Question #6
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
        self.size = 0 
        self.capacity = 4 
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided) 
        # before using this feature, implement append() method 
        if start_array is not None: 
            for value in start_array: 
                self.append(value) 
                

    def dynArrayAddAt(self, index: int, value: object) -> None: 
        """ 
        TODO: Write this implementation 
        """ 
        if index < 0 or index > self.size:
            raise DynamicArrayException
        
        if self.size == self.capacity:
            new_array = StaticArray(self.capacity * 2)
            for i in range(self.size):
                new_array[i] = self.data[i]
            self.data = new_array
            self.capacity = new_array.capacity

        for i in range(self.size, index -1):
            self.data[i] = self.data[i - 1]
        
        self.data[index] = value
        self.size += 1


# Question 10
class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass

class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        self.next = None
        self.value = value

class LinkedList:
    def __init__(self) -> None:
        """
        Initializes a new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def remove_at_index(self, index: int) -> None:
        """
        TODO: Write this implementation
        """
        if index < 0 or self._head is None or index >- self.length():
            raise SLLException

        node = self._head
        for i in range(index):
            node = node.next

        node = node.next.next