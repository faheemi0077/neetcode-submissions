class MinStack:

    def __init__(self):
        self.mystack = []
        self.size = 0

    def push(self, val: int) -> None:
        self.mystack.append(val)

    def pop(self) -> None:
        del(self.mystack[-1])

    def top(self) -> int:
        return self.mystack[-1]
    def getMin(self) -> int:
        minelement = self.mystack[0]
        for i in range(len(self.mystack)):
            if self.mystack[i] < minelement:
                minelement = self.mystack[i]
        return minelement
