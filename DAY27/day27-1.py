from collections import deque
class Solution(object):
    def isBipartite(self, graph):
        color = [-1] * len(graph)
        for i in range(len(graph)):
            if color[i] == -1:
                queue = deque([i])
                color[i] = 0
                while queue:
                    node = queue.popleft()
                    for nei in graph[node]:
                        if color[nei] == -1:
                            color[nei] = 1 - color[node]
                            queue.append(nei)
                        elif color[nei] == color[node]:
                            return False
        return True
graph1 = [[1,3],[0,2],[1,3],[0,2]]
print(Solution().isBipartite(graph1))  
graph2 = [[1,2,3],[0,2],[0,1,3],[0,2]]
print(Solution().isBipartite(graph2))  
