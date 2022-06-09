class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        stack = []
        
        for pos, speed in sorted(zip(position, speed))[::-1]:
            t = (target-pos)/speed
            if not stack:
                stack.append(t)
            elif t > stack[-1]:
                stack.append(t)
        
        return len(stack)
                