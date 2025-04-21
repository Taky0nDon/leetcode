'''

Since the input array is sorted and non-decreasing, we can use this information
to decide how to move our pointers. One pointer will start at the beginning of
the array, and the other will start at the end. If the sum of those two
elements is larger than the target, we decrement j, because we know j - 1th
index must be less than or equal to the jth index. For the same reason, we know
the i + 1th index must be greater than or equal to the ith index, so if the sum
is smaller than the target, we can increment i. This strategy assures that the
correct pair of elements will be identified in O(n) time.

'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        j = n - 1
        i = 0
        for _ in range(n):
            if numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] < target:
                i += 1
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
