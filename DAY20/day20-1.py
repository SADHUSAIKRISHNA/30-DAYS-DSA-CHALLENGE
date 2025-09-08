from collections import deque
class RecentCounter(object):
    def __init__(self):
        self.q = deque()   
    def ping(self, t):
        self.q.append(t)   
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)
rc = RecentCounter()
print(rc.ping(1))     
print(rc.ping(100))  
print(rc.ping(3001))  
print(rc.ping(3002))  