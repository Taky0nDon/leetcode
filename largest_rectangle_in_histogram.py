
'''
- can only form a rectangle if adjacent bar is of greater or equal height
- keep tracking of largest rectangle while going through
- is changing the height while sacrificing width worth it?
- left boundary : h[left] < h[i]
- right boundary: h[right] < h[i]
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        stack = []
        for i in range(n):
            last_index = i
            print(f"index: {i}, height: {heights[i]}, stack: {stack}, max: {max_area}")
            if stack:
                while stack and heights[i] < stack[-1][1]:
                    max_area = max(max_area, stack[-1][1] * ( i - stack[-1][0]))
                    last_index, last_height = stack.pop()
                stack.append((last_index, heights[i]))
            else:
                stack.append((i, heights[i]))
        if not stack:
            return max_area
        else:
            return max(*[e[1]*(n - e[0]) for e in stack], max_area)
'''
I wrote the code after watching the video explanation of the algorithm, but
before seeing any implementation details. They key thing I was missing was 
the conditions under which to start popping from the stack.
'''
            
