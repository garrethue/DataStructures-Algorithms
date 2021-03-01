class Stack:
    
    #NOTE: user-defined methods have a time complexity of O(1)
    def __init__(self):
        """
        creates a stack that is empty
        it needs no parameters and returns an empty stack
        """
        self.list = []
    
    def push(self, item):
        """
        adds a new item to the top of the stack 
        it needs the item and returns nothing
        """
        self.list.append(item)
    
    def pop(self):
        """
        removes the top item from the stack. 
        it needs no params and returns the item. The stack is MODIFIED
        """
        return self.list.pop()
    
    def peek(self):
        """
        returns the top item from the stack but does not remove it
        it needs no params and the stack is NOT MODIFIED
        """
        return self.list[len(self.list) - 1]
    
    def is_empty(self):
        """
        tests to see whether the stack is empty
        it needs no params and returns a boolean value
        """
        return len(self.list) == 0
    
    def size(self):
        """
        returns the number of items on the stack
        it needs no params and returns an integer
        """
        return len(self.list)