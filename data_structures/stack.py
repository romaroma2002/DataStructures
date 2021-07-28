class Stack:

    def __init__(self, *args):
        self.values = [*args]

    def size(self):
        """Returns the size of the stack"""
        return len(self.values)

    def empty(self):
        """Returns whether the stack is empty"""
        return not len(self.values)

    def last(self):
        """Returns the last element of the stack"""
        if self.size():
            return self.values[-1]
        raise IndexError("Empty stack")

    def push(self, value):
        """Adds the element to the stack"""
        self.values.append(value)

    def pop(self):
        """Deletes and returns the last element of the stack"""
        if self.size():
            return self.values.pop()
        raise IndexError("Empty stack")
