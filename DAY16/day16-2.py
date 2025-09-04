class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total_tank = 0
        curr_tank = 0
        start_index = 0

        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            total_tank += gain
            curr_tank += gain

            if curr_tank < 0:
                start_index = i + 1
                curr_tank = 0

        return start_index if total_tank >= 0 else -1
gas  = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

solution = Solution()
result = solution.canCompleteCircuit(gas, cost)
print("Starting station index to complete the circuit:", result)