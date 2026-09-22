class TimeMap:

    def __init__(self):
        self.themap = dict() 

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.themap.setdefault(key, []).append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.themap:
            return ""
        array = self.themap[key]
        left = 0
        right = len(array) - 1
        closest = ""
        while left <= right:
            mid = left + ((right - left) // 2)
            if array[mid][1] < timestamp:
                left = mid + 1
                closest = array[mid][0]
            elif array[mid][1] > timestamp:
                right = mid - 1
            else:
                return array[mid][0]
        return closest