class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        results = [0]*len(temperatures)

        for i in range(1,len(temperatures)):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                results[index] = i - index
            if len(stack) > 0 and temperatures[i] <= temperatures[stack[-1]] or len(stack) == 0:
                stack.append(i)
        
        return results

        