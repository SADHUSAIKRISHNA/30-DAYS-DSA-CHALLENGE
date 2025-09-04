class Solution(object):
    def reconstructQueue(self, people):
        people.sort(key=lambda x: (-x[0], x[1]))
        result = []
        for person in people:
            result.insert(person[1], person)
        return result
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
solution = Solution()
print(solution.reconstructQueue(people))    