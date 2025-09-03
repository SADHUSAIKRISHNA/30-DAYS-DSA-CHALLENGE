from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.q = deque()  
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.q.append(t)

        
        while self.q[0] < t - 3000:
            self.q.popleft()

        return len(self.q)
obj = RecentCounter()
print(obj.ping(1))     
print(obj.ping(100)) 
print(obj.ping(3001))  
print(obj.ping(3002)) 