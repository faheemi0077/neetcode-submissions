class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        mystack = []
        for i in range(len(temperatures)):
            while mystack and temperatures[i] > temperatures[mystack[-1]]:
                 j = mystack.pop()
                 result[j] = i - j
            mystack.append(i)
        return result

                