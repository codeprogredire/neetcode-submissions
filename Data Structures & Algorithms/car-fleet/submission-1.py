class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for p,s in zip(position,speed):
            cars.append((p,s))
        
        cars.sort(key=lambda x:x[0],reverse=True)
        
        stack = []

        for car in cars:
            stack.append(car)
            if len(stack)>=2:
                meet = (target-stack[-1][0])/stack[-1][1] <= (target-stack[-2][0])/stack[-2][1]
                if meet:
                    stack.pop()
        
        return len(stack)
        