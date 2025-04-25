
'''
- two pointers start at left
- need to look for local minima
- zero is lowest possible height of bar
- if L or R is 0, move it to the rcight
- find area between bars, but remove occupied area
- begin by finding local minima
- local minima is when H[i] < H[i - 1] and H [i] < H[i + 3]
- move pointers out from min until reach local maxima
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        # brute force
        n = len(height)
        water_area = 0
        for i in range(1, n - 1):
            r = max(height[i:])
            l = max(height[:i])
            water_area += max(min(r,l) - height[i], 0)
            print(f"{water_area=}")
        return water_area
