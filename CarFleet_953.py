'''
car[i] is at position[i] miles and going speed[i] mph
destination is at target miles
cars cannot pass! car[i-1] can only catch up to car[i] and then go at its speed.
cars driving at the same position and going the same speed count as a car fleet
if a car catches up to the fleet the moment the fleet reaches target, that car is
part of the fleet
return number of different car fleets that will arrive at the destination

example:
target = 10; position = [1,4]; speed = [3,2]
car[0] is at mile 1 and going 3 mph
car[1] is at mile 4 and going 2 mph
tick 0: {1,3} {4, 2}
tick 1: {4,3} {6, 2}
tick 2: {7,3} {8, 2}
tick 3: {10,3} {10, 2}

example 2:
target = 10
tick 0 {0,1} {1,2} {4,2} {7,1}
tick 1 {1,1} {3,2} {6,2} {8,1}
tick 2 {2,1} {5,2} {8,2} {9,1}
tick 3 {3,1} {7,2} {10,2} {10,1}
sort by position?
sort by descending order because you will pop the cars with starting positions closest to the
target first
monotonically increasing stack wrt car[i] distance from target? 

(target - pos) / speed = ticks remaining
a stack to track cars current positions, popping when it >= target?
if time_to_target[i - 1] > time_to_target[i], time_to_target[i] = time_to_target[i-1], need to remember
mapping time_to_target index to original speed index
'''
from math import ceil
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = sorted(list(zip(position,speed)), key=lambda x: x[0])
        ttd = [(target - cars[i][0])/cars[i][1] for i in range(n)]
        print(ttd)
        stack = [ttd[-1]]
        for i in range(n-2, -1, -1):
            if ttd[i] > stack[-1]:
                stack.append(ttd[i])
        return len(stack)

'''
I failed to solve this one on my own. However, after watching only the
portion of the NeetCode video where he discusses the problem and explains
the reasoning behind his solution, I wrote the code myself. The key thing
I was missing was how the stack should be utilized. While iterating over the
list of cars (sorted in ascending order of position), once a car joins a fleet,
only the car at the head of the fleet is relevant. The cars are essentially merged,
both having the same speed and position. That means they can be safely ignored.
By only adding the relevant cars to the stack, the length of the stack is the
number of fleets by the time every car has reached the destination. I got that
the time for a car to reach the destination could be calculated and used to determine when
adjacent cars would become a fleet, and that the cars should be gone over in sorted order.
I just couldn't figure out how to keep track of when a fleet ended, and a new fleet begna.
'''
