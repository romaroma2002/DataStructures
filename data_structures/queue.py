class Queue:

    def __init__(self, *args):
        self.values = [*args]

    def size(self):
        """Returns the size of the queue"""
        return len(self.values)

    def empty(self):
        """Returns whether the queue is empty"""
        return not len(self.values)

    def first(self):
        """Returns the first element of the queue"""
        if self.size():
            return self.values[0]
        raise IndexError("Empty queue")

    def push(self, value):
        """Adds the element to the queue"""
        self.values.insert(0, value)

    def pop(self):
        """Deletes and returns the first element of the queue"""
        if self.size():
            return self.values.pop()
        raise IndexError("Empty queue")
