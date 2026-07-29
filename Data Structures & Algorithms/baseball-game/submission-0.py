class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for i in range(len(operations)):
            try:
                int(operations[i])
                scores.append(int(operations[i]))
            except:
                if operations[i] == "+":
                    score = scores[-1] + scores[-2]
                    scores.append(score)
                elif operations[i] == "D":
                    score = scores[-1] * 2
                    scores.append(score)
                elif operations[i] == "C":
                    scores.pop()
        scores = [int(score) for score in scores]
        return sum(scores)