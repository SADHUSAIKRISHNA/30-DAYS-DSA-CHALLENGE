from collections import deque
class RecentCounter(object):
    def __init__(self):
        self.q = deque()  

    def ping(self, t):
        self.q.append(t)  
        while self.q[0] < t - 3000:
            self.q.popleft()

        return len(self.q)  
obj = RecentCounter()
print(obj.ping(1))     # [1] → returns 1
print(obj.ping(100))   # [1, 100] → returns 2
print(obj.ping(3001))  # [1, 100, 3001] → all within 3000 → returns 3
print(obj.ping(3002))  # [100, 3001, 3002] → 1 is removed → returns 3    