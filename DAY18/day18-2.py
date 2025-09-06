import heapq

class Solution(object):
    def kClosest(self, points, k):
        heap = []
        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(heap, (dist, [x, y]))
        
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result
points = [[1,3],[-2,2],[5,8],[0,1]]
k = 2
sol = Solution()
print(sol.kClosest(points, k))  # Output: [[-2,2],[0,1]]    