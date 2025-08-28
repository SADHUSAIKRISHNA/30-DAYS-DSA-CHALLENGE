class MyCircularQueue(object):

    def __init__(self, k):
        self.queue = [None] * k  # Fixed-size list
        self.size = k
        self.front = 0
        self.rear = -1
        self.count = 0

    def enQueue(self, value):
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        self.count += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size
q = MyCircularQueue(3)
print(q.enQueue(10))  # True
print(q.enQueue(20))  # True
print(q.enQueue(30))  # True
print(q.enQueue(40))  # False (queue is full)
print(q.Rear())       # 30
print(q.isFull())     # True
print(q.deQueue())    # True
print(q.enQueue(40))  # True
print(q.Rear())       # 40    