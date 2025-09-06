import heapq

class MedianFinder:
    def __init__(self):
        self.low = []   
        self.high = []  
    def addNum(self, num):
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))
    def findMedian(self):
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2.0
finder = MedianFinder()
finder.addNum(1)
finder.addNum(2)
print("Median after [1, 2]:", finder.findMedian())  
finder.addNum(3)
print("Median after [1, 2, 3]:", finder.findMedian())  
finder.addNum(4)
finder.addNum(5)
print("Median after [1, 2, 3, 4, 5]:", finder.findMedian())  