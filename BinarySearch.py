'''
this one is super basic, but I refused to look at the answer since I was
already aware of the general idea. I had to get a hint to use two pointers, but
once I got that, I worked out the details on my own until it worked. That's why it's
so ugly.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        i = (r - l + 1) // 2
        while l < r:
            if nums[i] == target:
                return i
            elif l == r:
                return -1
            if nums[i] < target:  # Search the right half
                l = i + 1
                i += (r - l + 1) // 2
            elif nums[i] > target:  # Search the left half
                r = i - 1
                i -= (r - l + 1) // 2
        if r == l and nums[r] == target:
            return r
        else:
            return -1
