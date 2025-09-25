from typing import *

class Solution:
   
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int: # mind blowing solution
        total_tank = 0     # total gas - total cost over the whole trip
        curr_tank = 0      # current tank during the simulation
        start_index = 0    # where we will try to start

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_tank += diff
            curr_tank += diff

            # If we run out of fuel at station i
            if curr_tank < 0:
                # This means all stations from start_index to i can't be the answer
                start_index = i + 1
                curr_tank = 0

        # Final decision
        return start_index if total_tank >= 0 else -1

    def canCompleteCircuit1(self, gas: List[int], cost: List[int]) -> int: # slower.
        n = len(gas)
        start = 0
        end = 0
        fuel = 0
        visited = 0  # how many stations have been passed

        while visited < n:
            fuel += gas[end] - cost[end]
            visited += 1
            end = (end + 1) % n

            while fuel < 0 and visited > 0:
                # shrink from start
                fuel -= gas[start] - cost[start]
                start = (start + 1) % n
                visited -= 1
                # if we've tried all stations as start
                if start == 0:
                    return -1

        return start
