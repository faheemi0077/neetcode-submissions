class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniors = 0
        for detail in details:
            age = detail[11:13]
            if int(age) > 60:
                seniors += 1
        return seniors