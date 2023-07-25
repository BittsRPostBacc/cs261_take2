# Name: Randy Bitts
# OSU Email: bittsr@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 3 - Linked List and ADT Implementation
# Due Date: 07/24/23
# Description: Linked List and other ADT Implementations


from SLNode import SLNode


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self) -> None:
        """
        Initialize new stack with head node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'STACK ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        Puts the passed value to the top of the stack
        """
        new_node = SLNode(value)
        node = self._head

        if self.is_empty():
            self._head = new_node
        else:
            length = self.size()
            for item in range(length):
                self._head = new_node
                self._head.next = node
                node = self._head.next

    def pop(self) -> object:
        """
        Removes the value from the top of the stack and returns it
        """
        popped_value = 0

        if self.is_empty():
            raise StackException
        else:
            popped_value = self._head.value
            self._head = self._head.next

        return popped_value

    def top(self) -> object:
        """
        Returns the value at the top of the stack
        """

        if self.is_empty():
            raise StackException
        else:
            return self._head.value

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
