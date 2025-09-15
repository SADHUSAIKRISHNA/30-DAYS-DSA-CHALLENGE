class Solution:
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False

        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n
n = 5
edges = [[0,1], [0,2], [0,3], [1,4]]

sol = Solution()
print(sol.validTree(n, edges))  # Output: True
