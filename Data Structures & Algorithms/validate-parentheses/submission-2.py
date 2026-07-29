class Solution:
    def isValid(self, s: str) -> bool:
        openparentheses = []
        valids = {"(": ")", "[": "]", "{": "}"}

        for char in s:
            if char in "([{":                           
                openparentheses.append(char)
            elif char in ")]}":                         
                if not openparentheses:                 
                    return False
                top = openparentheses[-1]               
                if valids[top] != char:                 
                    return False
                openparentheses.pop()                  

        return not openparentheses                      