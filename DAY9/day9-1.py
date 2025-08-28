class MyQueue(object):

    def __init__(self):
        self.stack_in = []   
        self.stack_out = []  

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_in.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.peek()  
        return self.stack_out.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack_in and not self.stack_out
q = MyQueue()
q.push(10)
q.push(20)
q.push(30)

print(q.peek())  
print(q.pop())  
print(q.peek()) 
print(q.empty())        