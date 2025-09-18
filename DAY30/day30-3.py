class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        cost = [float('inf')] * n
        cost[src] = 0

        for _ in range(k + 1):
            temp = cost[:]
            for u, v, w in flights:
                if cost[u] != float('inf'):
                    temp[v] = min(temp[v], cost[u] + w)
            cost = temp

        return -1 if cost[dst] == float('inf') else cost[dst]
n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 3, 100], [0, 3, 500]]
src = 0
dst = 3
k = 1

sol = Solution()
print(sol.findCheapestPrice(n, flights, src, dst, k))  # Output: 500    
    