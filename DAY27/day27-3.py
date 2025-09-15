class Solution:
    def countComponents(self, n, edges):
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
        count = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
        return count
n = 5
edges = [[0,1], [1,2], [3,4]]
sol = Solution()
print(sol.countComponents(n, edges)) # Output: 2
